class Student:
    school_name="Govt Agragami School And College"
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    
    def average(self):
        avg=(self.marks1+self.marks2+self.marks3)//3
        print(f"Average Marks of {self.name} is:",avg)  
        

print(Student.school_name,"\n")
        
s1=Student("Smita Paramita",90,85,100)
s1.average() 

s2=Student("Marian Chowdhury",98,92,80)
s2.average()
