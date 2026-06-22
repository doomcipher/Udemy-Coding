# Aula 01 - Anotações e práticas de Python
#
# Este arquivo funciona como um caderno de estudos.
# A ideia é ir testando comandos, observando os resultados
# e deixando comentários para entender depois.
#
# Observação:
# - Comentários começam com #
# - O Python executa o código de cima para baixo
# - print() mostra informações na tela
# - input() recebe informações digitadas pelo usuário
# - variáveis guardam valores
# - funções guardam blocos de código reutilizáveis
# - bibliotecas trazem códigos prontos para facilitar nossa vida
#
# Importante:
# Este arquivo tem muitos exemplos diferentes.
# Algumas partes pedem input(), ou seja, vão parar e esperar você digitar algo.
# Algumas partes usam time.sleep(), ou seja, vão esperar alguns segundos.
#
# Como é um arquivo de estudo, isso é normal.


# 1. Primeiro comando: print()

# print() mostra algo na tela.
# O texto precisa ficar entre aspas.

print('Hello World')

# Também podemos imprimir números.
print(10)
print(20.5)

# Podemos imprimir mais de um valor separando por vírgula.
print('Hello', 'World')

# Podemos misturar texto e número no mesmo print.
print('Minha idade é', 18)


# 2. Usando sep no print()

# sep significa "separador".
# Ele define o que vai aparecer entre os valores separados por vírgula.
# Por padrão, o separador é um espaço.

print('Hello', 'World')              # Separador padrão: espaço
print('Hello', 'World', sep='-')     # Separador com traço
print('Hello', 'World', sep='[]')    # Separador com []
print('2026', '06', '21', sep='/')   # Simulando uma data
print('Python', 'é', 'bom', sep=' ') # Separador com espaço manual

# Outros exemplos úteis:

print('lain', 'gmail.com', sep='@')  # Simulando e-mail
print('192', '168', '0', '1', sep='.')  # Simulando IP
print('C:', 'Users', 'Lain', 'Downloads', sep='/')  # Simulando caminho


# 3. Usando end no print()

# end define o que acontece no final do print.
# Por padrão, todo print termina com uma quebra de linha.
# A quebra de linha é representada por \n.

print('Linha 1')
print('Linha 2')

# Aqui o segundo print continua na mesma linha.
print('Hello', end=' ')
print('World')

# Outros exemplos com end:
print('Hello', 'World', sep='-', end=' | ')
print('Próximo print na mesma linha')

print('A', end='')
print('B', end='')
print('C')

# Pulando uma linha manualmente.
print()


# 4. Strings e tipos de aspas

# String é texto.
# Pode ser escrita com aspas simples ou aspas duplas.

print('Luiz')
print("Luiz")

# Aspas triplas também funcionam.
# São úteis principalmente para textos grandes ou com várias linhas.

print('''Luiz''')
print("""Luiz""")

# Aspas dentro de aspas:
print('Luiz "Otávio"')
print("Luiz 'Otávio'")

# Quebra de linha dentro da string usando \n.
print('Primeira linha\nSegunda linha')

# Tabulação usando \t.
print('Nome:\tLuiz')
print('Idade:\t18')

# Barra invertida pode escapar caracteres.
print('Ele disse: \"Python é massa\"')
print('Caminho exemplo: C:\\Users\\Lain\\Downloads')


# 5. Tipos de dados com type()

# type() mostra o tipo de um valor.

print(type('Luiz'))    # str   -> texto/string
print(type(20))        # int   -> número inteiro
print(type(20.20))     # float -> número decimal
print(type(True))      # bool  -> verdadeiro ou falso
print(type(False))     # bool  -> verdadeiro ou falso

# Exemplos de valores booleanos:
print(True)
print(False)

# bool é muito usado em comparações e condições.
print(10 > 5)
print(10 < 5)


# 6. Variáveis

# Variável é um nome que guarda um valor.
# Em Python, não precisa colocar ; no final da linha.

nome = 'Luiz'
idade = 18
altura = 1.75
estudando_python = True

print(nome)
print(idade)
print(altura)
print(estudando_python)

# Também podemos usar variáveis dentro de prints.
print('Meu nome é', nome)
print('Minha idade é', idade)
print('Minha altura é', altura)

# Nomes de variáveis devem ser claros.
# Evite nomes como x, y, z quando o código for crescer.
# Use nomes como idade, senha_correta, numero_digitado, lista_de_compras.

canal = 'DoomCipher'
link_do_canal = 'https://www.youtube.com/@doomcipher'

print('Meu canal é:', canal)
print('Link do canal:', link_do_canal)


# 7. Operações matemáticas

primeiro_numero = 5
segundo_numero = 7

