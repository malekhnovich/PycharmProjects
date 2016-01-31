#CREATE AN EMPTY DICTIONARY
empty_dict={}
d={}
#ADD A KEY-VALUE PAIR USING INDEX AND ASSIGNMENT OPERATORS
d['NJIT']='tech'

#LOOK UP THE VALUES OF A KEY USING THE INDEX([]) OPERATOR
print(d['NJIT'])

#CHANGE A VALUE BY ASSIGNING A NEW VALUE
d['NJIT']='tech school'

#REMOVE A KEY-VALUE PAIR AND RETURN ITS VALUE
njitSchoolType=d.pop('NJIT')
print(njitSchoolType)

print(d)

knights={'gallahad':'the pure','robin':'the brave'}
for k,v in knights.items():
    print(k,v)

#WHEN LOOPING THROUGH A SEQUENCE THE POSITION INDEX AND CORRESPONDING VALUE PAIR CAN BE RETRIEVED THROUGH THE enumerate() function
for i, v in enumerate(['tic','tac','toe']):
    print(i,v)

#LOOPING OVER TWO OR MORE SEQUENCES AT THE SAME TIME CAN BE DONE WITH THE ZIP SEQUENCE
questions=['name','quest','favorite color']#THIS IS A LIST BECAUSE OF THE STYLE OF THE BRACKETS ---------> SQQQQQQQQUAAAAARE ---------------> LIST
answers=['lancelot','the holy grail','blue']#THIS IS A LIST BECAUSE OF THE STYLE OF THE BRACKETS ----------> SQQQQQQUAAAAARE ---------------> LIST
for q,a in zip(questions,answers):
    print('What is your {0}? It is {1}.'.format(q,a))

for i in range(1,10,2):
    print("this is in the regular order")
    print(i)

#REVERSING THE PREVIOUS FOR LOOP
for j in reversed(range(1,10,2)):
    print("this is in the reversed order")
    print(j)

