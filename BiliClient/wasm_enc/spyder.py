from json import dumps
from pkg_resources import resource_filename
from .rustwasm import RustWasm
from .stdweb import StdWeb, Object, Array
from typing import Dict, Iterable, Union

window = Object({
    'location': {
        'href': 'https://live.bilibili.com/3',
        'origin': 'https://live.bilibili.com',
        'protocol': 'https:',
        'host': 'live.bilibili.com',
        'hostname': 'live.bilibili.com',
        'pathname': '/3',
    },
})

document = Object({
    'body': {
        'childNodes': {
            'length': 1, # >= 1
        },
    }
})

# define imported functions
def __cargo_web_snippet_0f503de1d61309643e0e13a7871406891e3691c9(address: int) -> int:
    stdweb.from_py(address, window)
    return address

def __cargo_web_snippet_6fcce0aae651e2d748e085ff1f800f87625ff8c8(address: int) -> int:
    stdweb.from_py(address, document)
    return address

def __cargo_web_snippet_0d39c013e2144171d64e2fac849140a7e54c939a(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, obj.location)
    return dst 

def __cargo_web_snippet_10f5aa3985855124ab83b21d4e9f7297eb496508(refid: int) -> int:
    val = stdweb.acquire_py_reference(refid)
    return int(isinstance(val, Array))

def __cargo_web_snippet_2b0b92aee0d0de6a955f8e5540d7923636d951ae(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, Object({
        'value': obj.origin,
        'success': True,
    }))
    return dst

def __cargo_web_snippet_461d4581925d5b0bf583a3b445ed676af8701ca6(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, Object({
        'value': obj.host,
        'success': True,
    }))
    return dst

def __cargo_web_snippet_4c895ac2b754e5559c1415b6546d672c58e29da6(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, Object({
        'value': obj.protocol,
        'success': True,
    }))
    return dst

def __cargo_web_snippet_a466a2ab96cd77e1a77dcdb39f4f031701c195fc(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, Object({
        'value': obj.pathname,
        'success': True,
    }))
    return dst

def __cargo_web_snippet_cdf2859151791ce4cad80688b200564fb08a8613(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, Object({
        'value': obj.href,
        'success': True,
    }))
    return dst

def __cargo_web_snippet_e8ef87c41ded1c10f8de3c70dea31a053e19747c(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, Object({
        'value': obj.hostname,
        'success': True,
    }))
    return dst

def __cargo_web_snippet_ab05f53189dacccf2d365ad26daa407d4f7abea9(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, obj.value)
    return dst

def __cargo_web_snippet_b06dde4acf09433b5190a4b001259fe5d4abcbc2(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, obj.success)
    return dst

def __cargo_web_snippet_614a3dd2adb7e9eac4a0ec6e59d37f87e0521c3b(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, obj.error)
    return dst

def __cargo_web_snippet_7ba9f102925446c90affc984f921f414615e07dd(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, obj.body)
    return dst

def __cargo_web_snippet_62ef43cf95b12a9b5cdec1639439c972d6373280(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, obj.childNodes)
    return dst

def __cargo_web_snippet_b33a39de4ca954888e26fe9caa277138e808eeba(dst: int, src: int) -> int:
    obj = stdweb.to_py(src)
    stdweb.from_py(dst, obj.length)
    return dst

def __cargo_web_snippet_80d6d56760c65e49b7be8b6b01c1ea861b046bf0(refid: int) -> int:
    stdweb.decrement_refcount(refid)
    return refid

def __cargo_web_snippet_8c32019649bb581b1b742eeedfc410e2bedd56a6(refid: int, address: int) -> int:
    array = stdweb.acquire_py_reference(refid)
    stdweb.serialize_array(address, array)
    return address 

def __cargo_web_snippet_ff5103e6cc179d13b4c7a785bdce2708fd559fc0(address: int) -> int:
    stdweb.tmp = stdweb.to_py(address)
    return address

def __cargo_web_snippet_897ff2d0160606ea98961935acb125d1ddbf4688(refid: int) -> int:
    # r = stdweb.acquire_py_reference(refid)
    raise NotImplementedError('__cargo_web_snippet_897ff2d0160606ea98961935acb125d1ddbf4688')

def __cargo_web_snippet_e9638d6405ab65f78daf4a5af9c9de14ecf1e2ec(address: int) -> int:
    # o = stdweb.to_py(address)
    raise NotImplementedError('__cargo_web_snippet_e9638d6405ab65f78daf4a5af9c9de14ecf1e2ec')

