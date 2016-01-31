'''
THE SUM CANT BE ANYWHERE ELSE IN THE FUNCTION OR ELSE IT WOULD BE AN ERROR
'''
global_list=[1,2,3]
def find_sum(l):
    sum=0
    for i in l:
        sum=sum+i
    #REMEMER THAT YOU HAVE TO CALL str(sum) PYTHON DOES NOT ALLOW FOR + OF STRING AND INT
    print('The sum is: '+str(sum))



find_sum(global_list)

#PYTHON ALSO HAS A BUILT_IN FUNCTION THAT DOES THE SAME THING
num_list=[1,2,3,4]
total=sum(num_list)
print(total)

#SIMILAR AS THE find_sum method but for products
def find_product(l):
    #FOR PRODUCTS WE HAD TO USE THE IDENTITY PRODUCT OF MULTIPLICATION
    #THEREFORE PRODUCTS INITIAL VALUE IS ONE RATHER THAN ZERO
    product=1
    for i in l:
        product=product*i
# MUST USE str(product) BECAUSE PYTHON DOES NOT UNDERSTAND STRING + AN INT.
    #PYTHON ONLY UNDERSTANDS STRING+STRING
    #THEREFORE CONVERT THE INT_PRODUCT TO A STRING
    print('the product is: '+str(product))

find_product(global_list)