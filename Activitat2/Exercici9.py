paraula1 = str(input("Entra una paraula: "))
paraula2 = str(input("Entra una paraula: "))
ch1 = paraula1[0]
ch2 = paraula2[0]
paraula1=paraula1.replace(paraula1[0],ch2)
paraula2=paraula2.replace(paraula2[0],ch1)
print(paraula1,paraula2)