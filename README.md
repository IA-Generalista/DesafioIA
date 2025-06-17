#  Desafio de IA - Remoção de Duplicatas de um Array

Este repositório apresenta a solução para o desafio **"Remover Duplicatas de um Array com Auxílio de IA"**, proposto para exercitar lógica de programação, manipulação de arrays em Python e o uso estratégico da Inteligência Artificial no desenvolvimento de software.

---

## 👥 Participantes

- Caroliny Gonçalves
- Juliana Ramos
- Marcelo Costa
- Michel Gonçalves
- Thainara Cruz
- Victoria Borges

---

##  Como a IA nos ajudou

Durante o desenvolvimento deste projeto, utilizamos **Inteligência Artificial** em diversas etapas:

1. **Entendimento da proposta:**  
   A IA nos ajudou a interpretar o desafio e esclarecer dúvidas sobre os requisitos, garantindo que compreendêssemos os critérios corretos de implementação.

2. **Refinamento do prompt para o Copilot:**  
   Com o auxílio da IA, aprimoramos os comandos e prompts enviados ao GitHub Copilot, melhorando a qualidade e a precisão das sugestões de código.

3. **Geração de dados de teste:**  
   A IA sugeriu diferentes cenários para testarmos a função, incluindo listas de números, letras, elementos repetidos e listas vazias, o que garantiu maior robustez e cobertura.

> ✅ A colaboração com IA tornou o processo mais ágil, criativo e eficiente, mas as decisões lógicas e os ajustes finais foram feitos com análise crítica pela equipe.

---

## 🎯 Objetivo

Criar uma função em Python chamada `remover_duplicatas(array)` que:

- Receba uma lista como parâmetro;
- Retorne uma nova lista com os **elementos únicos**, mantendo a **ordem original**;
- Seja testada com diferentes tipos de entrada: números, strings, listas vazias e com elementos repetidos.

---

## 🛠 Tecnologias Utilizadas

- Python 3.x  
- Visual Studio Code  
- GitHub Copilot (extensões: Copilot e Copilot Chat)  
- Git + GitHub  

---

## 💻 Código-fonte

```python
def remover_duplicatas(array):
    elementos_vistos = set()
    resultado = []
    for item in array:
        if item not in elementos_vistos:
            resultado.append(item)
            elementos_vistos.add(item)
    return resultado

# Testes
print(remover_duplicatas([1, 2, 2, 3, 4, 4, 5]))
print(remover_duplicatas(["a", "b", "a", "c", "d", "d"]))
print(remover_duplicatas([1, 1, 1, 1, 1]))
print(remover_duplicatas([]))

