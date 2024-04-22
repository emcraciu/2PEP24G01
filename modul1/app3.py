"""Createdecorator for adding customisable delay in function resonse """

def delay(seconds=0):
    pass

@delay(seconds=5)
def area(length: int, width: int):
    return length * width
