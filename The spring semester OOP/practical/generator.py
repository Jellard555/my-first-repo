#作用：用 yield 实现迭代器，惰性计算，比推导式更省内存
#特点：下次调用从 yield 下一行继续执行

def my_gen():
    n = 1
    print("first print")
    yield n
    
    n += 1
    print("second print")
    yield n

    n += 3
    print("third print")
    yield n

a = my_gen()
# We can iterate through the items using next().
next(a)
next(a)
next(a)
# when the function terminates, StopIteration is raised automatically on further calls.
next(a)


