def fibonacci(bound):
    #returns the smallest finbonacci number GREATER than the bound

    previous=1 #FIRST FIBONACCI NUMBER
    current=1  #SECOND FIBONACCI NUMBER
    while current<=bound:
        #current becomes previous, and new current is computed
        previous=current
        current=previous+current
    return current
print(fibonacci(52))

def cities():#THIS VERSION CAN BE OPTOMIZED BECAUSE IT HAS REDUNDANT CODE
    #returns the list of cities that are interactively entered by the user;
    #EMPTY STRING ENDS THE USER INPUT
    list=[]

    city=input('Enter the name of the city')
    while(city!=''):
        list.append(city)
        #AFTER YOU HAVE APPENDED THE CITY TO A LIST
        #YOU WANT TO ASK THE USER FOR ANOTHER CITY
        city=input('Enter the name of another city')
    return list

printedList=cities()
print(printedList)
def citiesImproved():
    #RETURNS THE LIST OF CITIES THAT ARE INTERACTIVELY ENTERED BY THE USER; THE EMPTY STRING ENDS THE INTERACTIVE INPUT
    list=[]
    city=input('Enter the name of the city ')
    while True:
        if(city== ''): #IF CITY IS THE FLAG VALUE YOU WANT TO RETURN THE LIST
            return list #RETURN LIST
        list.append(city) #APPENDS CITY TO LIST

#citiesImproved()
