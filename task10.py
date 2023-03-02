import time
def countTime(func):
    def decor_func(*arg):
        time1 = time.perf_counter()
        func(*arg)
        time2 = time.perf_counter()
        print(time2 - time1)
    return decor_func
