d1 = {'simple_key':'hello'} 
d2 = {'k1':{'k2':'hello'}} 
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}


print(d1['simple_key']) 
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])



'''

new_value= list(d3.items())
print(new_value)
print(new_value[0])
print(new_value[0][1][0])


my_dict = {} 
my_dict['l'] = 4
my_dict['m'] = 6
my_dict['n'] = 9
new_value = list(my_dict.items())
print(new_value)
print(new_value[2])
'''

