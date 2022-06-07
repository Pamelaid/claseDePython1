datos = []
datos.append(float (input("ingresar peso (kg): \n")))
#datos = [peso]
datos.append(float (input("ingresar altura (cm): \n"))/100)
datos.append(datos[0] / (datos[1] * datos[1]))
#print ("Tu indice de masa corporal es " + datos[2])
print ("indice es: " + "%.2f" % datos[2])
if (datos[2]<=18.5) :
    print ("Nivel de peso: Bajo peso")
if (datos[2]>18.5 and datos[2]<24.9) :
     print("Nivel de peso: Normal")
if (datos[2]>25.0 and datos[2]<29.9) :
     print("Nivel de peso: Sobre peso")
if (datos[2]>30.0) :
     print("Nivel de peso: Obesidad")