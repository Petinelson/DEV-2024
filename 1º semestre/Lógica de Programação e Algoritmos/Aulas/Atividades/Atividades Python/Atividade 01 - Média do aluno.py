n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

soma = n1 + n2 + n3
media = soma / 3

print("A média do aluno é: ", media)
if media >= 7:
    print("Aprovado")
elif media > 3:
    print("Recuperação")
else:
    print("Reprovado")