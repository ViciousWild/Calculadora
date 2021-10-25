# def Define uma funcao
for comando in range(0, 2):
    pergunta = float(input('Escolha um numero: '))

parametro1 = pergunta
parametro2 = pergunta
msg_erro = 'Digite APENAS o que e pedido na tela para nao bugar.'

def calculadora(x, y): #def Nome da funcao(Parametros definidos)
    if operacao == 1:
        return x + y
    elif operacao == 2:
        return x - y2
    elif operacao == 3:
        return x * y
    elif operacao == 4:
        return x / y
    elif operacao >= 5:
        return print(msg_erro)
    elif operacao <= 0:
        return print(msg_erro)

operacao = int(input('''Escolha sua operacao:
[ 1 ] SOMA
[ 2 ] SUBTRACAO
[ 3 ] DIVISAO
[ 4 ] MULTIPLICACAO
Sua Escolha: '''))

if calculadora(parametro1 , parametro2) != None:
    print('Seu resultado e igual a: ', calculadora(parametro1, parametro2))
if calculadora(parametro1 , parametro2) == None:
    print('Voce gosta de crashar as coisas, ne?')

