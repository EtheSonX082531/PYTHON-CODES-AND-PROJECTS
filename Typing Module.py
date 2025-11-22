from typing import TypedDict
from typing import Union
from typing import Optional 
from typing import Any

class Movie(TypedDict):
    name:str
    year:int
    
movie=Movie(name="Avenger",year=2017)


def square(x:Union[int,float])->float:
    return x*x
    


def nice_massage(name:Optional[str])->None:
    if name is None:
        print("Hey Random Guy!")    
    else:
        print(f"Hey {name}")
        
        
def print_any(x:Any):
    print(x)      
    
print_any("This function can take any datatype and print them!")    
      
