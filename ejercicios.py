cantidad = float(input("cantidad a invertir: "))
intereses = float(input("intereses porcentaje anuel: "))
años = float(input("años: "))
print("capital final:" + str(round(cantidad * (intereses/100+1) ** años, 2)))