import network
import time
# import datetime()
import urequests

print("Connecting to WiFi", end="")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST', '')
while not wifi.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")
print("conneted to the wifi")

currenTIme = time.ticks_ms()
counter = 0 
# while True:
  print(currenTIme)
  time.sleep(5)
  counter +=1
  print(counter)
  if(counter ==5):
    res = urequests.get("https://api.callmebot.com/whatsapp.php?phone=2347032687797&text=This+is+a+work&apikey=4217140")
    if res.status_code == 200:
      print("success")
    else:
      print("error")
    print(res.text)
    counter = 0
  
  
