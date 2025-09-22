# 🚀 PuLP Solver

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PuLP](https://img.shields.io/badge/PuLP-0078D4?style=for-the-badge)

**Uma aplicação web intuitiva que resolve problemas de programação linear sem que você precise escrever uma linha de código.**

<img width="900" alt="image" src="https://github.com/user-attachments/assets/a7cb40cc-0955-4d56-b350-a6aaa5a17cca" />

---

## Índice

- O Problema: Como Tomar a Melhor Decisão? [aqui](#o-problema-como-tomar-a-melhor-decisão)
- A Solução: Programação Linear. [aqui](#a-solução-programação-linear)
- Nosso Site: A Ferramenta que Simplifica Tudo. [aqui](#a-ferramenta-que-simplifica-tudo)
- Como Usar o PuLP Solver. [aqui](#como-usar-o-pulp-solver)
- Tecnologias Utilizadas. [aqui](#tecnologias-utilizadas)
- Como Executar o Projeto Localmente. [aqui](#como-executar-o-projeto-localmente)

---

## O Problema: Como Tomar a Melhor Decisão?

Todos os dias, empresas e pessoas enfrentam um desafio comum: **como usar recursos limitados da melhor maneira possível?**

-   Uma **fábrica** quer decidir quais produtos fabricar para ter o máximo de lucro, mas possui um limite de matéria-prima e horas de trabalho.
-   Uma **equipe de marketing** precisa distribuir seu orçamento entre diferentes canais (Google, Instagram) para obter o maior impacto, sem estourar os custos.
-   Um **provedor de nuvem** deve alocar tarefas em seus servidores para maximizar a receita, respeitando os limites de CPU, memória e banda.

Resolver esses quebra-cabeças "na intuição" quase sempre leva a perdas de eficiência e dinheiro. A boa notícia é que existe um método matemático para encontrar a resposta perfeita: **Programação Linear**.

---

## A Solução: Programação Linear

> A Programação Linear (PL) é uma técnica matemática poderosa usada para encontrar o melhor resultado possível (como lucro máximo ou custo mínimo) em um modelo cujos requisitos são representados por relações lineares.

Não se assuste com o nome! A ideia é muito simples e pode ser comparada a uma **receita de bolo**:

Imagine que você quer fazer bolos para vender e obter o **máximo de lucro**.

1.  🎯 **Função Objetivo (O que você quer otimizar?)**
    * Seu objetivo é `Maximizar o Lucro Total`. A cada bolo de chocolate você lucra R$ 20 e a cada bolo de baunilha, R$ 15.
    * *Matematicamente: `Lucro = 20 * (nº de bolos de chocolate) + 15 * (nº de bolos de baunilha)`*

2.  🤔 **Variáveis de Decisão (O que você pode controlar?)**
    * As suas decisões são: `quantos bolos de chocolate fazer` e `quantos bolos de baunilha fazer`.

3.  🧱 **Restrições (Quais são seus limites?)**
    * Você só tem 10 ovos e 1kg de farinha na sua cozinha.
    * Cada bolo de chocolate consome 2 ovos e 150g de farinha.
    * Cada bolo de baunilha consome 1 ovo e 200g de farinha.
    * *Esses são seus limites de recursos!*

A Programação Linear usa algoritmos para encontrar a combinação exata de bolos de chocolate e baunilha que maximiza seu lucro sem quebrar as regras (as restrições de ingredientes).

---

## A Ferramenta que Simplifica Tudo

Entender a teoria é ótimo, mas aplicá-la pode ser complexo. É por isso que criamos o **PuLP Solver**. A plataforma traduz seus problemas do mundo real para o modelo matemático e entrega a solução ótima para você, de forma visual e informativa.

### ✨ Funcionalidades

- **Interface Dinâmica**: Adicione quantas variáveis e restrições seu problema precisar.
- **Visualização Gráfica**: Para problemas com duas variáveis, geramos um gráfico da região de viabilidade e do ponto ótimo, facilitando a compreensão do resultado.
- **Análise de Sensibilidade**: Descubra quais são seus verdadeiros "gargalos".
- **Suporte Completo**: Resolve problemas de maximização e minimização, com variáveis contínuas ou inteiras.

---

## Como Usar o PuLP Solver

Resolver seu problema é tão simples quanto seguir 5 passos:

1.  **✍️ Defina o Problema**: Dê um nome ao seu problema e escolha se deseja `Maximizar` ou `Minimizar` seu objetivo.

2.  **➕ Adicione as Variáveis**: Clique em "+ Adicionar Variável" para cada variável de decisão do seu problema (ex: `Produto_A`, `Campanhas_Google`, etc.). Defina se são contínuas ou inteiras.

3.  **🎯 Construa a Função Objetivo**: À medida que você adiciona variáveis, a função objetivo é montada. Preencha os coeficientes que representam o impacto de cada variável (ex: lucro por produto, custo por campanha).

4.  **🧱 Adicione as Restrições**: Clique em "+ Adicionar Restrição" para cada limitação do seu problema. Preencha os coeficientes de cada variável na restrição, o tipo de limitação (`<=`, `>=`, `==`) e o valor limite.

5.  **🚀 Resolva!**: Clique em "Resolver Problema" e seja redirecionado para uma página de resultados completa, com o plano de ação, gráficos e análises para a sua melhor tomada de decisão.

---

## Tecnologias Utilizadas

Este projeto foi construído com uma combinação de tecnologias:

- **Back-end**: Python, Django
- **Otimização**: Biblioteca PuLP
- **Gráficos**: Matplotlib
- **Front-end**: HTML, CSS, JavaScript

---

## Como Executar o Projeto Localmente

Quer rodar o projeto na sua própria máquina? Siga os passos:

1.  **Clone o repositório.**
    ```bash
    git clone https://github.com/Vict0Rocha/pesquisa_operacional.git
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual.**
    ```bash
    python -m venv venv         # Para criar
    venv\Scripts\activate       # Ativar no windows
    source venv/bin/activate    # Ativar no Linux/Mac
    ```

3.  **Instale as dependências.**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute as migrações.**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Inicie o servidor de desenvolvimento.**
    ```bash
    python manage.py runserver
    ```

Acesse `http://127.0.0.1:8000/` no seu navegador e comece a otimizar!

---

*Este projeto foi desenvolvido na disciplina de Pesquisa Operacinal, apenas com o intuito de criar uma boa visilização na resolução de problemas com programação linear.*

Projeto gerador por [gemini](https://gemini.google.com/app)
