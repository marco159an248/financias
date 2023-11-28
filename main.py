class GastosMensais:
    def __init__(self):
        self.gastos = {
            'aluguel': 0.0,
            'conta_de_luz': 0.0,
            'conta_de_agua': 0.0,
            'internet': 0.0,
            'alimentacao': 0.0,
            'transporte': 0.0,
            'educacao': 0.0,
            'entretenimento': 0.0
        }
        self.total_gastos = 0.0

    def obter_valor_numerico(self, mensagem):
        while True:
            try:
                valor = float(input(mensagem))
                return valor
            except ValueError:
                print("Valor inválido. Tente novamente.")

    def calcular_total_gastos(self):
        self.total_gastos = sum(self.gastos.values())

    def exibir_gastos(self):
        print("----- Gastos Mensais -----")
        for categoria, valor in self.gastos.items():
            print(f"{categoria.replace('_', ' ')}: R$ {valor:.2f}")
        print(f"Total de gastos mensais: R$ {self.total_gastos:.2f}")

    def reduzir_valor_gasto(self, categoria, percentual):
        economia = self.gastos[categoria] * (percentual / 100)
        self.gastos[categoria] -= economia
        self.total_gastos -= economia

    def alterar_gastos(self):
        print("----- Alternativas de redução de custos -----")
        print("1. Reduzir o valor da internet")
        print("2. Fazer refeições em casa")
        print("3. Utilizar transporte público")
        print("4. Economizar em educação")
        print("5. Reduzir gastos com entretenimento")
        print("6. Reduzir todos os gastos em um valor percentual personalizado")
        print("7. Reduzir um gasto específico em um valor percentual personalizado")
        print("0. Sair")

        while True:
            opcao = input("Escolha uma opção (1 a 7) ou digite '0' para sair: ")

            if opcao == '1':
                novo_valor_internet = self.obter_valor_numerico("Digite o novo valor da internet: ")
                economia_internet = self.gastos['internet'] - novo_valor_internet
                self.gastos['internet'] = novo_valor_internet
                self.total_gastos -= economia_internet
                print("Total de gastos mensais com a alteração: R$", self.total_gastos)
            elif opcao == '2':
                economia_alimentacao = self.gastos['alimentacao'] * 0.2
                self.gastos['alimentacao'] -= economia_alimentacao
                self.total_gastos -= economia_alimentacao
                print("Total de gastos mensais com a alteração: R$", self.total_gastos)
            elif opcao == '3':
                economia_transporte = self.gastos['transporte'] * 0.3
                self.gastos['transporte'] -= economia_transporte
                self.total_gastos -= economia_transporte
                print("Total de gastos mensais com a alteração: R$", self.total_gastos)
            elif opcao == '4':
                economia_educacao = self.gastos['educacao'] * 0.15
                self.gastos['educacao'] -= economia_educacao
                self.total_gastos -= economia_educacao
                print("Total de gastos mensais com a alteração: R$", self.total_gastos)
            elif opcao == '5':
                economia_entretenimento = self.gastos['entretenimento'] * 0.25
                self.gastos['entretenimento'] -= economia_entretenimento
                self.total_gastos -= economia_entretenimento
                print("Total de gastos mensais com a alteração: R$", self.total_gastos)
            elif opcao == '6':
                percentual = self.obter_valor_numerico("Digite o percentual de redução (ex: 10 para 10%): ")
                economia_total = self.total_gastos * (percentual / 100)
                for categoria in self.gastos:
                    economia = self.gastos[categoria] * (percentual / 100)
                    self.gastos[categoria] -= economia
                self.total_gastos -= economia_total
                print("Total de gastos mensais com a alteração: R$", self.total_gastos)
            elif opcao == '7':
                categoria = input("Digite a categoria de gasto que deseja reduzir: ")
                if categoria in self.gastos:
                    while True:
                        percentual = input("Digite o percentual de redução (ex: 10 para 10%): ")
                        try:
                            percentual = float(percentual)
                            if percentual < 0 or percentual > 100:
                                print("Percentual inválido. O valor deve estar entre 0 e 100.")
                            else:
                                break
                        except ValueError:
                            print("Percentual inválido. Tente novamente.")
                    self.reduzir_valor_gasto(categoria, percentual)
                    print("Total de gastos mensais com a alteração: R$", self.total_gastos)
                else:
                    print("Categoria de gasto inválida. Tente novamente.")
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

        print("Programa encerrado.")

    def reduzir_gastos_sugerir(self):
        economia_total = self.total_gastos * 0.1
        for categoria in self.gastos:
            economia = self.gastos[categoria] * 0.1
            self.gastos[categoria] -= economia
        self.total_gastos -= economia_total

        print("----- Redução de Gastos Sugerida -----")
        print("Você pode reduzir todos os gastos em 10% para economizar.")
        print(f"Total de gastos mensais com a redução sugerida: R$ {self.total_gastos:.2f}")

    def adicionar_gasto(self):
        categoria = input("Digite o nome da nova categoria de gasto: ")
        valor = self.obter_valor_numerico(f"Digite o valor de {categoria}: ")
        self.gastos[categoria] = valor
        self.total_gastos += valor

        print(f"Gasto {categoria} adicionado com sucesso!")

    def remover_gasto(self):
        categoria = input("Digite o nome da categoria de gasto que deseja remover: ")
        if categoria in self.gastos:
            valor = self.gastos.pop(categoria)
            self.total_gastos -= valor
            print(f"Gasto {categoria} removido com sucesso!")
        else:
            print("Categoria de gasto inválida. Tente novamente.")

    def exibir_categorias(self):
        print("----- Categorias de Gastos -----")
        for categoria in self.gastos:
            print(categoria.replace('_', ' '))

    def executar_opcao(self, opcao):
        if opcao == '1':
            self.adicionar_gasto()
        elif opcao == '2':
            self.remover_gasto()
        elif opcao == '3':
            self.exibir_categorias()
        else:
            print("Opção inválida. Tente novamente.")

    def menu_opcoes(self):
        print("----- Opções -----")
        print("1. Adicionar um novo gasto")
        print("2. Remover um gasto existente")
        print("3. Exibir categorias de gastos")
        print("0. Sair")

        while True:
            opcao = input("Escolha uma opção (1 a 3) ou digite '0' para sair: ")
            if opcao == '0':
                break
            else:
                self.executar_opcao(opcao)


