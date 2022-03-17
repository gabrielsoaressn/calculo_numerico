resultado = 4.0 #considerando que o pi na primeira iteração o resultado é  4
N = 10000000
itera = 0
numerador = 4

for i in range (1, N):
    numerador *= -1
    itera = numerador/float((2*i)+1) 
    resultado += itera
print(resultado);