
# numbers=[10,25,30,40,1,2] #original list
# print("original list")
# for number in numbers:
#     print(number,end=" ")

# num_less_30=list(filter(lambda x: x<30, numbers))
# print("\n\nthis is updated list of number less than 30:")
# for number in num_less_30:
#     print(number,end=" ")

stud_marks={ 
    "man":33,
    "zam":44,
    "epoi":55,
    "aced":66,
    "edi":77,
    }

print("The list of the students and their marks:")
#print(stud_marks.items())
for stud_name,mark in stud_marks.items():
    print(f"student name: {stud_name} => Marks: {mark}")
    

#print(stud_marks)
print("\nstudent(s) who passed(marks >=40): ")
stud_pass=dict(filter(lambda mark: mark[1]>=40, stud_marks.items()))
for stud_name,mark in stud_pass.items():
    print(f"student name: {id} => Marks: {mark}")

print("\nstudent(s) who did not passed(marks<40): ")
stud_xpass=dict(filter(lambda mark: mark[1]<40, stud_marks.items()))
for stud_name,mark in stud_xpass.items():
    print("student name: ",stud_name, "=> Marks: ",mark)

sort_pass_stud=dict(sorted(stud_pass.items(), key=lambda x: x[1]))
print("\nPassed students in ascending order")
for stud_pass,mark in sort_pass_stud.items():
    print("student name: {} => marks: {}".format(stud_pass, mark))

sort_pass_stud_desc=dict(sorted(sort_pass_stud.items(), key=lambda x: x[1],reverse=True))
print("\nPassed students in descending order")
for stud_pass,mark in sort_pass_stud_desc.items():
    print(f"student name: {stud_pass} => marks: {mark}")

    


# print(stud_pass)