print(primeiro_numero + segundo_numero)   # Soma
print(primeiro_numero - segundo_numero)   # Subtração
print(primeiro_numero * segundo_numero)   # Multiplicação
print(primeiro_numero / segundo_numero)   # Divisão comum
print(primeiro_numero // segundo_numero)  # Divisão inteira
print(primeiro_numero % segundo_numero)   # Resto da divisão
print(primeiro_numero ** segundo_numero)  # Potência

# Exemplos extras:
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(2 ** 3)

# Ordem das operações:
resultado = 10 + 5 * 2
print(resultado)

# Usando parênteses para controlar a ordem:
resultado = (10 + 5) * 2
print(resultado)

# Utilidade do operador %:
# Ele é muito usado para saber se um número é par ou ímpar.
# Se o resto da divisão por 2 for 0, o número é par.

print(10 % 2)  # 0, então 10 é par
print(7 % 2)   # 1, então 7 é ímpar


# 8. Comparações

# Comparações retornam True ou False.

print(primeiro_numero > segundo_numero)    # Maior que
print(primeiro_numero < segundo_numero)    # Menor que
print(primeiro_numero >= segundo_numero)   # Maior ou igual
print(primeiro_numero <= segundo_numero)   # Menor ou igual
print(primeiro_numero == segundo_numero)   # Igual
print(primeiro_numero != segundo_numero)   # Diferente

# Exemplos extras:
print(10 == 10)
print(10 != 5)
print(8 > 3)
print(8 < 3)
print('a' == 'a')
print('a' == 'b')

# Atenção:
# = serve para atribuir valor.
# == serve para comparar valores.

idade = 18
print(idade == 18)


# 9. Input

# input() recebe uma informação digitada pelo usuário.
# Tudo que vem do input chega como string, ou seja, texto.

nome_digitado = input('Digite seu nome: ')
print('Você digitou:', nome_digitado)

idade_digitada = input('Digite sua idade: ')
print('Sua idade digitada foi:', idade_digitada)

# Mesmo digitando um número, o input retorna texto.
print(type(idade_digitada))


# 10. Convertendo input para número

# Para fazer contas com número digitado pelo usuário,
# precisamos converter o valor.

numero_digitado = input('Digite um número: ')
numero_digitado = int(numero_digitado)

print(numero_digitado + 10)

# Também dá para fazer direto assim:
outro_numero = int(input('Digite outro número: '))
print(outro_numero * 2)

# int() converte para número inteiro.
# float() converte para número decimal.

preco = float(input('Digite o preço do produto: '))
print('O dobro do preço é:', preco * 2)


# 11. If e else

# if significa "se".
# else significa "senão".
#
# O if executa um bloco se a condição for verdadeira.
# O else executa outro bloco se a condição do if for falsa.

senha_correta = 'receba123'
senha_digitada = input('Digite sua senha: ')

if senha_digitada == senha_correta:
    print('Senha correta!')
else:
    print('Senha incorreta!')


# 12. If, elif e else

# elif significa "senão se".
# Serve para testar mais de uma condição.

nota = float(input('Digite sua nota: '))

if nota >= 9:
    print('Excelente')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperação')
else:
    print('Reprovado')

# Utilidade:
# if, elif e else são usados em decisões.
#
# Exemplos:
# - sistema de login
# - verificação de idade
# - cálculo de desconto
# - classificação de notas
# - liberar ou negar acesso


# 13. Listas

# Lista é uma coleção de valores.
# Listas usam colchetes [].
# Os itens da lista são acessados por índice.
# O primeiro índice é 0.

frutas = ['banana', 'maçã', 'uva']

print(frutas)

# Acessando itens da lista:
print(frutas[0])  # banana
print(frutas[1])  # maçã
print(frutas[2])  # uva

# Índice negativo acessa de trás para frente:
print(frutas[-1])  # último item
print(frutas[-2])  # penúltimo item


# 14. Alterando itens da lista

frutas[0] = 'laranja'
print(frutas)

frutas[2] = 'melancia'
print(frutas)


# 15. Cuidado com lista dentro de lista

# Isto é uma string:
texto = 'ixi'

# Isto é uma lista:
lista = ['ixi']

print(texto)
print(lista)

# Exemplo de lista normal:
frutas = ['maçã', 'ixi', 'banana']
print(frutas)

# Exemplo de lista dentro de lista:
frutas = ['maçã', ['ixi'], 'banana']
print(frutas)

# Na lista acima, ['ixi'] é uma lista dentro da lista principal.
# Por isso, 'ixi' e ['ixi'] não são a mesma coisa.

print(frutas[1])     # ['ixi']
print(frutas[1][0])  # ixi

# Explicação:
# frutas[1] pega a lista ['ixi'].
# frutas[1][0] pega o primeiro item da lista interna, ou seja, 'ixi'.


# 16. Fatiamento de listas

frutas = ['banana', 'maçã', 'uva', 'laranja', 'abacaxi']

print(frutas[0:2])   # Pega do índice 0 até antes do índice 2
print(frutas[1:4])   # Pega do índice 1 até antes do índice 4
print(frutas[:3])    # Pega do começo até antes do índice 3
print(frutas[2:])    # Pega do índice 2 até o final
print(frutas[:])     # Copia a lista inteira

# Alterando uma parte da lista:
frutas[0:2] = ['morango', 'kiwi']
print(frutas)

# Exemplo parecido com uma tentativa sua:
frutas = ['banana', 'maçã', 'uva']
frutas[0:1] = ['oier', 'laelezinho']
print(frutas)

# Antes:
# ['banana', 'maçã', 'uva']
#
# Depois:
# ['oier', 'laelezinho', 'maçã', 'uva']
#
# Isso acontece porque frutas[0:1] substitui a fatia da posição 0
# por dois novos itens.


# 17. append()

# append() adiciona UM item no final da lista.

frutas = ['banana', 'maçã', 'uva']

frutas.append('laranja')
print(frutas)

frutas.append('abacaxi')
print(frutas)

# Cuidado:
# Se colocar uma lista dentro do append,
# ele adiciona a lista inteira como um único item.

frutas.append(['melancia', 'kiwi'])
print(frutas)

# Resultado parecido com:
# ['banana', 'maçã', 'uva', 'laranja', 'abacaxi', ['melancia', 'kiwi']]


# 18. extend()

# extend() adiciona vários itens de uma vez.
# Ele pega cada item da lista passada e adiciona separadamente.

frutas = ['banana', 'maçã', 'uva']

frutas.extend(['laranja', 'abacaxi', 'melancia'])
print(frutas)

# Diferença entre append e extend:

lista_append = ['a', 'b']
lista_append.append(['c', 'd'])
print(lista_append)

lista_extend = ['a', 'b']
lista_extend.extend(['c', 'd'])
print(lista_extend)

# append adiciona a lista inteira como um item.
# extend espalha os itens dentro da lista original.


# 19. insert()

# insert() adiciona um item em uma posição específica.
# O primeiro valor é o índice.
# O segundo valor é o item.

frutas = ['banana', 'maçã', 'uva']

frutas.insert(1, 'laranja')
print(frutas)

frutas.insert(0, 'morango')
print(frutas)

frutas.insert(3, 'kiwi')
print(frutas)


# 20. remove()

# remove() remove um item pelo valor.
# Ele remove a primeira ocorrência encontrada.

frutas = ['banana', 'maçã', 'uva', 'maçã']

frutas.remove('maçã')
print(frutas)

# Cuidado:
# Se tentar remover um item que não existe, dá erro.
#
# frutas.remove('abacaxi')
#
# Erro:
# ValueError: list.remove(x): x not in list

# Para evitar erro, podemos verificar antes:

if 'abacaxi' in frutas:
    frutas.remove('abacaxi')
else:
    print('abacaxi não está na lista')


# 21. pop()

# pop() remove um item pelo índice.
# Se não passar índice, ele remove o último item.
# O pop também devolve o item removido.

frutas = ['banana', 'maçã', 'uva', 'laranja']

fruta_removida = frutas.pop()
print(fruta_removida)
print(frutas)

fruta_removida = frutas.pop(1)
print(fruta_removida)
print(frutas)


# 22. del

# del também pode remover um item pelo índice.

frutas = ['banana', 'maçã', 'uva']

del frutas[1]
print(frutas)

# Também pode apagar uma fatia da lista:
frutas = ['banana', 'maçã', 'uva', 'laranja', 'abacaxi']

del frutas[1:3]
print(frutas)


# 23. len()

# len() mostra a quantidade de itens.

frutas = ['banana', 'maçã', 'uva']

print(len(frutas))

# len() também funciona em strings.
print(len('Python'))


# 24. in e not in

# in verifica se algo está dentro de uma lista.
# not in verifica se algo não está dentro.

frutas = ['banana', 'maçã', 'uva']

print('banana' in frutas)
print('laranja' in frutas)
print('laranja' not in frutas)

if 'banana' in frutas:
    print('Tem banana na lista')

if 'laranja' not in frutas:
    print('Não tem laranja na lista')


# 25. clear()

# clear() limpa todos os itens da lista.

frutas = ['banana', 'maçã', 'uva']

frutas.clear()
print(frutas)


# 26. Tuplas

# Tupla é parecida com lista, mas usa parênteses ().
# A principal diferença é:
# - Lista pode ser alterada
# - Tupla não pode ser alterada depois de criada

minha_tupla = ('banana', 'leite')

print(minha_tupla)
print(type(minha_tupla))

# Acessando itens da tupla:
print(minha_tupla[0])
print(minha_tupla[1])

# Isso daria erro, porque tupla não pode ser alterada:
# minha_tupla[0] = 'maçã'

# Utilidade de tupla:
# Use quando você quer guardar dados que não deveriam mudar.
#
# Exemplo:
coordenada = (10, 20)
print(coordenada)


# 27. Tupla com apenas um item

# Isto NÃO é uma tupla.
# É apenas uma string entre parênteses.

nao_e_tupla = ('casaco')
print(nao_e_tupla)
print(type(nao_e_tupla))

# Para criar uma tupla com apenas um item,
# precisa colocar vírgula.

tupla_de_um_item = ('casaco',)
print(tupla_de_um_item)
print(type(tupla_de_um_item))


# 28. Lista com tuplas dentro

# Aqui temos uma lista que contém tuplas.
# A lista pode ser alterada.
# As tuplas internas não podem ser alteradas diretamente.

minhas_tuplas = [
    ('banana', 'leite'),
    ('maçã', 'uva')
]

print(minhas_tuplas)

# Como minhas_tuplas é uma lista, podemos usar append().
minhas_tuplas.append(('kiwi', 'morango'))
print(minhas_tuplas)

# Podemos remover uma tupla inteira.
minhas_tuplas.remove(('maçã', 'uva'))
print(minhas_tuplas)

# Podemos trocar um item da lista por outra tupla.
minhas_tuplas[1] = ('ouro', 'casa de batata')
print(minhas_tuplas)


# 29. Erros comuns observados

# Erro comum 1:
# append com vários argumentos.
#
# frutas.append('maçã', 'uva', 'banana')
#
# Isso dá erro porque append() aceita apenas um item por vez.

frutas = []

frutas.append('maçã')
frutas.append('uva')
frutas.append('banana')

print(frutas)

# Ou usando extend:

frutas = []

frutas.extend(['maçã', 'uva', 'banana'])

print(frutas)


# Erro comum 2:
# Usar colchetes para chamar método.
#
# frutas.append['maçã']
# frutas.remove['maçã']
#
# Métodos usam parênteses:
#
# frutas.append('maçã')
# frutas.remove('maçã')


# Erro comum 3:
# Tentar remover 'ixi' quando existe ['ixi'].

frutas = ['maçã', ['ixi'], 'banana']

# Aqui precisa remover a lista ['ixi'], não a string 'ixi'.
frutas.remove(['ixi'])

print(frutas)


# Erro comum 4:
# Esquecer aspas em texto.
#
# frutas.remove(banana)
#
# O Python vai pensar que banana é uma variável.
# Para texto, use aspas:

frutas = ['banana', 'maçã']

frutas.remove('banana')

print(frutas)


# Erro comum 5:
# Escrever o nome da variável errado.
#
# frutas = ['banana']
# ffrutas.remove('banana')
#
# ffrutas é diferente de frutas.
# O Python diferencia nomes escritos de forma diferente.


# 30. Loops: while

# while significa "enquanto".
# Ele repete um bloco de código enquanto uma condição for verdadeira.
#
# Estrutura:
#
# while condição:
#     código que será repetido
#
# Utilidade:
# Use while quando você NÃO sabe exatamente quantas vezes o código vai repetir.
#
# Exemplos:
# - pedir senha até acertar
# - criar menu que fica aberto até escolher sair
# - gerar números até encontrar um resultado
# - repetir algo enquanto uma condição for verdadeira


# Exemplo parecido com sua tentativa antiga:

contador = 10
numero_maismais = 0

while numero_maismais < contador:
    numero_maismais += 1
    print(numero_maismais)

# Explicação:
# numero_maismais começa em 0.
# Enquanto ele for menor que contador, ele aumenta 1.
# Depois imprime o valor atual.


# 31. Contagem regressiva com while

borabill = 10

while borabill >= 1:
    print(borabill)
    borabill -= 1

    if borabill == 0:
        print('Acabou!')

# Explicação:
# borabill começa em 10.
# A cada repetição, ele diminui 1.
# Quando chega em 0, mostra "Acabou!".


# 32. while com senha e limite de tentativas

# Esta é uma versão melhorada da sua tentativa antiga.
# A ideia é a mesma: pedir senha várias vezes.
# A diferença é que agora a lógica fica mais organizada.

senha_certa = 'receba123'
senha_colocada = ''
tentativas = 0
tentativas_maximas = 3

while senha_colocada != senha_certa:
    senha_colocada = input('Digite sua senha: ')

    if senha_colocada == senha_certa:
        print('Senha correta!')
        break

    tentativas += 1
    print('Senha incorreta! Tente novamente.')

    tentativas_restantes = tentativas_maximas - tentativas
    print(f'Tentativas restantes: {tentativas_restantes}')

    if tentativas >= tentativas_maximas:
        print('Número máximo de tentativas atingido. Acesso negado.')
        break

# Explicação:
# senha_colocada começa vazia.
# O while roda enquanto senha_colocada for diferente de senha_certa.
# Se acertar, mostra "Senha correta!" e para com break.
# Se errar, aumenta as tentativas.
# Se chegar no máximo, nega o acesso.


# 33. while com else

# O else do while só executa quando o while termina naturalmente.
# Se o while parar com break, o else não roda.

senha_certa = 'receba123'
tentativas = 0
tentativas_maximas = 3

while tentativas < tentativas_maximas:
    senha_digitada = input('Digite sua senha novamente: ')

    if senha_digitada == senha_certa:
        print('Senha correta! Acesso liberado.')
        break

    tentativas += 1
    print('Senha incorreta.')
else:
    print('Você errou todas as tentativas.')

# Neste exemplo:
# - Se acertar, break para o while e o else não roda.
# - Se errar todas, o while termina normalmente e o else roda.


# 34. break

# break para o loop imediatamente.
#
# Utilidade:
# Use break quando você já encontrou o que queria.

numero = 1

while numero <= 10:
    print(numero)

    if numero == 5:
        print('Encontrei o número 5. Parando o loop.')
        break

    numero += 1


# 35. continue

# continue pula o restante daquela repetição
# e vai direto para a próxima volta do loop.
#
# Utilidade:
# Use continue quando quiser ignorar um caso específico.

numero = 0

while numero < 10:
    numero += 1

    if numero == 5:
        continue

    print(numero)

# O número 5 não será mostrado.


# 36. for

# for é usado para percorrer uma sequência.
# Sequência pode ser lista, tupla, string, range e outras coisas.

compras = ['feijão', 'arroz', 'macarrão']

for item in compras:
    print(f'Você precisa comprar {item}')

# Explicação:
# A cada volta do for, item recebe um valor da lista.
#
# Primeira volta: item = 'feijão'
# Segunda volta: item = 'arroz'
# Terceira volta: item = 'macarrão'


# 37. for percorrendo string

palavra = 'Python'

for letra in palavra:
    print(letra)

# Utilidade:
# Dá para analisar letra por letra de uma palavra.


# 38. for com números

numeros = [1, 6, 5, 4, 2, 5, 67, 7, 78, 5, 3, 3, 6]

for numero in numeros:
    print(numero)


# 39. for com if: par ou ímpar

numeros = [1, 6, 5, 4, 2, 5, 67, 7, 78, 5, 3, 3, 6]

for numero in numeros:
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')


# 40. for com continue

# Esta parte mantém a ideia da sua tentativa:
# pular os pares e mostrar apenas os ímpares.

numeros = [1, 6, 5, 4, 2, 5, 67, 7, 78, 5, 3, 3, 6]

for numero in numeros:
    if numero % 2 == 0:
        continue

    print(numero)

# Explicação:
# Se o número for par, o continue pula o print.
# Então só os números ímpares aparecem.


# 41. for com break

# Agora o contrário:
# vamos parar quando encontrar o primeiro número par.

numeros = [1, 6, 5, 4, 2, 5, 67, 7, 78, 5, 3, 3, 6]

for numero in numeros:
    if numero % 2 == 0:
        print(f'Primeiro número par encontrado: {numero}')
        break

# Como o primeiro par da lista é 6, ele para no 6.


# 42. range()

# range() cria uma sequência de números.
# É muito usado com for.

for numero in range(1, 11):
    print(numero)

# range(1, 11) começa em 1 e vai até antes de 11.
# Resultado: 1 até 10.

for numero in range(0, 11, 2):
    print(numero)

# range(início, fim, passo)
# Neste caso:
# início = 0
# fim = 11
# passo = 2
#
# Resultado: 0, 2, 4, 6, 8, 10

for numero in range(10, 0, -1):
    print(numero)

print('Contagem regressiva finalizada!')


# 43. enumerate()

# enumerate() permite pegar o índice e o valor ao mesmo tempo.

compras = ['feijão', 'arroz', 'macarrão']

for indice, item in enumerate(compras):
    print(f'{indice} - {item}')

# Utilidade:
# Serve quando você quer mostrar uma lista numerada.


# 44. Funções

# Função é um bloco de código reutilizável.
#
# Estrutura:
#
# def nome_da_funcao():
#     código da função
#
# Utilidade:
# - evitar repetição de código
# - organizar melhor o programa
# - criar seus próprios comandos
# - separar partes do sistema
# - facilitar manutenção


def ola():
    print('Olá, Mundo')


ola()

# def ola(): cria a função.
# ola() executa a função.


# 45. Função com parâmetro

# Parâmetro é uma informação que a função recebe.

def saudacao(nome):
    print(f'Olá, {nome}!')


saudacao('Casca de bala')
saudacao('Lain')
saudacao('DoomCipher')

# Explicação:
# nome é o parâmetro.
# Quando fazemos saudacao('Lain'), o valor 'Lain' entra no lugar de nome.


# 46. Função com input

def saudacao_usuario(nome):
    print(f'Olá, {nome}! Seja bem-vindo.')


nome_inserido = input('Digite seu nome: ')
saudacao_usuario(nome_inserido)


# 47. Função com mais de um parâmetro

def somar(n1, n2):
    resultado = n1 + n2
    print(f'A soma de {n1} + {n2} é {resultado}')


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

somar(n1, n2)

# Também posso chamar a função passando valores diretamente:

somar(5, 7)


# 48. Função com nomes de parâmetros mais claros

def somar_v2(numero_um, numero_dois):
    resultado = numero_um + numero_dois
    print(f'A soma de {numero_um} + {numero_dois} é {resultado}')


somar_v2(5, 7)

# Usar nomes claros ajuda a entender melhor o código.


# 49. return

# return devolve um valor para quem chamou a função.
#
# Diferença entre print e return:
#
# print:
# apenas mostra algo na tela.
#
# return:
# devolve um valor para ser usado depois.

def somando(numero_um, numero_dois):
    resultado = numero_um + numero_dois
    return resultado


resultado_da_soma = somando(5, 6)

print(f'O resultado da soma é {resultado_da_soma}')

# Como o valor foi retornado, posso usar em outra conta:

dobro = resultado_da_soma * 2

print(f'O dobro do resultado é {dobro}')


# 50. Função com return direto

def somar_direto(numero_um, numero_dois):
    return numero_um + numero_dois


resultado = somar_direto(10, 20)
print(resultado)


# 51. Função que retorna True ou False

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


print(verificar_par(10))
print(verificar_par(7))

numero = int(input('Digite um número para verificar se é par: '))

if verificar_par(numero):
    print('O número é par.')
else:
    print('O número é ímpar.')


# 52. Versão mais curta da função anterior

def verificar_par_v2(numero):
    return numero % 2 == 0


print(verificar_par_v2(8))
print(verificar_par_v2(9))

# Explicação:
# numero % 2 == 0 já gera True ou False.
# Então podemos retornar diretamente essa comparação.


# 53. Função com valor padrão

# Podemos definir um valor padrão para um parâmetro.

def apresentar(nome='Visitante'):
    print(f'Olá, {nome}!')


apresentar('Lain')
apresentar()

# Na segunda chamada, como nenhum nome foi passado,
# a função usa o valor padrão 'Visitante'.


# 54. Docstring

# Docstring é uma explicação dentro da função.
# Ela fica entre aspas triplas logo abaixo do def.

def multiplicar(n1, n2):
    """
    Recebe dois números e retorna a multiplicação entre eles.
    """
    return n1 * n2


resultado = multiplicar(4, 5)
print(resultado)


# 55. Escopo de variável

# Escopo é onde uma variável existe.
# Uma variável criada dentro de uma função só existe dentro dela.

def teste_escopo():
    mensagem = 'Essa variável existe dentro da função.'
    print(mensagem)


teste_escopo()

# Isso daria erro, porque mensagem só existe dentro da função:
# print(mensagem)


# 56. Mini projeto: sistema de login com funções

# Aqui vamos pegar sua ideia da senha e transformar em funções.
# Isso deixa o código mais organizado.

def verificar_senha(senha_digitada, senha_correta):
    return senha_digitada == senha_correta


def pedir_senha():
    return input('Digite sua senha: ')


def sistema_login():
    senha_correta = 'receba123'
    tentativas = 0
    tentativas_maximas = 3

    while tentativas < tentativas_maximas:
        senha_digitada = pedir_senha()

        if verificar_senha(senha_digitada, senha_correta):
            print('Senha correta! Acesso liberado.')
            return True

        tentativas += 1
        print('Senha incorreta!')

    print('Acesso negado.')
    return False


sistema_login()

# Explicação:
# verificar_senha() confere se a senha está certa.
# pedir_senha() pede a senha.
# sistema_login() controla o funcionamento geral.


# 57. Módulos próprios

# Um módulo é basicamente outro arquivo Python que pode ser importado.
#
# Exemplo:
# Se você criar um arquivo chamado funcoes.py na mesma pasta,
# pode importar funções dele.
#
# Arquivo funcoes.py:
#
# def dandoola(nome):
#     print(f'Dando olá para {nome}')
#
# No arquivo principal, você pode usar:
#
# from funcoes import dandoola
# dandoola('Lain')

# Como talvez o arquivo funcoes.py ainda não exista,
# vou deixar o import comentado para não dar erro.
#
# Descomente quando você realmente criar o arquivo funcoes.py.

# from funcoes import dandoola
# dandoola('Lain')

# Utilidade:
# Separar funções em outro arquivo deixa o projeto mais organizado.
#
# Exemplo de organização:
#
# main.py       -> arquivo principal
# funcoes.py    -> funções gerais
# calculos.py   -> funções de cálculo
# mensagens.py  -> funções de mensagens


# 58. Bibliotecas

# Biblioteca é um conjunto de códigos prontos que outras pessoas criaram.
#
# Utilidade:
# Em vez de criar tudo do zero, você usa ferramentas prontas.
#
# Exemplos:
# - time: trabalhar com tempo e pausas
# - random: gerar números aleatórios
# - math: funções matemáticas
# - datetime: datas e horários
# - os: interagir com arquivos, pastas e sistema operacional
# - qrcode: gerar QR Codes


# 59. Biblioteca time

import time

print('Aguarde...')
time.sleep(2)
print('Pronto!')

# time.sleep(2) pausa o programa por 2 segundos.
#
# Utilidade:
# - simular carregamento
# - esperar antes de executar outra ação
# - fazer testes com tempo
# - criar delay em programas simples


# 60. Simulando carregamento com time

print('Carregando', end='')

for _ in range(3):
    time.sleep(1)
    print('.', end='')

print()
print('Carregamento concluído!')

# O _ é usado quando precisamos de uma variável no for,
# mas não vamos usar o valor dela.


# 61. Biblioteca random

import random

numero_aleatorio = random.randint(1, 50)

print(f'O número aleatório é: {numero_aleatorio}')

# random.randint(1, 50) gera um número inteiro aleatório entre 1 e 50.
#
# Utilidade:
# - criar sorteios
# - criar jogos
# - simular dados
# - escolher itens aleatórios
# - testar programas com valores variados


# 62. random.choice()

nomes = ['Lain', 'DoomCipher', 'Casca de bala', 'Python']

sorteado = random.choice(nomes)

print(f'O nome sorteado foi: {sorteado}')

# random.choice(lista) escolhe um item aleatório da lista.


# 63. random.shuffle()

cartas = ['A', 'K', 'Q', 'J', '10']

random.shuffle(cartas)

print(cartas)

# random.shuffle(lista) embaralha a própria lista.
# Ele modifica a lista original.


# 64. Gerando números aleatórios até encontrar um par

# Esta parte mantém sua ideia antiga:
# gerar números aleatórios até encontrar um número par.

while True:
    numero_aleatorio = random.randint(1, 50)
    print(f'O número aleatório é: {numero_aleatorio}')

    time.sleep(1)

    if numero_aleatorio % 2 == 0:
        print('Número par encontrado! Encerrando o programa.')
        break

# Explicação:
# while True cria um loop infinito.
# Ele só para quando encontra um break.
#
# Neste exemplo:
# - gera um número aleatório
# - mostra na tela
# - espera 1 segundo
# - se for par, encerra


# 65. Biblioteca math

# math é uma biblioteca padrão do Python para cálculos matemáticos.

import math

print(math.sqrt(25))    # Raiz quadrada
print(math.pow(2, 3))   # Potência
print(math.ceil(4.2))   # Arredonda para cima
print(math.floor(4.9))  # Arredonda para baixo
print(math.pi)          # Valor de pi

# Utilidade:
# - cálculos mais avançados
# - fórmulas matemáticas
# - programas de física
# - geometria
# - estatística básica


# 66. Biblioteca datetime

# datetime serve para trabalhar com datas e horários.

import datetime

agora = datetime.datetime.now()

print(agora)
print(agora.day)
print(agora.month)
print(agora.year)
print(agora.hour)
print(agora.minute)

# Utilidade:
# - registrar horário de ações
# - criar logs
# - mostrar data atual
# - fazer sistemas de agendamento
# - calcular tempo entre datas


# 67. Biblioteca os

# os permite interagir com o sistema operacional.

import os

pasta_atual = os.getcwd()

print(f'A pasta atual é: {pasta_atual}')

# Utilidade:
# - descobrir a pasta atual do programa
# - criar pastas
# - verificar se arquivos existem
# - trabalhar com caminhos de arquivos


# 68. Criando pasta com os

nome_da_pasta = 'testes_python'

if not os.path.exists(nome_da_pasta):
    os.mkdir(nome_da_pasta)
    print('Pasta criada com sucesso!')
else:
    print('A pasta já existe.')

# os.path.exists() verifica se algo existe.
# os.mkdir() cria uma pasta.


# 69. Formas de importar bibliotecas

# Forma 1: importar a biblioteca inteira.

import random

numero = random.randint(1, 10)
print(numero)

# Forma 2: importar apenas uma função específica.

from random import randint

numero = randint(1, 10)
print(numero)

# Forma 3: importar com apelido.

import random as rd

numero = rd.randint(1, 10)
print(numero)

# Quando usar cada uma?
#
# import random
# Bom para deixar claro de onde vem cada função.
#
# from random import randint
# Bom quando você quer usar uma função específica sem escrever random toda hora.
#
# import random as rd
# Bom quando o nome da biblioteca é grande ou muito usado.
#
# Exemplos famosos:
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# 70. Biblioteca qrcode

# A biblioteca qrcode serve para criar QR Codes.
#
# Ela NÃO vem instalada por padrão no Python.
# Para instalar no terminal, use:
#
# python -m pip install "qrcode[pil]"
#
# O [pil] instala suporte melhor para gerar imagens PNG.
#
# Utilidade:
# - criar QR Code para canal do YouTube
# - criar QR Code para Pix
# - criar QR Code para site
# - criar QR Code para contato
# - criar QR Code para Wi-Fi
# - criar QR Code para cardápio digital
# - criar QR Code para divulgação de assistência técnica


# 71. Criando QR Code simples do seu canal

# Este exemplo cria um QR Code apontando para seu canal:
# https://www.youtube.com/@doomcipher

import qrcode

link_do_canal = 'https://www.youtube.com/@doomcipher'

qr = qrcode.make(link_do_canal)

qr.save('qrcode_doomcipher.png')

print('QR Code criado com sucesso!')
print('Arquivo salvo como: qrcode_doomcipher.png')

# Depois de rodar este código, procure o arquivo:
# qrcode_doomcipher.png
#
# Ele será criado na mesma pasta em que você executou este arquivo Python.


# 72. Criando QR Code personalizado

import qrcode

link_do_canal = 'https://www.youtube.com/@doomcipher'

qr_code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr_code.add_data(link_do_canal)
qr_code.make(fit=True)

imagem_qr = qr_code.make_image(
    fill_color='black',
    back_color='white'
)

imagem_qr.save('qrcode_doomcipher_personalizado.png')

print('QR Code personalizado criado com sucesso!')
print('Arquivo salvo como: qrcode_doomcipher_personalizado.png')

# Explicação:
#
# version:
# Controla o tamanho do QR Code.
# Quanto maior a versão, mais informação ele consegue guardar.
#
# error_correction:
# Define o nível de correção de erro.
# ERROR_CORRECT_H é um nível alto.
# Isso ajuda o QR Code a continuar funcionando mesmo com pequenas falhas.
#
# box_size:
# Define o tamanho dos quadradinhos do QR Code.
#
# border:
# Define a borda branca ao redor do QR Code.
#
# fill_color:
# Define a cor dos quadradinhos.
#
# back_color:
# Define a cor do fundo.


# 73. Gerador de QR Code com input

# Este exemplo permite criar QR Code de qualquer link
# sem precisar alterar o código manualmente.

import qrcode

link = input('Digite o link que deseja transformar em QR Code: ')
nome_arquivo = input('Digite o nome do arquivo sem .png: ')

qr = qrcode.make(link)

qr.save(f'{nome_arquivo}.png')

print(f'QR Code salvo como {nome_arquivo}.png')

# Exemplo de uso:
#
# Link:
# https://www.youtube.com/@doomcipher
#
# Nome do arquivo:
# meu_canal
#
# Resultado:
# meu_canal.png


# 74. Gerador de QR Code usando função

# Agora vamos transformar o QR Code em função.
# Isso é melhor porque podemos reutilizar o código várias vezes.

import qrcode

def criar_qr_code(link, nome_arquivo):
    qr = qrcode.make(link)
    qr.save(f'{nome_arquivo}.png')
    print(f'QR Code salvo como {nome_arquivo}.png')


criar_qr_code(
    'https://www.youtube.com/@doomcipher',
    'canal_doomcipher'
)

# Podemos reutilizar a função para outros links:

criar_qr_code('https://www.google.com', 'google')
criar_qr_code('https://www.youtube.com', 'youtube')


# 75. Mini projeto: sorteador simples com função

import random

def sortear_nome(lista_de_nomes):
    return random.choice(lista_de_nomes)


nomes = ['Lain', 'DoomCipher', 'Python', 'Casca de bala']

nome_sorteado = sortear_nome(nomes)

print(f'O nome sorteado foi: {nome_sorteado}')


# 76. Mini projeto: lista de compras organizada

def mostrar_lista_de_compras(lista):
    print('Lista de compras:')

    for indice, item in enumerate(lista):
        print(f'{indice + 1}. {item}')


compras = ['feijão', 'arroz', 'macarrão']

mostrar_lista_de_compras(compras)

# Explicação:
# indice começa em 0.
# Por isso usamos indice + 1 para mostrar começando em 1.


# 77. Mini projeto: calculadora simples com função

def calcular(n1, n2, operacao):
    if operacao == '+':
        return n1 + n2
    elif operacao == '-':
        return n1 - n2
    elif operacao == '*':
        return n1 * n2
    elif operacao == '/':
        return n1 / n2
    else:
        return 'Operação inválida'


resultado = calcular(10, 5, '+')
print(resultado)

resultado = calcular(10, 5, '-')
print(resultado)

resultado = calcular(10, 5, '*')
print(resultado)

resultado = calcular(10, 5, '/')
print(resultado)


# 78. Resumo importante

# print:
# Mostra algo na tela.
#
# input:
# Recebe algo digitado pelo usuário.
#
# variável:
# Guarda um valor.
#
# type:
# Mostra o tipo de um valor.
#
# int:
# Converte para número inteiro.
#
# float:
# Converte para número decimal.
#
# str:
# Texto.
#
# bool:
# Verdadeiro ou falso.
#
# if:
# Executa algo se uma condição for verdadeira.
#
# elif:
# Testa outra condição.
#
# else:
# Executa algo se nenhuma condição anterior for verdadeira.
#
# lista:
# Coleção mutável de valores.
#
# tupla:
# Coleção imutável de valores.
#
# append:
# Adiciona um item no final da lista.
#
# extend:
# Adiciona vários itens na lista.
#
# insert:
# Adiciona um item em uma posição específica.
#
# remove:
# Remove um item pelo valor.
#
# pop:
# Remove um item pelo índice e devolve esse item.
#
# del:
# Apaga item ou fatia da lista.
#
# len:
# Mostra quantidade de itens.
#
# in:
# Verifica se algo está dentro.
#
# not in:
# Verifica se algo não está dentro.
#
# while:
# Repete enquanto uma condição for verdadeira.
#
# for:
# Percorre os itens de uma sequência.
#
# break:
# Para o loop imediatamente.
#
# continue:
# Pula para a próxima repetição.
#
# def:
# Cria uma função.
#
# parâmetro:
# Informação que a função recebe.
#
# return:
# Devolve um valor da função.
#
# módulo:
# Arquivo Python que pode ser importado.
#
# biblioteca:
# Conjunto de códigos prontos para usar.
#
# import:
# Comando usado para trazer bibliotecas ou módulos.
#
# time:
# Biblioteca para tempo e pausas.
#
# random:
# Biblioteca para números e escolhas aleatórias.
#
# math:
# Biblioteca para matemática.
#
# datetime:
# Biblioteca para datas e horários.
#
# os:
# Biblioteca para interagir com sistema, arquivos e pastas.
#
# qrcode:
# Biblioteca para gerar QR Codes.


# 79. Observações finais

# Este arquivo cresceu bastante porque virou um caderno de prática.
# Não precisa decorar tudo de uma vez.
#
# O mais importante agora é entender:
#
# 1. O Python executa de cima para baixo.
# 2. Variáveis guardam valores.
# 3. if/else tomam decisões.
# 4. listas guardam vários itens.
# 5. loops repetem ações.
# 6. funções organizam e reaproveitam código.
# 7. bibliotecas trazem ferramentas prontas.
#
# Quanto mais você praticar criando exemplos seus,
# mais natural tudo isso vai ficar.

