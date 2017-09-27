my_list = ['pc', 'clothes', 'food']

#for items in my_list:
#    message = 'hello '
#    print message + items
#print 'done shopping'
#print 'xxxxxxx ' + message
#print my_list[2]

#for x in range (0,9):
#    print x

available_money = 300
running_total = 0
items_bought = []
money_spent =0
for item in my_list:
    if (item =="pc"):
        running_total = running_total + 240
    elif item =='clothes' :
        running_total = running_total + 50
    elif item == 'food':
        running_total = running_total + 20

    if (running_total > available_money):
        break
    else :
        items_bought.append(item)
        money_spent = running_total

print(items_bought)

print 'money left ' + str(available_money - money_spent)
