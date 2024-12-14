import sys
print("Python Executable:", sys.executable)
print("sys.path:", sys.path)
try:
    import mpmath
    print("mpmath is available!")
except ModuleNotFoundError:
    print("mpmath is NOT available!")
