a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
    print('o maior valor digitado foi: {}'.format(maior))