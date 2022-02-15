import array as arr
a = arr.array('i', [1 , 2 , 3])

print("The new created array is:", end=" ")
for i in range(0,3):
    print(a[i],end=" ")

a=arr.array('i',[1,2,3])
print("before insertion:",end=" ")
for i in range(0,3):
    print(a[i],end=" ")


#a=arr.array('i',[1,2,3])
print("after insertion:",end=" ")
a.insert(1,4)
for i in range(0,4):
    print(a[i],end=" ")


a=arr.array('i',[2,4,7,6])
print("before pop:",end=" ")
for i in range(0,4):
    print(a[i],end=" ")

print("after pop:", end=" ")
a.pop(1)
for i in range(0, 3):
print(a[i], end=" ")


a=arr.array('i',[3,1,6,3,9])
print("before removing:",end=" ")
for i in range(0,5):
    print(a[i],end=" ")

print("\n")
print("after removing:",end=" ")
a.remove(3)
a.remove(3)
for i in range(0,3):
    print(a[i],end=" ")
#

a=arr.array('i',[1,2,3])
print("before append:",end=" ")
for i in range(0,3):
    print(a[i],end=" ")

print("\n")
print("after append:",end=" ")
a.append(4)
for i in range(0,4):
    print(a[i],end=" ")



# list=['d','j','k','s']
# list.append('v')
# print(list)







