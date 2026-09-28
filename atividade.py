'''
Prova Prática de Cálculo 1
Professor : Júlio Aleixo
Aluno : Gustavo Sérgio Lira Cordeiro
Disciplina : Elementos da Diferenciação Computacional
'''
import matplotlib.pyplot as plt

# ======================================================================
# QUESTÃO 1 - f(x) = (x² - 1) / (x - 1), perto de x = 1
# ======================================================================
print("QUESTÃO 1")

def f(x):
    # função da questão 1
    return (x**2 - 1) / (x - 1)

# a) valores de h cada vez menores
valores_de_h = [0.1, 0.01, 0.001, 0.0001]

print("\nItem a) Tabela")
print(f"{'h':>8} | {'f(1 - h)':>10} | {'f(1 + h)':>10}")
for h in valores_de_h:
    esquerda = f(1 - h)   # x menor que 1; x tendendo a 1 pela esquerda (x -> 1-)
    direita = f(1 + h)    # x maior que 1; x tendendo a 1 pela direita (x -> 1+)
    print(f"{h:>8} | {esquerda:>10.4f} | {direita:>10.4f}")

# b) conclusão
print("""
Item b) Pela esquerda os valores de f(x) sobem e se aproximam MUITO de 2
(1,9; 1,99; 1,999; 1,9999). Pela direita eles descem e também chegam
MUITO perto de 2 (2,1; 2,01; 2,001; 2,0001). Como os dois lados se aproximam
do mesmo número, o limite de f(x) quando x tende a 1 é 2.
""")

# c) gráfico: para x diferente de 1, f(x) = x + 1, então uso listas de pontos
#    que pulam o valor x = 1
x_pela_esquerda = [i / 100 for i in range(0, 98)]     # de 0,00 até 0,97
x_pela_direita = [i / 100 for i in range(103, 201)]   # de 1,03 até 2,00

plt.plot(x_pela_esquerda, [f(x) for x in x_pela_esquerda], color="blue")
plt.plot(x_pela_direita, [f(x) for x in x_pela_direita], color="blue", label="f(x)")
# bolinha vazia em (1, 2): o limite existe, mas f(1) não existe
plt.plot(1, 2, "o", markerfacecolor="white", markeredgecolor="red",
         markersize=12, label="x = 1")
