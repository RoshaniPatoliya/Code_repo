'''
if 1 == 2:
    print('first')
elif 3 == 3:
    print('middel')
else:
    print('last')  '''

'''seq = [1,2,3,4,5]

for item in seq:
   # print(item)
   print('yes!') '''

'''ages = {"Bob": 3, "Frank": 4, "Maya": 5}  

for key in ages:
    print("This is the key")
    print(key)
    print("This is the value")
    print(ages[key])
    print('\n') '''

'''mypairs = [(1,10),(2,20),(3,30)]

#for item in mypairs:
    #print(item)

for item1,item2 in mypairs:
    print(item1)
    print(item2)'''

'''i = 1
while i < 5:
    print('i is: {}'.format(i))
    i= i+1  '''

'''for i in range(1,10,2):
    print(i)  '''

'''x= [1,2,3,4]
#out = []
#for item in x:
#    out.append(item*2)
#print(out) 

print([item*2 for item in x])'''

'''def evenCheck(num):
    print('I am checking if {} is even?'.format(num))
    print(num%2 == 0)

evenCheck(46) '''

'''def addEvenOnly(num1,num2):
    if((num1 % 2!= 0) or (num2 % 2!= 0)):
        return False
    else:
        return num1+num2

x= addEvenOnly(2,2)  
print(x)  '''

'''def returnTwo(num):
   # return num*2

lambda num:num*2'''

'''my_list = [1,2,3,4,5,6,7,8,9,10]

def evenBool(num):
    return num % 2 == 0

#evens = filter(evenBool,my_list)
#print(list(evens)) 

evens = filter(lambda num: num%2==0,my_list)
print(list(evens)) '''

'''tweet = "Go Brazil! #Soccer"
print(tweet.split('#')[1])'''

'''lst = [1,2,3]
x= lst.pop()
print(x)
print(lst)'''
    


