try:
    #try block
    strAge=input('Enter your age')
    intAge=int(strAge)
    print('You are {} years old.'.format(intAge))
except ValueError:
    #except block---executed only if valueError
    #exception is raised in the try block
    print('Enter your digits 0-9!')
