#colocando em uppar,lower,mostrando quantas letras tem até o primeiro espaço e quantas letras tem tirando os espaços

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome.....')
print(nome.upper())
print(nome.lower())
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))

