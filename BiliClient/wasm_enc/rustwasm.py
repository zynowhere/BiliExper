import struct
from enum import Enum
from typing import Dict, Callable, Any, Union, Optional

from wasmtime import Store, Module, Instance
from wasmtime import Func, Table, Global, Memory

__all__ = 'RustWasm',

class HeapKind(Enum):
    U8 = 0
    S8 = 1
    U16 = 2
    S16 = 3
    U32 = 4
    S32 = 5
    # ...

class Heap:
    __slots__ = 'memory', 'itemsize', 'signed', 'format'

    def __init__(self, memory: Memory, kind: HeapKind) -> None:
        self.memory = memory

        if kind == HeapKind.U8:
            self.itemsize = 1
            self.signed = False
            self.format = '<B'
        elif kind == HeapKind.S8:
            self.itemsize = 1
            self.signed = True
            self.format = '<b'
        elif kind == HeapKind.U16:
            self.itemsize = 2
            self.signed = False
            self.format = '<H'
        elif kind == HeapKind.S16:
            self.itemsize = 2
            self.signed = True
            self.format = '<h'
        elif kind == HeapKind.U32:
            self.itemsize = 4
            self.signed = False
            self.format = '<I'
        elif kind == HeapKind.S32:
            self.itemsize = 4
            self.signed = True
            self.format = '<i'

    def __getitem__(self, index: Union[int, slice]) -> Union[int, bytes]:
        if isinstance(index, int):
            memory = self.memory
            itemsize = self.itemsize

            address = index << (itemsize >> 1)
            if address < 0:
                address += self.size
            self.check_address(address)

            number_bytes = b''
            for i in range(itemsize):
                value = memory.data_ptr[address + i]
                # number_bytes += value.to_bytes(1, byteorder='little')
                number_bytes += struct.pack('B', value)

            # return int.from_bytes(number_bytes, byteorder='little')
            return struct.unpack(self.format, number_bytes)[0]
        elif isinstance(index, slice):
            m = self.memory
            size = self.size

            start = index.start or 0
            stop = index.stop or size
            step = index.step or 1
            if start < 0:
                start += size
            if stop < 0:
                stop += size
            self.check_address(start, stop)

            return bytes(m.data_ptr[a] for a in range(start, stop, step))
        else:
            raise TypeError('Heap indices must be integers or slices')

    def __setitem__(self, index: Union[int, slice], value: Union[int, bytes]) -> None:
        if isinstance(index, int):
            memory = self.memory
            itemsize = self.itemsize

            address = index << (itemsize >> 1)
            if address < 0:
                address += self.size
            self.check_address(address)

            # number_bytes = value.to_bytes(itemsize, byteorder='little', signed=self.signed)
            number_bytes = struct.pack(self.format, value)

            for i in range(itemsize):
                memory.data_ptr[address + i] = number_bytes[i]
        elif isinstance(index, slice):
            memory = self.memory
            size = self.size

            start = index.start or 0
            stop = index.stop or size
            step = index.step or 1
            if start < 0:
                start += size
            if stop < 0:
                stop += size
            self.check_address(start, stop)

            for i, address in enumerate(range(start, stop, step)):
                memory.data_ptr[address] = value[i]
        else:
            raise TypeError('Heap indices must be integers or slices')

    def __len__(self) -> int:
        return self.size

    @property
    def size(self) -> int:
        return self.memory.data_len

    def check_address(self, begin: int, end: Optional[int] = None) -> None:
        if not 0 <= begin < self.size:
            raise ValueError(f'out-of-bounds memory access: {begin}')

        if end is not None and not 0 < end <= self.size:
            raise ValueError(f'out-of-bounds memory access: {end}')

class RustWasm:
    def __init__(self, pathname: str,
                 import_object: Dict[str,
                    Dict[str, Union[Func, Table, Global, Memory, Callable]]
                ]) -> None:
        import_object['env'].update({ '__web_on_grow': lambda : None})

        self.store = store = Store()
        self.module = module = Module.from_file(store.engine, pathname)

        imoprts = []

        for wasm_import in module.imports:
            module_name = wasm_import.module
            filed_name = wasm_import.name
            item = import_object[module_name][filed_name]

            if not isinstance(item, (Func, Table, Global, Memory)):
                item = Func(store, wasm_import.type, item)

            imoprts.append(item)

        self.instance = instance = Instance(store, module, imoprts)
        self.exports = exports = instance.exports
        self.memory = exports['memory']
        self.web_free = exports['__web_free']
        self.web_malloc = exports['__web_malloc']

        self.HEAP8 = Heap(self.memory, HeapKind.S8)
        self.HEAP16 = Heap(self.memory, HeapKind.S16)
        self.HEAP32 = Heap(self.memory, HeapKind.S32)
        self.HEAPU8 = Heap(self.memory, HeapKind.U8)
        self.HEAPU16 = Heap(self.memory, HeapKind.U16)
        self.HEAPU32 = Heap(self.memory, HeapKind.U32)