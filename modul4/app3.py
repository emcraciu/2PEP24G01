# Create context that logs exceptions to file
import sys
import traceback

class ExceptionLogger:

    def __init__(self, file_name):
        self.file_stream = open(file_name, 'w')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(traceback.format_exc())
        self.file_stream.write(exc_tb.tb_frame.f_locals['__file__'])
        self.file_stream.write(f'\n{traceback.format_exc()}')
        self.file_stream.flush()
        self.file_stream.close()
        return True


with ExceptionLogger('another_ex.log'):
    raise ValueError('This is my custom Exception')
