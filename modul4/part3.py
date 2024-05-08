# context

class FileOpener:

    def __init__(self, file_name, mode):
        print("this will execute first")
        self.file = file_name
        self.file_stream = open(file_name, mode)

    def __enter__(self):
        print(f"File {self.file} is ready for operations")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Completed action on file {self.file}")
        self.file_stream.flush()
        self.file_stream.close()
        if isinstance(exc_val, ValueError):
            print("Ignoring this exception")
            return True
        else:
            print("This exception is unknown it will be raised")
            return False

    def write_something(self):
        print("doing something")
        self.file_stream.write("something")


with FileOpener("example2.py", "w") as fo:
    print("in context1")
    fo.write_something()
    print("in context2")
    # raise IndexError()
    raise ValueError()
