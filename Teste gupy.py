# Exercício 1 - Linguagem python

def pertence_fibonacci(num):
    if num == 0 or num == 1:
        return True  # 0 e 1 estão na sequência

    a, b = 0, 1
    while b < num:
        a, b = b, a + b  # Calcula o próximo número na sequência

    return b == num  # Verifica se o número calculado é igual ao número informado

# Solicita a entrada do usuário
numero = int(input("Informe um número para verificar na sequência de Fibonacci: "))

# Verifica se o número pertence à sequência de Fibonacci
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")




# Exercício 2 - Linguagem python

def contar_letras_a(string):
    # Converte a string para minúsculas para facilitar a contagem
    string_lower = string.lower()
    
    # Conta quantas vezes a letra 'a' aparece
    contador = string_lower.count('a')
    
    return contador

# Solicita a entrada do usuário
texto = input("Informe uma string para verificar a ocorrência da letra 'a': ")

# Verifica a ocorrência da letra 'a'
quantidade_a = contar_letras_a(texto)

# Exibe o resultado
if quantidade_a > 0:
    print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")





# Exercício 3 - Linguagem c

int INDICE = 12, SOMA = 0, K = 1;
enquanto K < INDICE faça {
    K = K + 1;
    SOMA = SOMA + K;
}
imprimir(SOMA);

Iteração 1: K = 2, SOMA = 2
Iteração 2: K = 3, SOMA = 5 (2 + 3)
Iteração 3: K = 4, SOMA = 9 (5 + 4)
Iteração 4: K = 5, SOMA = 14 (9 + 5)
Iteração 5: K = 6, SOMA = 20 (14 + 6)
Iteração 6: K = 7, SOMA = 27 (20 + 7)
Iteração 7: K = 8, SOMA = 35 (27 + 8)
Iteração 8: K = 9, SOMA = 44 (35 + 9)
Iteração 9: K = 10, SOMA = 54 (44 + 10)
Iteração 10: K = 11, SOMA = 65 (54 + 11)
Iteração 11: K = 12, SOMA = 77 (65 + 12)

Valor final de SOMA: 77.



# Exercício 4

a) 1, 3, 5, 7, ___

Lógica: Sequência de números ímpares consecutivos.
Próximo número: 9

b) 2, 4, 8, 16, 32, 64, ____

Lógica: Multiplicação por 2 a cada passo.
Próximo número: 128

c) 0, 1, 4, 9, 16, 25, 36, ____

Lógica: Quadrados perfeitos 
Próximo número: 49

d) 4, 16, 36, 64, ____

Lógica: Quadrados perfeitos de números pares
Próximo número: 100

e) 1, 1, 2, 3, 5, 8, ____

Lógica: Sequência de Fibonacci.
Próximo número: 13

f) 2, 10, 12, 16, 17, 18, 19, ____

Lógica: Alterna entre números com um padrão de adição variado e depois sequência consecutiva.
Próximo número: 20



# Exercício 5

Para descobrir qual interruptor controla cada lâmpada, fiz assim: primeiro, liguei o primeiro interruptor e deixei ligado por uns 5 a 10 minutos para a lâmpada esquentar. Depois, desliguei esse interruptor e liguei o segundo.

Aí fui até as salas. Se a lâmpada estivesse acesa, era a do segundo interruptor. Se estivesse apagada, eu tocava nela. Se estivesse quente, era a do primeiro. Se estivesse apagada e fria, era a do terceiro.

Com isso, descobri qual interruptor controla cada lâmpada em só duas idas!