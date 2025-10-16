
# print("sets in python")
# set_one = {'laptop', 'airphone', 'ipad', 'mobile'}
# print("number of items in set_one are: ",len(set_one))
# for item in set_one:
#          print(item)


#clear(): remove all the items from set

# set_one.clear()
# print("\nafter clear number of items in set_one are: ",len(set_one))
# for item in set_one:
#     print(item)

# set_one.remove('airphone')
# print("\nafter removing one item from set: ",len(set_one))
# for item in set_one:
#     print(item)



  #union, intersectiom, difference
set_one={100,200,300,500,700,900,150}
set_two={100,300,400,700,1000,1300}
set_three={3000,280,500,700}

####################################################################################
#union

#s1.union(s2): returns a new set with all items from both sets s1,s2.
# print(f"set one contains: {len(set_one)} items")
# print(set_one)
# print(f"set two contains : {len(set_two)} items")
# print(set_two)

# unionset=set_one.union(set_two)
# print(f"union of set_one and set_two contains {len(unionset)} following items:")
# print(unionset)

# unionset=set_one.union(set_two,set_three)
# print(f"\nunion of set_one, set_two and set_three contains {len(unionset)} following items:")
# print(unionset)

####################################################################################

#s1.intersection
# print(f"set one contains: {len(set_one)} items")
# print(set_one)

# print(f"\nset two contains : {len(set_two)} items")
# print(set_two)

# print(f"\nset two contains : {len(set_three)} items")
# print(set_three)

# new_set=set_one.intersection(set_two,set_three)
# print("\nthe intersection of set_one and set_two is: ")
# print(new_set)

####################################################################################

#s1.difference : returns element that is outside intersection
print(f"set one contains: {len(set_one)} items")
print(set_one)

print(f"\nset two contains : {len(set_two)} items")
print(set_two)

#print(f"\nset two contains : {len(set_three)} items")
#print(set_three)

new_set=set_one.difference(set_two)
print("\nthe difference of set_one and set_two is: ")
print(new_set)

####################################################################################

