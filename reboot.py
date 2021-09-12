#!/usr/bin/python3
import os
devices = os.popen('chia plots show').readlines()
USB = []
Chia = []
print("Script wird gestartet")
for line in os.listdir("/usb"):
 USB.append("/usb/" + line)
for line in devices:
 if "/" in line:
  Chia.append(line.replace("\n",""))
# hinzufuegen
for line in USB:
 if line not in Chia:
  print("chia plots remove -d " + line)
  os.system("chia plots add -d " + line)
# entfernen
for line in Chia:
 if line not in USB and "txt" not in line:
  print("chia plots remove -d " + line)
  os.system("chia plots remove -d " + line)
print("Script beendet")
