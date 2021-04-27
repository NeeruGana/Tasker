import os
import time
import ctypes
import asyncio
from winrt.windows.devices import radios
import pywhatkit
import webbrowser

#m=int(input())


#def type_of_commands():
 #   if m==1:
  #      print("original commands")
   # elif m==2:
    #    print("Special Commands")
    #else:
     #   print("Wrong Input")

async def bluetooth_power(turn_on):
    all_radios = await radios.Radio.get_radios_async()
    for this_radio in all_radios:
        if this_radio.kind == radios.RadioKind.BLUETOOTH:
            if turn_on:
                result = await this_radio.set_state_async(radios.RadioState.ON)
            else:
                result = await this_radio.set_state_async(radios.RadioState.OFF)


def command_instructions():
    print("1. Open Firefox")
    print("2. Close Firefox")
    print("3. Disconnect Wi-Fi")
    print("4. Connect Wi-Fi")
    print("5. ShutDown The System")  #should add sheduler
    print("6. Restart The System")    #Should add sheduler
    print("7. Change WallPaper")     #Under Construction
    print("8. Open Calculator")
    print("9. Send Message Through Whats App") #WA Web Should be On
    print("10. Turn On Bluetooth")
    print("11. Turn Off Bluetooth")
    print("12. Open Youtube Now")
    print("13. Watch Netflix")
    print("14. Shedule the time to open firefox/youtube/facebook ")
command_instructions()

n=int(input("Enter An Option From Above: "))


def commands():

    if n==1:
        #ff_location=os.system("where /r C:\ firefox.exe")
       # ff_loc=ff_location.replace("\\","/")
        #print(ff_location)
        #os.system("start "+ ff_location )
        #hff="firefox.exe"
        #os.startfile()
        os.system("start firefox")
        print("Command Executed")
    elif n==2:
        os.system("TASKKILL /F /IM firefox.exe")
        time.sleep(10)
        print("command Executed")

    elif n==3:
        def disable():
            os.system("netsh wlan"+" disconnect")
        disable()
    elif n==4:
        os.system('netsh wlan connect name="honor MediaPad T3 10"' )

    elif n==5:
        os.system("shutdown /s")
    elif n==6:
        os.system("shutdown /r")
    elif n==7:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "absolute path" , 0)
    elif n==8:
        os.system("calc")
    elif n==9:
        phone_num=input()
        msg=input("Enter Your Message")
        time_hour=int(input("Enter Time(24 hour format): "))
        time_min=int(input("Enter Min: "))
        pywhatkit.sendwhatmsg('+91'+phone_num,msg,time_hour,time_min)

    elif n==10:
        asyncio.run(bluetooth_power(True))
        print("Your Bluetooth is on")

    elif n==11:
        asyncio.run(bluetooth_power(False))
        print("Your Bluetooth is Off")
    elif n==12:
        webbrowser.open('https://www.youtube.com/')

    elif n==13:
        k=int(input("1.Open From Browser\n2.Open From Installer Exe(You should have already installed Netflix\nElse download it from MS Store)"))
        if k==1:
            webbrowser.open('https://www.netflix.com/in/')
        elif k==2:
            os.system("start netflix:")



            print("Enter Time")
 #          #time1=input()
#            p=""'C:/Program Files/Mozilla Firefox/firefox.exe'""




    elif n==14:
        def find(name, path):
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)

        found = find("firefox.exe", "C:\\")
        txt = found.replace("\\", "\\\\")
        print(txt)

        #j = "ONCE"
        m = input("name(Any random name): ")
        n1 = input("time(At which time to open): ")
        j = int(input("1.Once\n2.Daily\n(1)or(2)"))
        if j == 1:
            j1 = "ONCE"
        elif j == 2:
            j2 = "DAILY"
        k =int(input("1.Youtube\n2.Facebook\n(1)or(2)"))
        if k==1:
            o1="https://youtube.com"
            o = "\"\'" + txt + "\'" + o1 + "\""
            os.system("SCHTASKS /CREATE /SC " + j1 + " /TN " + m + " /TR " + o + " /ST " + n1)
        elif k==2:
            o2="https://facebook.com"
            o = "\"\'" + txt + "\'"+o2+"\""
        # os.system("cmd /K "+str(find_files.kali))
            os.system("SCHTASKS /CREATE /SC " + j1 + " /TN " + m + " /TR " + o + " /ST " + n1)



commands()