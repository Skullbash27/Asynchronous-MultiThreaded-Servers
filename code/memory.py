import psutil#Acivates functions to give system information
import time

while True:
    mem=psutil.virtual_memory()#Gives memory related information of the system
    print(mem)
    time.sleep(1)
