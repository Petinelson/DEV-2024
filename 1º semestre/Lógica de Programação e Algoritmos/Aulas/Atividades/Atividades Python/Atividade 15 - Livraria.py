print("[1]R$ 0,25 por livro + R$ 7,50 fixo")
print("[2]R$ 0,50 por livro + R$ 2,50 fixo")
livro = int(input('Digite a quantidade de livros que deseja comprar: '))
op1 = (livro * 0.25) + 7.50
op2 = (livro * 0.50) + 2.50

if op1 > op2:
    print('A melhor opção é a 2', op2)
elif op2 > op1:
    print('A melhor opção é a 1', op1)