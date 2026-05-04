# Calculadora Simples

Projeto final desenvolvido em Python que emula uma calculadora com as quatro operações aritméticas básicas, operações lógicas e interface de menu em linha de comando.

---

## Disciplinas contempladas

- Algoritmo e Linguagem de Programação
- Matemática Aplicada
- Programação Orientada a Objeto (POO)

---

## Como executar

Requisito: Python 3 instalado.

```bash
python calculadora.py
```

---

## Operações disponíveis

### Aritméticas

| Símbolo | Operação       | Exemplo         | Resultado |
|---------|----------------|-----------------|-----------|
| `+`     | Soma           | `10 + 3`        | `13`      |
| `-`     | Subtração      | `10 - 3`        | `7`       |
| `*`     | Multiplicação  | `10 * 3`        | `30`      |
| `/`     | Divisão        | `10 / 3`        | `3.3333…` |

### Lógicas (Bônus 1)

Considera qualquer número diferente de zero como **Verdadeiro** e zero como **Falso**.

| Símbolo | Operação    | Descrição                                  | Exemplo        | Resultado    |
|---------|-------------|--------------------------------------------|----------------|--------------|
| `AND`   | E lógico    | Verdadeiro se **ambos** forem != 0         | `1 AND 0`      | `Falso`      |
| `OR`    | OU lógico   | Verdadeiro se **pelo menos um** for != 0   | `0 OR 5`       | `Verdadeiro` |
| `NOT`   | NÃO lógico  | Inverte o valor lógico do primeiro número  | `NOT 0`        | `Verdadeiro` |

---

## Estrutura do código

```
calculadora.py
├── class Calculadora          # Encapsula toda a lógica de cálculo (POO)
│   ├── somar(a, b)
│   ├── subtrair(a, b)
│   ├── multiplicar(a, b)
│   ├── dividir(a, b)          # Valida divisão por zero
│   ├── e_logico(a, b)         # AND
│   ├── ou_logico(a, b)        # OR
│   ├── nao_logico(a)          # NOT
│   └── calcular(a, op, b)     # Despacha para o método correto pelo símbolo
├── exibir_menu()              # Imprime o menu de opções
├── ler_numero(msg)            # Lê e valida a entrada numérica do usuário
├── formatar_resultado(res)    # Formata o resultado para exibição
└── main()                     # Loop principal da interface
```

### Por que usar uma classe? (Bônus 2 — POO)

A classe `Calculadora` **encapsula** toda a lógica matemática, separando-a da interface com o usuário. Isso aplica o princípio de **responsabilidade única**: a classe só sabe calcular; a função `main()` só sabe interagir com o usuário. Se futuramente precisar trocar o menu por uma interface gráfica, a classe `Calculadora` não precisa mudar.

---

## Validações implementadas

- Entrada não-numérica: o programa solicita nova entrada até receber um número válido.
- Divisão por zero: exibe mensagem de erro sem encerrar o programa.
- Operador inválido: exibe mensagem de erro sem encerrar o programa.

---

## Exemplo de uso

```
========================================
        CALCULADORA SIMPLES
========================================
  Operações aritméticas:
    +   Soma
    -   Subtração
    *   Multiplicação
    /   Divisão
  Operações lógicas (bônus):
    AND  E lógico  (a != 0  E  b != 0)
    OR   OU lógico (a != 0  OU b != 0)
    NOT  NÃO lógico (apenas usa o 1º número)
  Outros:
    S   Sair
========================================

Digite o operador (ou S para sair): /
Digite o 1º número: 10
Digite o 2º número: 0

  ⚠  Erro: divisão por zero não é permitida.
```
