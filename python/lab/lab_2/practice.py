'''
def list_in(a, b):
...     return any(map(lambda x: b[x:x + len(a)] == a, range(len(b) - len(a) + 1)))
...
>>> a = [0, 0, 7]
>>> b = [1, 0, 0, 7, 3]
>>> c = [7, 0, 0, 0]
>>> list_in(a, b)
True
>>> list_in(a, c)
False '''

'''l1 = [10, 20, 30, 40, 50] 
l3 = [50, 75, 30, 20, 40, 69] 

res = [x for x in l1 + l3 if x not in l1 or x not in l3]

print(res)
if not res:
    print("Lists l1 and l3 are equal")
else:
    print("Lists l1 and l3 are not equal")'''

def list123(nums):

    for items in range(0,len(nums)-1):

        if nums[items]==1:

            if nums[items+1]==2:

                if nums[items+2]==3:

                    return True

       

    return False

result=list123([1,1,2,1,2,3])
print(result)

    
 
