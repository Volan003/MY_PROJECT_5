import time


def log(filename="mylog.txt"):
    '''Декоратор, автоматически регистрирующий детали выполнения функций'''
    def decorator(func):
        def wrapper(*args, **kwargs):

            try:
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                log_message = (f'Функция {func.__name__} ok\n start_time:{start_time}\n'
                               f' end_time:{end_time}\n {result}')
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message)
                return result

            except Exception as e:
                error_type = type(e).__name__
                log_message = f'Функция {func.__name__} error: {error_type}. Inputs: {args}, {kwargs}'
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
                raise

        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
