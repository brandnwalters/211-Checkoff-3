import ctypes
import sys
from pathlib import Path

filename = "libsquare_all.dylib" if sys.platform == "darwin" else "libsquare_all.so"
library_path = Path(__file__).resolve().with_name(filename)
library = ctypes.CDLL(str(library_path))

square_all = library.square_all
square_all.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_size_t]
square_all.restype = None  # The C function returns void.

original = [3.0, -4.0, 0.5]
DoubleArray = ctypes.c_double * len(original)
buffer = DoubleArray(*original)

print("Before:", list(buffer))
square_all(buffer, len(buffer))
print("After: ", list(buffer))

assert list(buffer) == [9.0, 16.0, 0.25]
assert original == [3.0, -4.0, 0.5]
print("Both checks passed.")
