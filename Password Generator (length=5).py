import random

key=True
while (key):
    val=int(input("Enter 1 to generate Password or 0 to Exit:"))
    if(val==1):
        str1="1234567890"
        str2="abcdefghijklmnopqrstuvwxyz"
        str3="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str4="<>(){}[]"
        str5="@#%&*!-+=/\?$%="
        index=[0,1,2,3,4]
        list=[str1,str2,str3,str4,str5]
        password=""
        for i in range(1,6):
        	random_num=random.choice(index)
        	password=password + random.choice(list[random_num])
        	index.remove(random_num)
        print("----------------------------")    
        print(f"Generated Passward is: {password}")  
        print("----------------------------")  
    elif(val>1):
        print("Invalid Operation!")  
    else:
        print("Thank You!")    
        key=False
          
    
    
