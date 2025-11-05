'''
For using the RegEx in python we must import
the re module in python.
'''
import re

print("--- Find All Bangladeshi Mobile Number From The Given Text ---")
print("---------------------------------------------")
text=input("\nGive The Text Here:")

#Giving pattern to search
mobile_num_pattern = r"(?:\+?88)?01[3-9]\d{8}"
mobile_num=re.findall(mobile_num_pattern,text)

'''
re.findall(pattern,text) will return a list
containing the string that matches the given 
pattern in the function.
'''
print("\nAll Mobile Numbers From The Text Are:")

i=1

for num in mobile_num:
    print(f"{i}:",num,end="\n")
    i+=1


    
