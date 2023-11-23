import datetime
import os
import time
os.system("cls")
sec=0
min=0
hour=0
active=True
while active:
    os.system("cls")
    sec=sec+1
    if sec==60:
        min=min+1
        sec=sec-60
    
    if min==60:
        hour=hour+1
        min=min-60
    
    print(f"0{hour}:0{min}:{sec}")
    time.sleep(1)

origintime = time.time()

while active:
    os.system('cls')
    
    time_now = time.time() #tog hjälp av din kod

    timer = time_now - origintime

    timer_tuple = time.localtime(timer)

    timer_formatted = time.strftime("%M:%S", timer_tuple)

    print(timer_formatted)
    
    time.sleep(1)





while active:
    date = datetime.datetime.now()
    print(date.strftime("%x"))
    print(date.strftime("%X"))
    
    time.sleep(1)
    os.system("cls")
    