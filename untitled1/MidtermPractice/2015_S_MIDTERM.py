'''
SPRING 2015 MIDTERM
#IMPORTANT TO NOTE THAT THE COUNT(STRING) METHOD IN PYTHON COUNTS THE NUMBER OF INSTANCES OF THE CHARACTER IN THE STRING
#REPEATING IT TO EMPHASIZE IMPORTANCE COUNT(STRING) METHOD IN PYTHON COUNTS THE NUMBER OF INSTANCES OF THE CHARACTER
#IN THE STRING
^ SEE QUESTION 1 FOR AN EXAMPLE


'''

#THIS IS QUESTION 1
def testString(aString):
    aDict={}
    for letter in aString:
        num=aString.count(letter)
        print(num)
        if num not in aDict:
            aDict[num]=letter
            print(aDict)
        else:
            return -1

text='eager'
print("The answer to Q1 is: ")
print(testString(text))

#THIS IS QUESTION2

def container(s1,s2):
    rtnVal=''
    for i in range(len(s2)):
        sub=s2[:i]
        print("sub equals "+sub)
        if sub not in s1:
            rtnVal+=sub
    return rtnVal

t1='hoof'
t2='hoot'
print("The answer to Q2 is ")
print(container(t1,t2))

#THIS IS QUESTION 3
def reflections(t):
    tList=t.split()
    pos=0
    anti=-1
    for word in tList:
        if tList[pos]==tList[anti]:
            return tList[pos]

        pos+=1
        anti-=1
s='a thing worth doing is worth doing well'
print("This is the answer to question 3: ")
reflections(s)

#THIS IS QUESTION 4
word='the'
sub=''
accum=''
for let in word[1:]:
    for subLet in sub:
        if let<subLet:
            accum+=let
            break
    sub+=let
print("This is the answer to question 4: ")
print(accum)

#THIS IS QUESTION 5
spell={1:'one',0:'zero',2:'two'}
print("The answer to question 5 is")
print((spell[0][1]))

numbers="01234"
print(numbers[1:])

#THIS IS QUESTION 5
spell={1:'one',0:'zero',2:'two'}
print("The answer to question 5 is: ")
print((spell[0][1]))

#THIS IS QUESTION 6
ben="Lost time is never found again."

def property(t):
    tList=t.split()#length of tList is 6
    d={}
    for word in tList:#checks each word in tList
        length=len(word)#checks the length of the first word
        if len(word) not in d:
            d[length]=1
        else:
            d[length]+=1
    return d
print('THE ANSWER TO QUESTION 6 IS: ')
print(len(property(ben)))
#print(len(ben.split()))

sz={}
sz[0]=4
print(len(property(ben)))

