#!!!REMEMBER THAT NO ORDERING ASSUMPTION CAN BE MADE WHEN IT COMES TO DICTIONARY
#!!!INDEX OF DICTIONARIES IS USER-DEFINED BY THE KEY OF THE KEY-VALUE PAIRS
#EXAMPLE OF A DICTIONARY
#THE FIRST NUMBER IS THE REFERENCE TO THE EMPLOYEE
#ACTS AS AN INDEX
#SIMILAR TO KEY-VALUE PAIRS IN JAVA
employee={
          '864312':['Pedro, Martinez'],
          '243123':['Joe, Smith'],
          '123214':['Doc,Pederson']
}
#MUST CALL THE DICT
print(employee['864312'])
#KEY POINT OF DICTIONARIES IS THAT YOU ACCES THEM WITH A USER-DEFINED INDEX
#RATHER THAN THE INDEX GIVEN TO THEM
#print(employee['Pedro, Martinez'])

days={'day0':'Sunday',
      'day1':'Monday',
      'day2':'Tueday',
      'day3':'Wendsday',
      'day4':'Thursday',
      'day5':'Friday',
      'day6':'Saturday',
      'day7':'Sunday'}
print(days['day0'])
#INCORRECT MEANS OF POPPING A METHOD BECAUSE IT ALREADY KNOWS YOU ARE LOOKING AT A KEY VALUE OF DAYS
#days.pop(['day0'])
#days.pop('day0')
print(days.keys())
print(days.items())
print(days.values())

def complete(abbreviation):
    #retunrs day of the week corresponding to the abbreviation
    days={'Mo':'Monday',
          'Tu':'Tuesday',
          'We':'Wednesday',
          'Th':'Thursday',
          'Fri':'Friday',
          'Sat':'Saturday',
          'Sun':'Sunday'}
    return days[abbreviation]

print(complete('Mo'))

def frequency(itemList):
    #returns frequency of items in itemList
    counters={}

    for item in itemList:
        if item in counters:
            counters[item]+=1
        else:
            counters[item]=1
    return counters
sum=frequency([5,5,3,1,4,2,4])
print(sum)