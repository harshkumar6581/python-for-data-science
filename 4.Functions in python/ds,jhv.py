def print_numbar(*harsh):
    for number in harsh:
        print(number )




print_numbar(1,2,3,4,5,6,7,7,8,"harsh")        


def print_numbar(*args):
    for number in args:
        print(number )

print_numbar(1,2,3,4,5,6,7,7,8,"harsh")  



## keyword arguments

def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")



print_details(name="harsh",age="55",country="india")
     

   