def f(y):
    x=2
    print('In f(): x={},y={}'.format(x,y))
    g(3)
    print('In f(): x={},y={}'.format(x,y))

def g(y):
    x=4
    print('In f():x={},y={}'.format(x,y))

#print(g(3))
print(f(3))