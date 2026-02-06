def f():
    return 5

def foo(tab=f()):
    return tab

print(foo())


print(((), 5))