# calculo1-python
Atividade de Cálculo 1 envolvendo Python!

Limites e Derivadas com Python

Exercícios de Cálculo 1 resolvidos de forma numérica em Python, feitos na disciplina de Elementos da Diferenciação Computacional (Ciência da Computação, UNICAP). A ideia central é usar o computador para enxergar dois conceitos: o limite como o valor de que uma função se aproxima, e a derivada como o limite do quociente de diferenças.

O que o projeto cobre
Limites numéricos: aproximação de um ponto pela esquerda e pela direita com valores de h cada vez menores, e estimativa do limite a partir das tabelas.
Limites laterais e continuidade: um caso em que a função não está definida no ponto (buraco no gráfico) e outro em que o valor da função no ponto é diferente do limite.
Derivada pela definição: cálculo numérico de s'(x) e f'(x) com o quociente [f(x + h) - f(x)] / h.
Reta tangente e reta secante: comparação entre o resultado numérico e a derivada analítica, e visualização da secante se aproximando da tangente.
Resumo dos resultados
Estudo	Função	Resultado
Limite com buraco	f(x) = (x² - 1)/(x - 1)	O limite quando x tende a 1 é 2, e f(1) não existe
Limite diferente do valor	g(x) = x + 2 (x ≠ 2), g(2) = 10	O limite quando x tende a 2 é 4, mas g(2) = 10
Velocidade instantânea	s(t) = t² + 3t + 2	s'(2) = 7
Derivada e tangente	f(x) = x³ - 4x + 1	f'(1) = -1, reta tangente y = -x - 1

O quociente de diferenças do último caso é h² + 3h - 1, que tende a -1 quando h diminui. Isso confere com a derivada analítica f'(x) = 3x² - 4.

Gráficos gerados
f(x) = (x² - 1)/(x - 1) próximo de x = 1, com o ponto vazio em (1, 2) marcando o buraco.
g(x) próximo de x = 2, com o limite (ponto vazio em y = 4) e o valor da função (ponto em y = 10).
f(x) = x³ - 4x + 1 no intervalo [-3, 3].
A mesma função com a reta tangente em x = 1.
Como executar

No Google Colab: copiei e colei este código numa célula e enviei ao meu professor, como solicitado. Nenhuma instalação de biblioteca é necessária.

No computador:

bash
pip install matplotlib
python prova_pratica.py

O script imprime as tabelas e as interpretações no terminal e abre uma janela para cada gráfico.

Tecnologias Utilizadas:
Python 3
matplotlib, apenas para os gráficos

O restante usa só utilizei Python básico: funções, listas, laços for e print formatado.

Autor:

Gustavo Sérgio Lira Cordeiro, estudante de Ciência da Computação.
