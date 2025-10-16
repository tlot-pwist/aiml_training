import os

file_path=r'C:\Users\DELL\Coding\AIML\Day-8\new_folder'
# day8file_path='C:\\Users\DELL\\Coding\AIML\\Day-8\\new_folder'
# file_path=os.getcwd()

# try:
#     file_name=input('enter new file name: ')
# except Exception:
#     full_path=os.path.join(file_path,file_name)
#     file=open(file_path,'w')
# content=input('enter text to write in file:\n')
# file.write(content)
# file.close()

"""create new file and write inside the file"""
# file_name=input('enter new file name: ')
# full_path=os.path.join(file_path,file_name)
# file=open(full_path,'w')
# content=input('enter text to write in file:\n')
# file.write(content)
# print(f'File {file_name} created at {full_path} and content saved in file')
# file.close()

"""check if the file name already existed"""
# file_name=input('enter file name to edit: ')
# full_path=os.path.join(file_path,file_name)

# if os.path.exists(full_path):
#     file=open(full_path,'a')
#     content=input('enter text to write in file:\n')
#     file.write(content)
#     print(f'File {file_name} updated')
#     # print(f'File {file_name} created at {full_path} and content saved in file')
#     file.close()
# else:
#     print(f'No such file {file_name} exists')

"""read content of a file"""
file_name=input('enter file name to read content: ')
full_path=os.path.join(file_path,file_name)

if os.path.exists(full_path):
    file=open(full_path,'r')
    #content=input('enter text to write in file:\n')
    content=file.read()
    print("file content:\n")
    print(f'{content}\n')
    # print(f'File {file_name} created at {full_path} and content saved in file')
    file.close()
else:
    print(f'No such file {file_name} exists')