imports = {
    'env': {
        '__cargo_web_snippet_0d39c013e2144171d64e2fac849140a7e54c939a': __cargo_web_snippet_0d39c013e2144171d64e2fac849140a7e54c939a,
        '__cargo_web_snippet_6fcce0aae651e2d748e085ff1f800f87625ff8c8': __cargo_web_snippet_6fcce0aae651e2d748e085ff1f800f87625ff8c8,
        '__cargo_web_snippet_0f503de1d61309643e0e13a7871406891e3691c9': __cargo_web_snippet_0f503de1d61309643e0e13a7871406891e3691c9,
        '__cargo_web_snippet_10f5aa3985855124ab83b21d4e9f7297eb496508': __cargo_web_snippet_10f5aa3985855124ab83b21d4e9f7297eb496508,
        '__cargo_web_snippet_2b0b92aee0d0de6a955f8e5540d7923636d951ae': __cargo_web_snippet_2b0b92aee0d0de6a955f8e5540d7923636d951ae,
        '__cargo_web_snippet_461d4581925d5b0bf583a3b445ed676af8701ca6': __cargo_web_snippet_461d4581925d5b0bf583a3b445ed676af8701ca6,
        '__cargo_web_snippet_4c895ac2b754e5559c1415b6546d672c58e29da6': __cargo_web_snippet_4c895ac2b754e5559c1415b6546d672c58e29da6,
        '__cargo_web_snippet_a466a2ab96cd77e1a77dcdb39f4f031701c195fc': __cargo_web_snippet_a466a2ab96cd77e1a77dcdb39f4f031701c195fc,
        '__cargo_web_snippet_cdf2859151791ce4cad80688b200564fb08a8613': __cargo_web_snippet_cdf2859151791ce4cad80688b200564fb08a8613,
        '__cargo_web_snippet_e8ef87c41ded1c10f8de3c70dea31a053e19747c': __cargo_web_snippet_e8ef87c41ded1c10f8de3c70dea31a053e19747c,
        '__cargo_web_snippet_ab05f53189dacccf2d365ad26daa407d4f7abea9': __cargo_web_snippet_ab05f53189dacccf2d365ad26daa407d4f7abea9,
        '__cargo_web_snippet_b06dde4acf09433b5190a4b001259fe5d4abcbc2': __cargo_web_snippet_b06dde4acf09433b5190a4b001259fe5d4abcbc2,
        '__cargo_web_snippet_614a3dd2adb7e9eac4a0ec6e59d37f87e0521c3b': __cargo_web_snippet_614a3dd2adb7e9eac4a0ec6e59d37f87e0521c3b,
        '__cargo_web_snippet_7ba9f102925446c90affc984f921f414615e07dd': __cargo_web_snippet_7ba9f102925446c90affc984f921f414615e07dd,
        '__cargo_web_snippet_62ef43cf95b12a9b5cdec1639439c972d6373280': __cargo_web_snippet_62ef43cf95b12a9b5cdec1639439c972d6373280,
        '__cargo_web_snippet_b33a39de4ca954888e26fe9caa277138e808eeba': __cargo_web_snippet_b33a39de4ca954888e26fe9caa277138e808eeba,
        '__cargo_web_snippet_80d6d56760c65e49b7be8b6b01c1ea861b046bf0': __cargo_web_snippet_80d6d56760c65e49b7be8b6b01c1ea861b046bf0,
        '__cargo_web_snippet_8c32019649bb581b1b742eeedfc410e2bedd56a6': __cargo_web_snippet_8c32019649bb581b1b742eeedfc410e2bedd56a6,
        '__cargo_web_snippet_ff5103e6cc179d13b4c7a785bdce2708fd559fc0': __cargo_web_snippet_ff5103e6cc179d13b4c7a785bdce2708fd559fc0,
        '__cargo_web_snippet_897ff2d0160606ea98961935acb125d1ddbf4688': __cargo_web_snippet_897ff2d0160606ea98961935acb125d1ddbf4688,
        '__cargo_web_snippet_e9638d6405ab65f78daf4a5af9c9de14ecf1e2ec': __cargo_web_snippet_e9638d6405ab65f78daf4a5af9c9de14ecf1e2ec,
    }
}

pathname = resource_filename(__name__, 'bili.wasm')
wasm = RustWasm(pathname, imports)
stdweb = StdWeb(wasm)
spyder = wasm.exports['spyder']

def calc_sign(data: Dict[str, Union[str, int]], secret_rule: Iterable[int]) -> str:
    data = data.copy()
    for k in ("id", "device"):
        if not isinstance(data[k], str):
            data[k] = dumps(data[k])
    input_string = dumps(data)
    string_address = stdweb.prepare_any_arg(input_string)
    array_address = stdweb.prepare_any_arg(Array(secret_rule))
    spyder(string_address, array_address)
    return stdweb.acquire_tmp()