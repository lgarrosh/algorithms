import time

class ExecutionTime:
    def decorator_function(func):
        def execute_time(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            time_exec = "{:.6f}".format((end - start) * 1000)
            return(time_exec)
        return (execute_time)
    
    def find_best_time( func1, func2, *args, **kwargs):
        dec_func1 = Self.decorator_function(func1)
        dec_func2 = self.decorator_function(func2)
        first_time = dec_func1(*args, **kwargs)
        second_time = dec_func2(*args, **kwargs)
        print("first function - ", first_time)
        print("second function - ", second_time)
        print("ween - ", "ferst" if first_time < second_time else "second")
