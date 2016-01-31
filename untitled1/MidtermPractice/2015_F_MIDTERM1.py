#QUESTION 1
def Q1():
    boolsSeen=0
    bools=[not True,not False,True,False,True and False,True or False]
    for expr in bools:
        if expr:
            boolsSeen+=1
    print(boolsSeen)
#HINT X+=1 is the same as x=x+1

#ANSWER--> 3
print("The answer to question 1 is: ")
Q1()

def Q2():
    aSeq=[2,1,0,-1,-2]
    sum=aSeq[0]+aSeq[-1]+aSeq[-2]
    print(sum)

#ANSWER--> -1
print("The answer to question2 is: ")
Q2()

def Q3():
    mix=['zero',0,['two'],-1]
    #REMEMBER THAT END INDEX IS UP TO
    #AND NOT INCLUDED !!!!
    print(mix[0:-1])

#ANSWER--> ['zero',0,['two']]
print("The answer to question3 is: ")
Q3()

def Q4():
    aList=['one',-1,2]
    prefix=aList[:2]
    suffix=aList[-1:]
    print(prefix+suffix)

#ANSWER--> ['one',-1,2]
print("The answer to question4 is: ")
Q4()
''''
def Q5():
    import turtle
    s=turtle._Screen()
    t=turtle.Turtle()
    for i in range(4):
        if i%2==0:
            t.right(60)
            t.forward(100)
            t.right(60)

Q5()
'''''
#THIS IS QUESTION 6
def check(aList):
    for element in range(len(aList)):
        if str(aList[element])==aList[element+1]:
            return True
        return False

arg=[0,'0',1,'1']
matched=check(arg)

print('The answer to question 6 is')
#THE ANSWER TO QUESTION 6--> TRUE
print(matched)

def Q7():
    muchSnow=False
    veryCold=True
    takeTrain=True
    if muchSnow:
        print("school closed")
    else:
        print("give exam")
    if veryCold:
        print("car won't start")
    elif takeTrain:
        print("take exam")
    else:
        print("miss exam")

print("The answer to question 7 is")
#Q7 ANSWER--> give exam
#             car won't start
#             None
print(Q7())

def Q8():
    isaac=['I','do','not','fear','computers','I','fear','the','lack','of','them']
    short=3
    shortCount=0

    for word in isaac:
        if len(word)<=short:
            shortCount+=1
    print(shortCount)

print('The answer to question 8 is')
#Q8 ANSWER--> 6
print(Q8())

#QUESTION 9
def notIn(letter,wordList):
    rtnList=[]
    for word in wordList:
        if letter not in word:
            rtnList.append(word)
    return rtnList

quote=['round','up','the','usual','suspects']
#ANSWER TO Q9 --> ['round','up','usual]
print("The answer to question 9 is: ")
print(notIn('e',quote))

#QUESTION 10
def accumulate(sequence):
    returnVal=[]
    for element in sequence:
        returnVal.append(element)

    return returnVal

print("The answer to question 10 is")
#['a','n','a','g','r','a','m']
print(accumulate('anagram'))



