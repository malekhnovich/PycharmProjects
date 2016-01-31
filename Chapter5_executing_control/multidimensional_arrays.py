def print2D(t):
    #PRINTS VALUES IN 2D LIST AS 2D TABLE
    #CAN BE READ AS EACH ROW IN TABLE T
    for row in t:
        #EACH ITEM IN A SINGLE ROW
        for item in row:
            print(item, end='')#PRINTS THE ITEM FOLLOWED BY A BLANK SPACE
        print()#MOVES TO THE NEXT LINE
print2D([[1,2,3],[4,5,6]])

#METHOD THAT INCREMENTS EACH ELEMENT IN EACH ROW
def increment2D(t):
    #INCREMENTS EACH VALUE IN 2D LIST OF NUMBERS

    nrows=len(t) #NUMBER OF ROWS
    ncols=len(t[0]) #NUMBER OF COLUMNS

    for i in range(nrows):
        for j in range(ncols):
            t[i][j]+=1
    return t;
incremented=increment2D([[1,2,3],[7,8,9],[4,5,6]])
print(incremented)

def checkThis():
    #WHEN IT TAKES THREE PARAMETERS INTO THE RANGE
    #THE FIRST STATES WHAT NUMBER TO START AT
    #THE SECOND STATES WHAT NUMBER TO GO UP TO
    #THE THIRD STATES THAT YOU SHOULD ADD 24 TO EACH ELEMENT UNTIL YOU CAN NO LONGER STAY UNDER 400
    for i in range(1,400,24):
        print(i)

#checkThis()

def checkThat():
    multiple=0
    while multiple<6951:
        multiple=multiple+73
    print(multiple)

checkThat()