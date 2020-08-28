temps = [221,234,443,230]

new_temp = []
for temp in temps:
    if temp != 230:
        new_temp.append(temp/10)


print(new_temp)
    

#List comprehension
nt = [tem /10 for tem in temps if tem != 230] 
print(nt)


# return only integer values
a = ['a',1,2,'b',3]

def foo(lst):
    return [i for i in lst if isinstance(i,int)]

print(foo(a))


# return only positive integer values
b = [1,1,-2,-9,3]

def fooo(lst):
    return [ii for ii in lst if ii > 0]

print(fooo(b))



# return only positive integer values
c = [1,2,3,3,4,4,5,6,6,7,7,77,55,4,3]

def replace_a_num(l):
    return [a if a != 6 else 0 for a in l]


print(replace_a_num(c))


new_tempr = []
for temp in c:
    if temp != 6:
        new_tempr.append(temp)
    else:
        
        new_tempr.append(0)


print(new_tempr)
        
