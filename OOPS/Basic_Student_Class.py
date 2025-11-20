class Student:
    school_name="Govt Agragami School And College"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def average(self):
        total_marks=0
        for mark in self.marks:
            total_marks+=mark
        avg=total_marks//3    
        print(f"Average Marks of {self.name} is:",avg)  
        

print(Student.school_name,"\n")
        
s1=Student("Smita Paramita",[90,85,100])
s1.average() 

s2=Student("Marian Chowdhury",[98,92,80])
s2.average()