def calcular_gastos_mensais():
    gastos_mensais = GastosMensais()

    for categoria in gastos_mensais.gastos:
        mensagem = f"Digite o valor de {categoria.replace('_', ' ')}: "
        gastos_mensais.gastos[categoria] = gastos_mensais.obter_valor_numerico(mensagem)

    gastos_mensais.calcular_total_gastos()
    gastos_mensais.exibir_gastos()
    gastos_mensais.alterar_gastos()
    gastos_mensais.reduzir_gastos_sugerir()
    gastos_mensais.menu_opcoes()


calcular_gastos_mensais()from decimal import Decimal, ROUND_HALF_UP


def criar_carteira(quantia_investimento):
    carteira = [
        {"nome": "Ações", "taxa_mensal": Decimal("0.05")},
        {"nome": "Títulos do governo", "taxa_mensal": Decimal("0.03")},
        {"nome": "Fundos imobiliários", "taxa_mensal": Decimal("0.04")},
        {"nome": "Criptomoedas", "taxa_mensal": Decimal("0.1")},
        {"nome": "Fundos de renda fixa", "taxa_mensal": Decimal("0.02")},
        {"nome": "Commodities", "taxa_mensal": Decimal("0.06")}
    ]

    carteira_ordenada = sorted(carteira, key=lambda x: x["taxa_mensal"], reverse=True)

    total_taxa_mensal = sum(investimento["taxa_mensal"] for investimento in carteira_ordenada)

    for investimento in carteira_ordenada:
        peso = investimento["taxa_mensal"] / total_taxa_mensal
        quantia_investida = quantia_investimento * peso
        investimento["quantia_investida"] = quantia_investida.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
        investimento["retorno_mensal"] = (quantia_investida * investimento["taxa_mensal"]).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)

    return carteira_ordenada


def tomar_decisao_investimento(carteira, valor_disponivel):
    carteira_ordenada = sorted(carteira, key=lambda x: x["retorno_mensal"], reverse=True)

    alocacoes = {}

    for investimento in carteira_ordenada:
        quantia_investida = min(valor_disponivel, investimento["quantia_investida"])
        alocacoes[investimento["nome"]] = quantia_investida
        valor_disponivel -= quantia_investida

        if valor_disponivel <= 0:
            break

    return alocacoes


lucro_total_mensal = Decimal("0")

