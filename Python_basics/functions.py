# def print_my_name(fname,lname):
#     print(f'My First Name is : {fname}, lastname is {lname}')



# def print_color (color):
#     color='pink'
#     print(f'color is {color}')

# color='red'
# print(f'color is {color}')
# print_color ('blue')
# print(f'color is {color}')
# #print_my_name('Satish','vudaru')


# def getTotalCostofItem(cost):

#     return cost + getTaxforItem(cost)

# def getTaxforItem(cost):
#     return cost * .0825

# cost_of_item=30
# print(f'Total cost of item is : {getTotalCostofItem(30)}')


def getdict(firstname,lastname,age):
    my_dict= {'firstname':firstname,
              'lastname':lastname,
              'age':age}
    
    return my_dict

for x,y in getdict('satish','vudaru',27).items():
    print(f'Key is {x}, value is {y}')