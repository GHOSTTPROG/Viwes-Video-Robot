import webbrowser
import time
import os
import threading

print("""
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████──██████─██████████████─██████████████─██████████████─██████████████─██████████████─████████████████───██████████████─██████████████─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██──██░░██─██░░██████░░██─██░░██████████─██████░░██████─██░░██████████─██░░██████░░██─██░░████████░░██───██░░██████░░██─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██─────────────██░░██─────██░░██─────────██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─██░░██─────────
─██░░██─────────██░░██████░░██─██░░██──██░░██─██░░██████████─────██░░██─────██░░██████████─██░░██████░░██─██░░████████░░██───██░░██──██░░██─██░░██─────────
─██░░██──██████─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░██──██░░██─██░░██──██████─
─██░░██──██░░██─██░░██████░░██─██░░██──██░░██─██████████░░██─────██░░██─────██░░██████████─██░░██████████─██░░██████░░████───██░░██──██░░██─██░░██──██░░██─
─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────────██░░██─────██░░██─────██░░██─────────██░░██─────────██░░██──██░░██─────██░░██──██░░██─██░░██──██░░██─
─██░░██████░░██─██░░██──██░░██─██░░██████░░██─██████████░░██─────██░░██─────██░░██████████─██░░██─────────██░░██──██░░██████─██░░██████░░██─██░░██████░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──██████─██████████████─██████████████─────██████─────██████████████─██████─────────██████──██████████─██████████████─██████████████─
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
# https://www.aparat.com/v/VCmAn

print()

url = input("Enter The Url Video : ")
print()
refresh_time = 60

def openurl():
    print("success viewed")
    webbrowser.open(url)
    time.sleep(refresh_time)

for i in range(100):
    t1 = threading.Thread(target=openurl)
    t2 = threading.Thread(target=openurl)
    t3 = threading.Thread(target=openurl)
    t4 = threading.Thread(target=openurl)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    os.system("taskkill /F /IM firefox.exe /T")
