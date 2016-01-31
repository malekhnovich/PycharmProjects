def before0(table):
    #PRINTS VALUES IN 2D LIST OF NUMBERS T AS A 2D TABLE
    #ONLY VALUES IN ROW UP TO FIRST 0 ARE PRINTED
    for row in table:
        for num in row:
            if num==0:
                break
            print(num, end=' ')
        print()
before0([[2,3,0,6],[0,3,4,5],[4,5,6,0]])
print("---------------------")


def ignore0(table):
    '''PRINTS VALUES IN 2D LIST OF NUMBERS t as a 2D TABLE
    #IGNORES VALUES THAT ARE 0(ZERO)
        '''
    for row in table:
        for num in row:
            if num==0:
                continue
            print(num,end=' ')
        print()

ignore0([[2,3,0,6],[0,3,4,5],[4,5,6,0]])