while True:
    quantia_investimento = Decimal(input("Digite a quantia que deseja investir: "))
    precisao = int(input("Digite a quantidade de casas decimais desejada: "))

    carteira = criar_carteira(quantia_investimento)

    alocacoes = tomar_decisao_investimento(carteira, quantia_investimento)

    lucro_mensal = Decimal("0")

    print("Sua carteira de investimentos:")
    for investimento, quantia_investida in alocacoes.items():
        investimento_info = next(item for item in carteira if item["nome"] == investimento)
        nome = investimento_info["nome"]
        taxa_mensal = investimento_info["taxa_mensal"]
        retorno_mensal = (quantia_investida * taxa_mensal).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
        lucro_mensal += retorno_mensal

        print(f"Nome: {nome}")
        print(f"Taxa mensal: {taxa_mensal * 100:.2f}%")
        print(f"Quantia investida: R$ {quantia_investida:.{precisao}f}")
        print(f"Retorno mensal: R$ {retorno_mensal:.{precisao}f}")
        print("---------------------------")

    lucro_total_mensal += lucro_mensal
    print(f"Lucro total mensal: R$ {lucro_mensal:.{precisao}f}")
    print("---------------------------")

    continuar = input("Deseja realizar outro investimento? (s/n): ")
    if continuar.lower() != "s":
        break

print(f"Lucro total acumulado: R$ {lucro_total_mensal:.{precisao}f}")
def calcular_preco_venda(investimento):
    preco_venda = investimento * 1.5
    return preco_venda

def calcular_custo_anuncio(investimento):
    custo_anuncio = investimento * 0.2
    return custo_anuncio

def calcular_custo_manutencao(investimento):
    custo_manutencao = investimento * 0.1
    return custo_manutencao

def calcular_popularidade(investimento):
    popularidade = investimento * 0.05
    return popularidade

def calcular_extensao(investimento):
    extensao = investimento * 0.03
    return extensao

def calcular_custo_total_forma_venda(investimento):
    custo_total = (
        calcular_custo_anuncio(investimento)
        + calcular_custo_manutencao(investimento)
    )
    return custo_total

def calcular_custo_total_todas_formas_venda(investimentos):
    custo_total_todas_formas = sum(investimentos)
    return custo_total_todas_formas

def obter_valor_investimento():
    while True:
        try:
            print("f-----------------------------------------------------f")
            valor = float(input("Digite o valor de investimento: "))
            if valor <= 0:
                print("O valor de investimento deve ser maior que zero. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")

def obter_nome_forma_venda(indice):
    while True:
        forma_venda = input("Digite o nome da forma de venda {}: ".format(indice))
        if forma_venda:
            return forma_venda
        else:
            print("Nome da forma de venda inválido. Tente novamente.")

num_formas_venda = 0
investimentos = []
formas_venda = []

while True:
    try:
        print("//////////////////////////////////////////")
        num_formas_venda = int(input("Digite o número de formas de venda em que deseja investir: "))
        if num_formas_venda <= 0:
            print("O número de formas de venda deve ser maior que zero. Tente novamente.")
        else:
            break
    except ValueError:
        print("Número inválido. Tente novamente.")

for i in range(1, num_formas_venda + 1):
    print("\nInformações da forma de venda", i)
    investimento = obter_valor_investimento()
    forma_venda = obter_nome_forma_venda(i)
    investimentos.append(investimento)
    formas_venda.append(forma_venda)

print("\nResultados:")

for i in range(num_formas_venda):
    investimento = investimentos[i]
    forma_venda = formas_venda[i]

    preco_venda = calcular_preco_venda(investimento)
    custo_anuncio = calcular_custo_anuncio(investimento)
    custo_manutencao = calcular_custo_manutencao(investimento)
    popularidade = calcular_popularidade(investimento)
    extensao = calcular_extensao(investimento)
    custo_total = calcular_custo_total_forma_venda(investimento)

    print("\nForma de venda:", forma_venda)
    print("Preço de venda:", "{:.2f}".format(preco_venda))
    print("Custo de anúncio:", "{:.2f}".format(custo_anuncio))
    print("Custo de manutenção:", "{:.2f}".format(custo_manutencao))
    print("Popularidade:", "{:.2f}".format(popularidade))
    print("Extensão:", "{:.2f}".format(extensao))
    print("Custo total:", "{:.2f}".format(custo_total))

custo_total_todas_formas = calcular_custo_total_todas_formas_venda(investimentos)
print("\nCusto total de todas as formas de venda:", "{:.2f}".format(custo_total_todas_formas))

print("Fim do programa")