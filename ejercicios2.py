inversion = float(input("ingrese la inversion inicial: "))
intereses = 0.04
balance1 = inversion * (1 + intereses)
print("balance del primer año: " + str(round(balance1, 2))) 
balance2 = balance1 * (1 + intereses)
print("balance del segundo año: " + str(round(balance2, 2)))
balance3 = balance2 * (1 + intereses)
print("balance del tercer año: " + str(round(balance3, 2)))