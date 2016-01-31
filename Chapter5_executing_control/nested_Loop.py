#
'''
n=5
for j in range(n):#OUTER LOOP ITERATES 5 TIMES
    for i in range(n):#INNER LOOP PRINTS 0 1 2 3 4
        print(i, end=' ')
    print(end=' \n')
'''
def nested(n):
    #prints n lines each containing values 0 1 2 ...  n-1

     for j in range(n): #REPEAT N TIMES
         for i in range(n): # PRINT 0, 1, ..., n-1
             print(i, end=' ')
         print()
#nested(5)

def nested2(n):
    #PRINTS N LINES 0 1 2 ... J FOR J=0, 1, ..., n-1
    for j in range(n):
        #NEED TO START WITH J+1 BECAUSE INITIALLY IF J EQUALS 0, THEN THERE IS NO OUTPUT
        for i in range(j+1):  #print 0 1 2 ... j
            print(i,end='')
        print()

#nested2(4)

#DOESNT PRINT ANYTHING BECAUSE RANGE IS ZERO
#ALWAYS NEED RANGE TO HAVE A VALUE GREATER THAN ZERO OR ELSE IT IS MEANINGLESS
for x in range(0):
    print('hello')

for x in range(1):
    print('hello')
