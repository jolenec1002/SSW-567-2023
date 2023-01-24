from datetime import datetime
def my_brand(name):
    print("=*=*=*= Jolene Ciccarone =*=*=*=")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*=")
    print("=*=*=*= " + name + " =*=*=*=")

    now = datetime.now()
    # dd/mm/YY H:M:S
    dt= now.strftime("%d/%m/%Y %H:%M:%S")
    print("=*=*=*= " + dt + " =*=*=*=")

my_brand("SSW 567 HW 00")
print("Hello World")
my_brand("SSW 567 HW 00")
    

     