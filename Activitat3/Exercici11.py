divises = {
    "Euro":"€",
    "Dollar":"$",
    "Yen":"JPY",
    "Pesos":"MXN",
    "Libras":"UKP",
    "Haiti":"HMT",
    "Thailand":"TLB",
    "PuertoRico":"PR$"
}
request = str(input("Consulta una divisa: "))

while request!='':
    if divises.__contains__(request):
        print(divises[request])
    else:
        print("La divisa que vols consultar no esta en el diccionari ")
    request = str(input("Consulta una divisa: "))