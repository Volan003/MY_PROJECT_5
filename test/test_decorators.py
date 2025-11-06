import pytest

from src.decorators import my_function, log


# def test_log(error_type=None):
#     with pytest.raises(Exception, match=error_type):
#         my_function()


def test_log_1():
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3  # 3


@log()
def test_function_success():
    return 1 + 1


@log()
def test_function_error():
    return 1 / 0
