
print("\nwe are going to discuss about tuple here")
prog_lang=("python","c","c++","java","php","SQL","HTML","CSS")
print("\nthe number of programming languages are: ",len(prog_lang))
print("\nall listed programming languages are:")
for prog_lang_list in prog_lang:
    print(prog_lang_list)

search_lang_index=int(input("enter index number to know the programming language: "))
# Semak indeks sah (boleh guna indeks negatif juga) kod diubah oleh chatgpt bermula dari sini
if -len(prog_lang) <= search_lang_index < len(prog_lang):
    print(f"The index {search_lang_index} contains '{prog_lang[search_lang_index]}'")
else:
    print("Index number not valid")
#kod diubah oleh chatgpt sampai sini
"""
if search_lang_index in prog_lang:
        print(f"The index {search_lang_index} contains {prog_lang.index(search_lang_index)}")
else:
        print(f"index number not valid")
"""


"""
numbers=(1,2,4,10,2,3,2,3,5,50,1)
print("all numbers in tuple: ",len(numbers))
for num in numbers:
    print(num)
search_num=int(input("\nenter number to find out frequency:\t"))
if search_num in numbers:
    print(f"number: {search_num} occurs: {numbers.count(search_num)} times")
else:
    print(f"no such number {search_num} in our tuple")

"""

"""
#sum of 4 numbers in a list
numbers=[6,8,9,2]
print("the list of the number is:")
for each_num in numbers:
 print(each_num)
total=sum(numbers)
print("sum of the numbers : ",total)
"""