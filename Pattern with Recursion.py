def pattern(n):
    if(n==0):
        return
    for i in range(n):
        print("+ ",end="")
    print("\n")    
    pattern(n-1)


n=int(input("Enter a Number for Pattern Print:"))    
pattern(n)   
            
