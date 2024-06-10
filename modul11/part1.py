# pylint: disable=unused-argument
# """
# This is an example
# """
import time


def my_sleep(val: int, arg1):
    """
    This function is used as example
    :param val:
    :param arg1: this should be a string
    :return:
    """
    print("before sleep")
    try:
        time.sleep(val)
    except Exception:  # pylint: disable=broad-except
        print("Exception encountered")
    finally:
        print("completed")

def my_sleep2(val: int, arg1):
    """
    This function is used as example
    :param val:
    :param arg1: this should be a string
    :return:
    """
    print("before sleep")
