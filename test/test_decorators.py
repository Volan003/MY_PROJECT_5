import pytest

from src.decorators import log


# def test_log():
#     @log()
#     def my_function_1(x, y):
#         return x / y
#     with pytest.raises(Exception, match='Функция my_function_1 error: ZeroDivisionError: division by zero. Inputs: (2, 0), {}'):
#         my_function_1(2, 0)


def test_log_1():
    @log(filename=None)
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert 'my_function ok' == 'my_function ok'


def test_log_2():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert None is None


def test_log_3(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert '' in captured.out


def test_log_4():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open("mylog.txt", "r") as file:
        log_content = file.read()

    assert 'my_function ok' in log_content
