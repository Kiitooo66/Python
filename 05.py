letra = input('Digite uma Letra:  ')

vogais = 'aeiou'

if letra in vogais or letra in vogais.upper():
    print('uma vogal ')
else:
    print('Uma cosoante')
