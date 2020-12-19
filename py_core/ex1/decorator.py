import time
def total_time(fn):
    def inner():
        start=time.time()
        fn()
        end=time.time()
        print("耗时",end-start)
    return inner

@total_time
def dem1():
    global i
    for i in range(1,10000):
        i+=1

dem1()



