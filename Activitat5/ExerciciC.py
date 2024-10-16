import pandas as pd

IDs = [3,13,34,56,70,85,110,120,210,400]
DataFrame = pd.read_csv("mobiles.csv",usecols=["id","clock_speed","px_height","px_width","battery_power"])

def getClockSpeed():
    dataClockSpeed = DataFrame[DataFrame['id'].isin(IDs)][['id', 'clock_speed']]
    return dataClockSpeed

def getMegapixels():
    dataMegapixels = DataFrame[DataFrame['id'].isin(IDs)][['id','px_height','px_width']]
    #Creem la columna calculMegapixels per a guardar el pixelheightxpixelwidth
    dataMegapixels['calculMegapixels']= dataMegapixels['px_height']*dataMegapixels['px_width']
    return dataMegapixels

def getBatteryPower():
    dataBatteryPower = DataFrame[DataFrame['id'].isin(IDs)][['id','battery_power']]
    return dataBatteryPower
