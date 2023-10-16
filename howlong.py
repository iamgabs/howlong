import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        total_time = end - start
        print(f"Execution time for call {func.__name__} : {total_time} seconds")
        return result
    return wrapper
