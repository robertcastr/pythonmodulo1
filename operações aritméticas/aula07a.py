n1 = int(input('um valor:'))
n2 = int(input('Outro valor valor'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
sub = n1-n2
print('A soma é {}, \n o produto é {} \n  e a divisão é {:.2f} \n'.format(s, m, d), end=' ')
print('Subtração é {},\n potência é {} \n e divisão inteira é {}'.format(sub , e , di))