plt.title("Gráfico de f(x) = (x² - 1)/(x - 1) perto de x = 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

print("""
Item c) O gráfico tem uma interrupção em x = 1 porque nesse ponto o
denominador é zero, então f(1) não existe, é indeterminado (dá 0/0). Fatorando,
x² - 1 = (x - 1)(x + 1), e para x diferente de 1 a função é igual a x + 1.
O gráfico é uma reta com um buraco em (1, 2). O limite existe porque
olha só para os pontos vizinhos de 1, e não para o próprio 1.
""")

# ======================================================================
# QUESTÃO 2 - g(x) = x + 2 para x diferente de 2, e g(2) = 10
# ======================================================================
print("QUESTÃO 2")

# a) função implementada
def g(x):
    if x == 2:
        return 10
    else:
        return x + 2

# b) valores cada vez mais perto de 2, pela esquerda e pela direita
print("\nItem b) Tabela")
print(f"{'h':>8} | {'g(2 - h)':>10} | {'g(2 + h)':>10}")
for h in [0.1, 0.01, 0.001, 0.0001, 0.00001]:
    print(f"{h:>8} | {g(2 - h):>10.5f} | {g(2 + h):>10.5f}")

# c) e d)
print(f"\ng(2) = {g(2)}")
print("""
Item c) Os dois lados se aproximam de 4, então o limite de g(x)
quando x tende a 2 é 4.

Item d) O limite é 4, mas g(2) = 10. São valores diferentes. Então o
limite NÃO depende do valor da função exatamente em x = 2. Ele depende
só dos valores de g que se aproximam de 2 (com x diferente de 2). Como o limite é
diferente de g(2), a função é descontínua em x = 2.
""")

# e) gráfico
x_pela_esquerda = [i / 100 for i in range(0, 198)]     # de 0,00 até 1,97
x_pela_direita = [i / 100 for i in range(203, 401)]    # de 2,03 até 4,00

plt.plot(x_pela_esquerda, [g(x) for x in x_pela_esquerda], color="blue")
plt.plot(x_pela_direita, [g(x) for x in x_pela_direita], color="blue", label="g(x) = x + 2")
plt.plot(2, 4, "o", markerfacecolor="white", markeredgecolor="red",
         markersize=12, label="limite = 4")
plt.plot(2, 10, "o", color="green", markersize=8, label="g(2) = 10")
plt.title("Gráfico de g(x) perto de x = 2")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.grid(True)
plt.legend()
plt.show()

print("""
Item e) No gráfico, a reta chega em y = 4 quando x = 2 (bolinha vazia),
mas o valor real da função em x = 2 é 10 (bolinha verde sozinha).
""")

# ======================================================================
# QUESTÃO 3 - s(t) = t² + 3t + 2, velocidade em t = 2
# ======================================================================
print("QUESTÃO 3")

# a) função posição
def s(t):
    return t**2 + 3 * t + 2


# b) quociente [s(2 + h) - s(2)] / h para h cada vez menor
print("\nItem b) Tabela")
print(f"{'h':>8} | {'[s(2+h) - s(2)] / h':>20}")
for h in [0.1, 0.01, 0.001, 0.0001, 0.00001]:
    quociente = (s(2 + h) - s(2)) / h
    print(f"{h:>8} | {quociente:>20.5f}")

# c) conclusão
print("""
Item c) Os valores são 7,1; 7,01; 7,001; 7,0001; 7,00001 e vão chegando
em 7. Então s'(2) é aproximadamente 7, ou seja, a velocidade instantânea
em t = 2 é 7.
""")

# ======================================================================
# QUESTÃO 4 - f(x) = x^3 - 4x + 1
# ======================================================================
print("QUESTÃO 4")

def f4(x):
    return x**3 - 4 * x + 1

# a) gráfico de -3 a 3 (uso passos de 0,01)
xs = [i / 100 for i in range(-300, 301)]
ys = [f4(x) for x in xs]

plt.plot(xs, ys, color="blue", label="f(x) = x³ - 4x + 1")
plt.title("Gráfico de f(x) = x³ - 4x + 1 no intervalo [-3, 3]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

# b) derivada numérica em x = 1 com vários valores de h
print("\nItem b) Tabela")
print(f"{'h':>10} | {'[f(1+h) - f(1)] / h':>20}")
derivada_numerica = 0
for h in [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]:
    derivada_numerica = (f4(1 + h) - f4(1)) / h
    print(f"{h:>10} | {derivada_numerica:>20.6f}")
# no fim do loop, derivada_numerica guarda o valor do menor h
print(f"\nEstimativa: f'(1) é aproximadamente {derivada_numerica:.4f}")

# c) gráfico com a reta tangente: y = f(1) + m*(x - 1)
m = round(derivada_numerica, 2)   # inclinação (arredondei para tirar o erro pequeno)
y_tangente = [f4(1) + m * (x - 1) for x in xs]

plt.plot(xs, ys, color="blue", label="f(x)")
plt.plot(xs, y_tangente, color="red", linestyle="--", label="reta tangente em x = 1")
plt.plot(1, f4(1), "ko", label="ponto (1, -2)")
plt.ylim(-8, 8)   # limita o eixo y para a reta aparecer bem
plt.title("f(x) = x³ - 4x + 1 e a reta tangente em x = 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

# d) derivada analítica (à mão): f'(x) = 3x² - 4
derivada_analitica = 3 * 1**2 - 4
print(f"\nItem d) f'(x) = 3x² - 4, então f'(1) = {derivada_analitica}")
print(f"Numérico: {derivada_numerica:.6f} | Analítico: {derivada_analitica}")
print("Os dois resultados são praticamente iguais. A pequena diferença")
print("vem de h não ser exatamente zero.")

# e) explicação
print("""
Item e) A reta secante passa pelo ponto (1, f(1)) e pelo ponto
(1 + h, f(1 + h)). Quando h diminui, o segundo ponto chega cada vez mais
perto do primeiro, e a inclinação da secante chega cada vez mais perto de
f'(1). Como a reta tangente tem exatamente essa inclinação, a secante
vira a tangente no limite quando h tende a 0.
""")
