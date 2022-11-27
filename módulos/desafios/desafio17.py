import math

#cat1 = float(input('Digite o valor do cateto 1'))
#cat2 = float(input('Digite o valor do cateto 2'))
#h1 = math.hypot(cat1,cat2)
#print('A hipotenusa vai medir {:.2f}'.format(h1))
cat1 = float(input('Digite o valor do cateto 1'))
cat2 = float(input('Digite o valor do cateto 2'))
hipcat1 = math.pow(cat1,2)
hipcat2 = math.pow(cat2,2)
res = hipcat1+hipcat2
hipotenusa = math.sqrt(res)
print(hipotenusa)