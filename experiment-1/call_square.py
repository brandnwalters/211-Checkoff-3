import ctypes
import sys
from pathlib import Path

suffix = ".dylib" if sys.platform == "darwin" else ".so"
library_path = Path(__file__).resolve().with_name(f"libsquare{suffix}")
library = ctypes.CDLL(str(library_path))

square = library.square
square.argtypes = [ctypes.c_double]
square.restype = ctypes.c_double

for value, expected in [(3.0, 9.0), (-4.0, 16.0), (0.5, 0.25)]:
    result = square(value)
    assert isinstance(result, float), type(result)
    assert result == expected, (value, result, expected)
    print(f"square({value}) = {result}")

print("All checks passed")
