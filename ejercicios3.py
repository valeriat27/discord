barras_de_pan = int(input("ingrese el numero de barras vendidad no frescas: "))
precio = 3.49
descuento = 0.6
costo = barras_de_pan * precio * (1 - descuento)
print("el costo de una barra de pan fresca es de: " + str(precio) + "€")
print("el descuento de una barra de pan no fresca es de: " + str(descuento * 100)+ "%")
print("el costo total a pagar es: " + str(round(costo, 2 ))+ "€")
