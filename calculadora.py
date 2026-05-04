# ============================================================
#  Calculadora Simples — Projeto Final
#  Disciplinas: Algoritmos, Matemática Aplicada, POO
# ============================================================

class Calculadora:
    """
    Classe que representa uma calculadora com operações
    aritméticas e lógicas (bônus 1 e 2).
    """

    # ---------- Operações Aritméticas ----------

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Erro: divisão por zero não é permitida.")
        return a / b

    # ---------- Operações Lógicas (Bônus 1) ----------

    def e_logico(self, a, b):
        """AND: True se ambos forem diferentes de zero."""
        return bool(a) and bool(b)

    def ou_logico(self, a, b):
        """OR: True se pelo menos um for diferente de zero."""
        return bool(a) or bool(b)

    def nao_logico(self, a):
        """NOT: inverte o valor lógico do primeiro número."""
        return not bool(a)

    # ---------- Executa a operação pelo símbolo ----------

    def calcular(self, a, operador, b):
        operacoes = {
            "+":   lambda: self.somar(a, b),
            "-":   lambda: self.subtrair(a, b),
            "*":   lambda: self.multiplicar(a, b),
            "/":   lambda: self.dividir(a, b),
            "AND": lambda: self.e_logico(a, b),
            "OR":  lambda: self.ou_logico(a, b),
            "NOT": lambda: self.nao_logico(a),   # usa só 'a'
        }

        operador = operador.strip().upper() if operador.strip().upper() in ("AND", "OR", "NOT") else operador.strip()

        if operador not in operacoes:
            raise ValueError(f"Operador '{operador}' não reconhecido.")

        return operacoes[operador]()


# ============================================================
#  Interface de texto (menu)
# ============================================================

def exibir_menu():
    print("\n" + "=" * 40)
    print("        CALCULADORA SIMPLES")
    print("=" * 40)
    print("  Operações aritméticas:")
    print("    +   Soma")
    print("    -   Subtração")
    print("    *   Multiplicação")
    print("    /   Divisão")
    print("  Operações lógicas (bônus):")
    print("    AND  E lógico  (a != 0  E  b != 0)")
    print("    OR   OU lógico (a != 0  OU b != 0)")
    print("    NOT  NÃO lógico (apenas usa o 1º número)")
    print("  Outros:")
    print("    S   Sair")
    print("=" * 40)


def ler_numero(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("  ⚠  Digite um número válido (ex: 3, -1.5, 0.75).")


def formatar_resultado(resultado):
    """Exibe inteiro sem casas decimais; float com até 10 dígitos."""
    if isinstance(resultado, bool):
        return "Verdadeiro" if resultado else "Falso"
    if isinstance(resultado, float) and resultado.is_integer():
        return str(int(resultado))
    return f"{resultado:.10g}"


def main():
    calc = Calculadora()

    print("\nBem-vinda à Calculadora!")

    while True:
        exibir_menu()

        operador = input("\nDigite o operador (ou S para sair): ").strip()

        if operador.upper() == "S":
            print("\nEncerrando a calculadora. Até logo!\n")
            break

        # NOT usa apenas um operando
        op_upper = operador.upper()
        if op_upper == "NOT":
            a = ler_numero("Digite o número: ")
            b = None
        else:
            a = ler_numero("Digite o 1º número: ")
            b = ler_numero("Digite o 2º número: ")

        try:
            resultado = calc.calcular(a, operador, b)

            if op_upper == "NOT":
                print(f"\n  Resultado: NOT {a} = {formatar_resultado(resultado)}")
            else:
                print(f"\n  Resultado: {a} {operador.upper()} {b} = {formatar_resultado(resultado)}")

        except ValueError as erro:
            print(f"\n  ⚠  {erro}")


if __name__ == "__main__":
    main()
