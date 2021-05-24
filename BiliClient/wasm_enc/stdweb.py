from enum import IntEnum
from weakref import WeakKeyDictionary
from typing import Any

from .rustwasm import RustWasm

__all__ = 'StdWeb', 'Object', 'Array'

class Object(dict):
    def __getattr__(self, name: str) -> Any:
        if name not in self:
            raise AttributeError(f"The object has no attribute '{name}'")

        value = self[name]

        if not isinstance(value, Object) and isinstance(value, dict):
            value = Object(value)
            self[name] = value

        return value

    def __hash__(self) -> int:
        return id(self)

class Array(list):
    @property
    def length(self) -> int:
        return len(self)

    def __hash__(self) -> int:
        return id(self)

class ValueKind(IntEnum):
    UNDEFINED = 0
    NONE = 1
    INT = 2
    FLOAT = 3
    STRING = 4
    FAlSE = 5
    TRUE = 6
    ARRAY = 7
    OBJECT = 8
    ANY = 9
    # ...

class StdWeb:
    def __init__(self, rustwasm: RustWasm) -> None:
        self.wasm = rustwasm
        self.tmp = None
        self.id_to_ref_map = {}
        self.id_to_refcount_map = {}
        self.ref_to_id_map = WeakKeyDictionary()
        self.last_refid = 1

    def alloc(self, size: int) -> int:
        return self.wasm.web_malloc(size)

    def prepare_any_arg(self, value: Any) -> int:
        address = self.alloc(16)
        self.from_py(address, value)
        return address

    def acquire_tmp(self) -> Any:
        value = self.tmp
        self.tmp = None
        return value

    def acquire_py_reference(self, refid: int) -> Any:
        return self.id_to_ref_map[refid]

    def acquire_rust_reference(self, ref: Any) -> int:
        if ref is None:
            return 0

        ref_to_id_map = self.ref_to_id_map
        id_to_ref_map = self.id_to_ref_map
        id_to_refcount_map = self.id_to_refcount_map

        refid = ref_to_id_map.get(ref)

        if refid is None:
            ref_to_id_map[ref] = refid = self.last_refid
            self.last_refid += 1

        if refid in id_to_ref_map:
            id_to_refcount_map[refid] += 1
        else:
            id_to_ref_map[refid] = ref
            id_to_refcount_map[refid] = 1

        return refid

    def increment_refcount(self, refid: int) -> None:
        self.id_to_refcount_map[refid] += 1

    def decrement_refcount(self, refid: int) -> None:
        id_to_refcount_map = self.id_to_refcount_map

        if 0 == id_to_refcount_map[refid] - 1:
            del self.id_to_ref_map[refid]
            del id_to_refcount_map[refid]

    def from_py(self, address: int, value: Any) -> None:
        wasm = self.wasm

        if value is None:
            wasm.HEAPU8[address + 12] = ValueKind.NONE
        elif value is True:
            wasm.HEAPU8[address + 12] = ValueKind.TRUE
        elif value is False:
            wasm.HEAPU8[address + 12] = ValueKind.FAlSE
        elif isinstance(value, int): # isinstance(True, int)
            wasm.HEAPU8[address + 12] = ValueKind.INT
            wasm.HEAP32[address >> 2] = value
        elif isinstance(value, float):
            pass
        elif isinstance(value, str):
            wasm.HEAPU8[address + 12] = ValueKind.STRING
            self.to_utf8_string(address, value)
        else:
            refid = self.acquire_rust_reference(value)
            wasm.HEAPU8[address + 12] = ValueKind.ANY
            wasm.HEAP32[address >> 2] = refid

    def to_py(self, address: int) -> Any:
        wasm = self.wasm
        kind = wasm.HEAPU8[address + 12]

        if kind == ValueKind.UNDEFINED:
            raise ValueError(f'Unexpected value kind: {kind}')
        elif kind == ValueKind.NONE:
            value = None
        elif kind == ValueKind.TRUE:
            value = True
        elif kind == ValueKind.FAlSE:
            value = False
        elif kind == ValueKind.INT:
            value = wasm.HEAPU32[address >> 2]
        # elif kind == ValueKind.FLOAT:
        #     pass
        elif kind == ValueKind.STRING:
            pointer = wasm.HEAPU32[address >> 2]
            length = wasm.HEAPU32[(address + 4) >> 2]
            value = self.to_py_string(pointer, length)
        elif kind == ValueKind.ANY:
            refid = wasm.HEAPU32[address >> 2]
            value = self.acquire_py_reference(refid)
        else:
            raise ValueError(f'Unsupported value kind: {kind}')

        return value

    def to_utf8_string(self, address: int, string: str) -> None:
        wasm = self.wasm
        string_bytes = string.encode('utf8')
        length = len(string_bytes)

        if length > 0:
            pointer = self.alloc(length)
            wasm.HEAPU8[pointer:pointer+length] = string_bytes
        else:
            pointer = 0

        wasm.HEAPU32[address >> 2] = pointer
        wasm.HEAPU32[(address + 4) >> 2] = length

    def to_py_string(self, pointer: int, length: int) -> str:
        string_bytes = self.wasm.HEAPU8[pointer:pointer+length]
        return string_bytes.decode('utf8')

    def serialize_array(self, address: int, array: Array) -> None:
        wasm = self.wasm

        length = len(array)
        pointer = self.alloc(length * 16)

        wasm.HEAPU8[address + 12] = ValueKind.ARRAY
        wasm.HEAPU32[address >> 2] = pointer
        wasm.HEAPU32[(address + 4) >> 2] = length

        for i, value in enumerate(array):
            self.from_py(pointer + i * 16, value)

    def serialize_object(self, address: int, obj: Object) -> None:
        pass
