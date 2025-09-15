#  All about Python String

name = "anik Roy"
name_slice = name[1:7]
print("Sliced String:",name_slice)
print("Length of String:",len(name))

# skip character in string after particular jump
string1="123456789"
skip_string=string1[1:9:3]
print(skip_string)
print(string1.endswith("789"))
print(string1.startswith("ani"))
print(name.capitalize())

# make upper and lower
print(name.upper())
print(name.lower())

# capitalize each word in string
print(name.title())

# searching and finding 
string2='''Hello Anik How are you bondhu Anik?'''
print(string2.find("Anik"))
print(string2.find("anik")) # case sensitive 
print(string2.count("Anik")) # find occurrences of sub string 
print("How" in string2) # check sub string available or not

# all functions that ar mostly used 
# https://chatgpt.com/share/68c83651-0690-8006-a8e4-5fdc337a4274
