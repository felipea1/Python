# i = 1

# while i < 10:
#     print(i)
#     i += 1

# print("Terminou!")
# print(i)

#criancas = ["Lucas", "Kayque", "Carlos"]
#              0         1         2
# for item in criancas:
#     print(item)

# canal = "yFelpsz"

# for letra in canal:
#     print(letra)

# for index in range(len(criancas)):
#     print(criancas[index],index)
#     print(index)

# for index in range (5):
#     if index == 0:
#         print("Primeira linha")
#     else:
#         print(f"outras linhas {criancas[index]}")

matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]

for linha in matrix_numeros:
    #print(linha)
    print("----")
    for coluna in linha:
        print(coluna)