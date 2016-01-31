#QUESTION 1
def Q1():
    boolExprs=[3>2,0==0,True,False,True or False,not False]
    trueCount=0
    for expr in boolExprs:
        if expr:
            trueCount+=1
    print(trueCount)
print("The answer to question 1 is: ")
Q1()

def Q2():
    aSequence=[-1,0,'str','0']
    sum=aSequence[0]+aSequence[-1]
    print(sum)

print("The answer to question 2 is: ")
#Q2()

def Q3():
    nested=[['0'],'0','0']
    print(nested[:1])
    #PREVIOUS STATEMENT SUGGEST PRINT UP TO BUT NOT
    #INCLUDING THE FIRST ELEMENT

print("The answer to question 3 is: ")
Q3()

def Q4():
    types=['chocolate','vanilla','birthday','retirement']
    occasions=types[-2:]
    print(types-occasions)
print("Q4 PRODUCES AN ERROR AND IS THEREFORE COMMENTED OUT")
#Q4()
'''
def Q5():
    import turtle
    s=turtle._Screen()
    t=turtle.Turtle()
    for i in range(6):
        t.foward(100)
        t.left(120)
print("The answer to question 4 is: ")
Q5()
'''



def Q6(int1,thing1):
    for i in range(int1):
        return thing1

returned=Q6(2,'a')
print("The answer to Q6 is: ")
print(returned)

def Q7():
    wishesWereFishes=True
    wishesWereHorses=True
    if wishesWereFishes:
        print('beggars would eat')
    elif wishesWereHorses:
        print('beggars would ride')
    else:
        print('sad rhyme but true')

print("The answer to Q7 is: ")
Q7()

def Q8():
    bogie=['Here','looking','at','you','kid']
    short=[]
    for word in bogie:
        if len(word)<=3:
            short.append(word)
    print(short)

print("The answer to Q8 is: ")
Q8()

#THIS IS QUESTION 9
'''print(zero())
def zero():
    return 0
'''

#THIS IS QUESTION 10
def echo(param):
    return param

print('here')
print(echo('there'))




