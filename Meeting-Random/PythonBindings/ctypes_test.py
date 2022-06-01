import ctypes
import pathlib

if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = pathlib.Path().absolute() / "libcmult.so"
    c_lib = ctypes.CDLL(libname)

    x, y = 6, 2.3

    c_lib.cmult.restype = ctypes.c_float

    s = c_lib.cmult(x, ctypes.c_float(y))

    print(f"    In Python: int: {x} float {y:.1f} return val {s:.1f}")
