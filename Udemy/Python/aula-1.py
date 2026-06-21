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


# 1. Primeiro comando: print()

# Mostra uma mensagem simples na tela
print('Hello World')

# Também podemos imprimir números
print(10)
print(20.5)

# Podemos imprimir mais de um valor separando por vírgula
print('Hello', 'World')

# Podemos misturar texto e número no mesmo print
print('Minha idade é', 18)


# 2. Usando sep no print()

# O sep define o separador entre os valores do print.
# Por padrão, o separador é um espaço.

print('Hello', 'World')              # Separador padrão: espaço
print('Hello', 'World', sep='-')     # Separador com traço
print('Hello', 'World', sep='[]')    # Separador com []
print('2026', '06', '21', sep='/')   # Simulando uma data
print('Python', 'é', 'bom', sep=' ') # Separador com espaço manual


# 3. Usando end no print()

# O end define o que acontece no final do print.
# Por padrão, o print termina com quebra de linha.
# A quebra de linha é representada por \n.

print('Linha 1')
print('Linha 2')

# Aqui o segundo print continua na mesma linha
print('Hello', end=' ')
print('World')

# Outros exemplos com end
print('Hello', 'World', sep='-', end=' | ')
print('Próximo print na mesma linha')

print('A', end='')
print('B', end='')
print('C')

# Pulando uma linha manualmente
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

# Aspas dentro de aspas
print('Luiz "Otávio"')
print("Luiz 'Otávio'")

# Quebra de linha dentro da string usando \n
print('Primeira linha\nSegunda linha')

# Tabulação usando \t
print('Nome:\tLuiz')
print('Idade:\t18')


# 5. Tipos de dados com type()

# type() mostra o tipo de um valor.

print(type('Luiz'))    # str   -> texto
print(type(20))        # int   -> número inteiro
print(type(20.20))     # float -> número decimal
print(type(True))      # bool  -> verdadeiro ou falso
print(type(False))     # bool  -> verdadeiro ou falso

# Exemplos de valores booleanos
print(True)
print(False)


# 6. Variáveis

# Variável é um nome que guarda um valor.

nome = 'Luiz'
idade = 18
altura = 1.75
estudando_python = True

print(nome)
print(idade)
print(altura)
print(estudando_python)

# Também podemos usar variáveis dentro de prints
print('Meu nome é', nome)
print('Minha idade é', idade)
print('Minha altura é', altura)


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

# Exemplos extras
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(2 ** 3)

# Ordem das operações
resultado = 10 + 5 * 2
print(resultado)

# Usando parênteses para controlar a ordem
resultado = (10 + 5) * 2
print(resultado)


# 8. Comparações

# Comparações retornam True ou False.

print(primeiro_numero > segundo_numero)    # Maior que
print(primeiro_numero < segundo_numero)    # Menor que
print(primeiro_numero >= segundo_numero)   # Maior ou igual
print(primeiro_numero <= segundo_numero)   # Menor ou igual
print(primeiro_numero == segundo_numero)   # Igual
print(primeiro_numero != segundo_numero)   # Diferente

# Exemplos extras
print(10 == 10)
print(10 != 5)
print(8 > 3)
print(8 < 3)
print('a' == 'a')
print('a' == 'b')


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

# Também daria para fazer direto assim:
outro_numero = int(input('Digite outro número: '))
print(outro_numero * 2)


# 11. If e else

# if significa "se".
# else significa "senão".

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


# 13. Listas

# Lista é uma coleção de valores.
# Listas usam colchetes [].
# Os itens da lista são acessados por índice.
# O primeiro índice é 0.

frutas = ['banana', 'maçã', 'uva']

print(frutas)

# Acessando itens da lista
print(frutas[0])  # banana
print(frutas[1])  # maçã
print(frutas[2])  # uva

# Índice negativo acessa de trás para frente
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

# Exemplo de lista normal
frutas = ['maçã', 'ixi', 'banana']
print(frutas)

# Exemplo de lista dentro de lista
frutas = ['maçã', ['ixi'], 'banana']
print(frutas)

# Na lista acima, ['ixi'] é uma lista dentro da lista principal.
# Por isso, 'ixi' e ['ixi'] não são a mesma coisa.

print(frutas[1])     # ['ixi']
print(frutas[1][0])  # ixi


# 16. Fatiamento de listas

frutas = ['banana', 'maçã', 'uva', 'laranja', 'abacaxi']

print(frutas[0:2])   # Pega do índice 0 até antes do índice 2
print(frutas[1:4])   # Pega do índice 1 até antes do índice 4
print(frutas[:3])    # Pega do começo até antes do índice 3
print(frutas[2:])    # Pega do índice 2 até o final
print(frutas[:])     # Copia a lista inteira

# Alterando uma parte da lista
frutas[0:2] = ['morango', 'kiwi']
print(frutas)


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

# Também pode apagar uma fatia da lista
frutas = ['banana', 'maçã', 'uva', 'laranja', 'abacaxi']

del frutas[1:3]
print(frutas)


# 23. len()

# len() mostra a quantidade de itens.

frutas = ['banana', 'maçã', 'uva']

print(len(frutas))


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

# Acessando itens da tupla
print(minha_tupla[0])
print(minha_tupla[1])

# Isso daria erro, porque tupla não pode ser alterada:
# minha_tupla[0] = 'maçã'


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


# Fim das anotações da aula 01

