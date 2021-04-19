# Verificção de empréstimo

# casa = float(input('Qual o preço da casa? R$ '))
# sálario = float(input('Qual o valor do seu sálario? R$ '))
# anos = int(input('Quantos anos de financiamento?'))
# prestação = casa / (anos * 12)
# mínimo = sálario * 30 / 100
# print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end = '')
# print(' a pretação será de R${:.2f}'.format(prestação))
# if prestação <= mínimo:
#   print('Empréstimo pode ser concedido!')
# else:
#   print('Empréstimo negado!')

# Conversor de bases numéricas

# num = int(input('digite um número inteiro: '))
# print('''Escolha uma das bases para conversão:
# [ 1 ] converter para binário
# [ 2 ] converter para octal
# [ 3 ] converter para hexadecimal
# ''')

# opção = int(input('sua opção:'))

# if opção == 1:
#   print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
# elif opção == 2:
#   print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
# elif opção == 3:
#   print('{} convertido para hexadecial é igual a {}'.format(num, hex(num)[2:]))
# else:
#   print('opção inválida. Tente novamente.')

# Comparando números

# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo número: '))

# if num1 > num2:
#   print('O primeiro número é maior que o segundo')
# elif num2 > num1:
#   print('O segundo número é maior que o primeiro')
# else:
#   print('Os números são iguais')

# Alistamento

# from datetime import date

# atual = date.today().year 
# nasc = int(input('Ano de nascimento: '))
# idade = atual - nasc
# print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
# if idade == 18:
#   print('Você deve se alistar imediatamente')
# elif idade < 18:
#   anos = 18 - idade
#   previsão = anos + atual
#   print('Você ainda não pode se alistar.')
#   print('Ainda faltam {} anos para o seu alistamento'.format(anos))
#   print('Seu alistamento será em {}'.format(previsão))
# else:
#   anos = idade - 18
#   atraso = atual - anos
#   print('Você já deveria ter se alisado.')
#   print('Seu alistamento deveria ter sido feito em {}'.format(atraso))
#   print('Você está atrasado {} anos.'.format(anos))

# IMC

peso = int(input('Qual o seu peso? (kg)'))
altura = float(input('Qual sua altura? (m)'))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
  print('Você está abaixo do peso ideal')
elif 18.5 <= imc < 25:
  print('Você está no peso ideal')
elif 25 <= imc < 30:
  print('Você está com sobrebeso')
elif 30 <= imc < 40:
  print('Você está com obesidade')
elif 40 <= imc:
  print('Você está com obesidade mórbida. CUIDADO!')
