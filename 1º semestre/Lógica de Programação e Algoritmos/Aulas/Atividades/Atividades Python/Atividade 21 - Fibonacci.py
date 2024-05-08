v1 = int(input('Digite quantos numeros da sequencia deseja ver: '))

t1 = 1
t2 = 1
con = 2

print(t1)
print(t2)

while con < v1:
    v2 = t1 + t2
    print(v2)
    t1, t2 = t2, v2
    con += 1