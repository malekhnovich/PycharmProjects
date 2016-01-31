'''
this method is incorrect because index at len(l) is not defined
'''

def checkOrderWrong(l):
    for i in range(len(l)):
        #works properly but index at len(l) is unneccessary
        if(l[i]>=l[i+1]):
            print('The list is not in increasing order')
            return False
        else:
            print('Everything is in its proper order')
            return True



#PROPER WAY TO CHECK THE ORDER BELOW

def checkOrderProperly(l):
    for i in range(len(l)-1):
        if(l[i]>=l[i+1]):
            print('The numbers are not in the proper order')
            return False
        else:
            print('The numbers are in the proper order')
            return True

checkOrderProperly([1,2,3])

#OUTPUTS THE FIRST FIVE ELEMENTS
#REMEMBER THAT THIS DOESNT MEAN THAT IT OUTPUTS UNTIL 5!!!!
for i in range(5):
    print(i)

