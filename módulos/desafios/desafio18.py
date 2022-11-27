import math

angulo = float(input('Digite o angulo que deseja'))
seno = math.sin(math.radians(angulo))
print ('O angulo {} tem o seno de {:.2f}'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print ('O angulo {} tem o cossenlo de {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo {} tem a tangente de {:.2f}'.format(angulo,tangente))
