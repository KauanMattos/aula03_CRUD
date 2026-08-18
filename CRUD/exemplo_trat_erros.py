# Tratamento de erros no python (try...except...else...finally)

# Exemplo sem o tratamento de erros
'''
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo segundo inteiro: "))

soma = num1 + num2

print(f"A soma dos dois números é: {soma}")
'''
# Mesmo exemplo com tratamento de erros

try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo segundo inteiro: "))
except ValueError: # except é executado quando o "python" não consegue fazer as conversões para int 
    print("Os dados devem ser númericos!")
else: # else é quando deu certo no try
    soma = num1 + num2
    print(f"A soma dos dois números é: {soma}")
finally: # finally é opcional, mas é executado para garantir a execução de um trecho de código, independentemente de ter ocorrido uma exceção ou não
    print("Programa finalizado")