# # rf# Questão 1
def function(x):
    y = 2*x**2 + 3*x - 1
    return (x, y)

# Questão 2
def payday():
    salario_bruto = float(input("Qual seu salario:"))
    alicota = 0.15
    salario_liquido = salario_bruto * (1 - alicota)
    print(f"Seu salário bruto é: R$ {salario_bruto}\nSeu desconto do imposto de renda foi de: R$ {salario_bruto - salario_liquido}\nSeu salário líquido é: R$ {salario_liquido}")
    print("Seja feliz!")

# Questão 3
def greetings(name):
    return f"Bom dia {name}, tudo bem?"

# Questão 4
def lista():
    lista = [25, -1, 58, -10, 23, 2, 4, 8, 16, 32]
    lista.sort()
    return f"""
    tamanho: {len(lista)};
    menor: {min(lista)};
    maior: {max(lista)};
    sum: {sum(lista)};
    ordem crescente: {lista};
    ordem decrescente: {lista[::-1]};
    """

# Questão 5
def make_list():
    lista1 = list(range(0,21))
    lista2 = list(range(1,16))
    lista3 = list(range(0,22,2))
    lista4 = list(range(0,101,5))
    return f"{lista1}\n{lista2}\n{lista3}\n{lista4}"

# Questão 6
def notas(notas):
    media = 0
    for bim, nota in notas.items():
        print(f"Nota no {bim}: {nota}")
        media += nota
    return media

# Questão 7
def vadidate_user(user, password):

# Questão 8
def tabuada(number):
    for i in range(1,11):
        print(f"{i} x {number} = {number*i}")

# Questão 9
def line(length):
    print(''.join('_' for i in range(0, length + 1)))

# Questão 10
"""
10. Crie um código usando if, if-else ou if-elif-else, que solicite o login (string) e
senha (mínimo 8 caracteres).
O código deve:
- não permitir avançar se a senha for menor que 8 caracteres;
- verificar o login correto;
- a senha correta;
- retornar mensagem se o usuário foi autorizado ou não.
"""

def main():
    print(greetings("Sr. Raskolnikov"))
    payday()
    print(lista())
    print(make_list())

if __name__ == "__main__":
    main()
