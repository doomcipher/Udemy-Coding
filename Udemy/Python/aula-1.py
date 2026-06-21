# Documento da primeira aula, não exatamente significa que as aulas são da aula que assisti, muito pelo contrário
# eu vou documentando tudo que aprendi com o passar do tempo que fiquei assistindo e praticando. 
# As vezes vai ficar extremamente desorganizado, mas depois eu organizo já que é apenas para aprender.

# Primeiros comandos 

print('Hello World')

# Imprime a frase entre aspas

print('Hello', 'World', sep="-")

# Faz com que em cada separador ( espaço maracado com a vírgula entre palavras) apareça um traço ou qualquer outra
# coisaque seja colocada entre aspas no sep=""

print('Hello', 'World', sep="[]", end="=") # o \n indica uma quebra de linha, ou seja, o próximo print vai aparecer em
                                        # uma nova linha, já o end="" indica que o próximo print vai aparecer na 
                                        # mesma linha, ou seja, sem quebra de linha.

print('Hello', 'World', sep=",", end="+") 

print('Hello', 'World', sep=".", end="()")

print('Hello', 'World', sep="~", end="()")







# Outros exemplos

# -----------------------------------------------------------------------------------------------------------------#

# Aspas Simples

print('Luiz')

# Aspas Duplas

print("Luiz")

# aspás triplas

print('''Luiz''')

# aspas triplas duplas

print("""Luiz""")

# aspas dentro de aspas

print('Luiz "Otávio"')

# Type

print(type('Luiz')) # str

print(type(20)) # int

print(type(20.20)) # float

# Variáveis

primeiro_numero = 5;
segundo_numero = 7;

print(primeiro_numero + segundo_numero)
print(primeiro_numero * segundo_numero)
print(primeiro_numero ** segundo_numero)
print(primeiro_numero - segundo_numero)
print(primeiro_numero % segundo_numero)
print(primeiro_numero / segundo_numero)
print(primeiro_numero // segundo_numero)
print(primeiro_numero > segundo_numero)
print(primeiro_numero < segundo_numero)
print(primeiro_numero >= segundo_numero)
print(primeiro_numero <= segundo_numero)
print(primeiro_numero == segundo_numero)
print(primeiro_numero != segundo_numero)


senha = "receba123";
senha_botada = input("Digite sua senha: ")

if senha_botada == senha:
    print("Senha correta!")
else:    print("Senha incorreta!")

# coleções odeio affffffffff

frutas = ['banana', 'maçã', 'uva']
frutas[0:1] = ['oier','laelezinho']

print(frutas)