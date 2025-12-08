# read  - "r"
# append - "a"
# write - "w"
#readbinary - "rb"
#writebinary - "wb"

"""
file = open("example.txt", "w")   
file.write("how are you collinstonesssssss")
file.close()   
"""

'''
file = open("example.txt", "r")
print(file.read())
'''

'''
file = open("example.txt", "a")   
file.write("\n" "you look nice")
file.close() 
'''

'''
#automatically closes the file — even if errors happen.
with open("example.txt", "w") as file:
    file.write("Hello odera")
'''

'''
file1 = open("example.txt, "r")

file2 = open("abc.txt", "w")

for data in file1:
    file2.write(data)
'''

'''
file1 = open("image.png","rb")

file2 = open("image.png","wb")

for data in file1:
    file2.write(data)
'''

'''
#counting the number of line in a file 
count = 0
with open("example.txt" "r") as file:
    for line in file:
        count = count + 1
print("Number of lines in the file: ",count)
'''

'''
#counting the number of characters in a file 
count = 0
with open("example.txt" "r") as file:
    content = file.read()
    for character in file:
        count = count + 1
print("Number of characters in the file:",count)
'''