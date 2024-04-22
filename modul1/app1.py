"""Decorator to execute function only during working hours"""

# decorator
def working_hours(start: int, stop: int):
    pass

@working_hours(9, 22)
def alarm():
    print('Wake UP!!!!')