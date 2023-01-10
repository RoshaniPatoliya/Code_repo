def arrayCheck(arra):

    for items in range(0,len(arra)-1):
        if arra[items]==1:
            if arra[items+1]==2:
                if arra[items+2]==3:
                    return True

    return False

result=arrayCheck([1,1,2,1,2,3])
print(result)  

result=arrayCheck([1,2,4,5,6])
print(result)

result = arrayCheck([1,1,2,3,3,4,5])
print(result)




'''    
my_list = [0,1,2,3,4,5,6,7,8,9]
>>> my_num = (1, 2, 3)

>>> any(x== my_num for x in zip(my_list, my_list[1:], my_list[2:]))
True'''