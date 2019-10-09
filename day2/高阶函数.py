def bar():
    print('hello')
# 函数名可以赋给其他变量
a = bar
a()


# 函数可以作为参数传递
def foo():
    print('函数可以作为参数传递')
def bar(func):
    func()

bar(foo)
