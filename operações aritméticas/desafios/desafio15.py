dias = float(input("Quantos dias o carro percorreu?"))
km = float(input("Quantos km o carro percorreu? "))

pago = (dias*60)+(km*0.15)

print('O total a pagar é {:.2f}'.format(pago))