import matplotlib.pyplot as plt
from ExerciciC import *

#Creem els dataFrames corresponents utilitzant les funcions de l'exercici C
clockSpeed = getClockSpeed()
megaPixels = getMegapixels()
batteryPower = getBatteryPower()

#Creem la finestra de 15x10
plt.figure(figsize=(15, 10))

#Primer grafic
plt.subplot(2, 2, 1)  # 1 row, 2 columns, 1st position
plt.bar(clockSpeed['id'], clockSpeed['clock_speed'], color='skyblue')
plt.title('Clockspeed per dispositiu')
plt.xlabel('ID')
plt.ylabel('Clockspeed en Gigaherz')
#Segon grafic
plt.subplot(2, 2, 2)  # 1 row, 2 columns, 1st position
plt.bar(megaPixels['id'], megaPixels['calculMegapixels'],color='yellow')
plt.title('Megapixels per dispositiu')
plt.xlabel('ID')
plt.ylabel('Megapixels en millons')
#Tercer grafic
plt.subplot(2, 2, 3)  # 1 row, 2 columns, 1st position
plt.bar(batteryPower['id'], batteryPower['battery_power'],color='green')
plt.title('Batterypower per dispositiu')
plt.xlabel('ID')
plt.ylabel('BatteryPower en Ampers per hora')
#Ho mostrem tot
plt.show()