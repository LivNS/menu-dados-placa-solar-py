''' Debora da Silva Amaral RM 550412
    Levy Nascimento Junior RM 98655
    Lívia Namba Seraphim RM 97819
    Mateus Iago Sousa Conceição RM 550270
    Sarah Ribeiro da Silva RM 97747'''

# Dados iniciais
energia_produzida_diaria = 0
co2_produzido = 0
energia_no_painel = 0
capacidade_painel = 1000

# Lista para armazenar dados da semana
dados_semana = []

# Contador de dias inseridos
dias_inseridos = 0

# Função para calcular a produção de CO2 com base na energia produzida
def calcular_co2(energia_produzida):
    return energia_produzida * 0.5  # Suponha que cada 1 watt produza 0.5 kg de CO2

# Função para exibir os dados diários
def exibir_dados_diarios():
    print(f"Energia produzida diariamente: {energia_produzida_diaria} watts")
    print(f"CO2 produzido: {co2_produzido} kg")
    print(f"Energia no painel: {energia_no_painel} watts")
    print(f"Capacidade do painel: {capacidade_painel} watts")

# Função para registrar os dados da semana
def registrar_dados_diarios(producao_diaria):
    global energia_produzida_diaria, co2_produzido, energia_no_painel, dias_inseridos
    energia_produzida_diaria += producao_diaria
    co2_produzido += calcular_co2(producao_diaria)
    energia_no_painel += producao_diaria
    dias_inseridos += 1
    dados_semana.append((producao_diaria, calcular_co2(producao_diaria)))
    if dias_inseridos >= 7:
        print("Dados da semana registrados com sucesso.")
    else:
        print(f"Ainda é necessário inserir mais {7 - dias_inseridos} dias para visualizar os dados semanais.")

# Função para exibir os dados semanais
def exibir_dados_semanais():
    if not dados_semana:
        print("Nenhum dado semanal registrado ainda.")
        return

    semana = len(dados_semana)
    energia_total = sum([dados[0] for dados in dados_semana])
    co2_total = sum([dados[1] for dados in dados_semana])

    print(f"Resumo da semana {semana}:")
    print(f"Energia produzida na semana: {energia_total} watts")
    print(f"CO2 produzido na semana: {co2_total} kg")

while True:
    print("\n**** Menu ****")
    print("1. Registrar produção diária")
    print("2. Exibir dados diários")
    print("3. Exibir dados semanais")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        producao_diaria_str = input("Digite a quantidade de energia produzida diariamente (watts): ")
        producao_diaria_str = ''.join(filter(str.isdigit, producao_diaria_str))
        if producao_diaria_str:
            producao_diaria = float(producao_diaria_str)
            if producao_diaria >= 0:
               registrar_dados_diarios(producao_diaria)
            else:
                print("A produção diária deve ser maior ou igual a zero.")
        else:
            print("Entrada inválida. Digite apenas números.")

    elif escolha == "2":
        exibir_dados_diarios()
    elif escolha == "3":
        if dias_inseridos >= 7:
            exibir_dados_semanais()
        else:
            print(f"Ainda é necessário inserir mais {7 - dias_inseridos} dias para visualizar os dados semanais.")
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Programa encerrado.")
