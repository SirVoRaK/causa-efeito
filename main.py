data = [
    {
        "linguagem": "Python",
        "caracteristicas": { "facilidade": 9, "velocidade": 3, "salario": 7, "vagas": 4, "versatilidade": 6 }
    },
    {
        "linguagem": "Javascript",
        "caracteristicas": { "facilidade": 7, "velocidade": 5, "salario": 4, "vagas": 8, "versatilidade": 9 }
    },
    {
        "linguagem": "Java",
        "caracteristicas": { "facilidade": 4, "velocidade": 6, "salario": 6, "vagas": 7, "versatilidade": 4 }
    },
    {
        "linguagem": "C#",
        "caracteristicas": { "facilidade": 3, "velocidade": 7, "salario": 7, "vagas": 6, "versatilidade": 5 }
    },
    {
        "linguagem": "GoLang",
        "caracteristicas": { "facilidade": 6, "velocidade": 8, "salario": 7, "vagas": 5, "versatilidade": 3 }
    },
    {
        "linguagem": "C",
        "caracteristicas": { "facilidade": 2, "velocidade": 9, "salario": 8, "vagas": 1, "versatilidade": 2 }
    },
    {
        "linguagem": "C++",
        "caracteristicas": { "facilidade": 2, "velocidade": 9, "salario": 8, "vagas": 3, "versatilidade": 4 }
    },
    {
        "linguagem": "Rust",
        "caracteristicas": { "facilidade": 4, "velocidade": 8, "salario": 7, "vagas": 4, "versatilidade": 4 }
    },
    {
        "linguagem": "Ruby",
        "caracteristicas": { "facilidade": 6, "velocidade": 5, "salario": 5, "vagas": 2, "versatilidade": 4 }
    },
    {
        "linguagem": "Assembly",
        "caracteristicas": { "facilidade": 0, "velocidade": 10, "salario": 9, "vagas": 1, "versatilidade": 10 }
    }
]

def receber_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas números")

def solicitar_numero_dentro_intervalo(mensagem, minimo, maximo):
    while True:
        numero = receber_numero(mensagem)
        if numero >= minimo and numero <= maximo:
            return numero
        print(f"Digite números apenas entre {minimo} e {maximo}")

def solicitar_caracteristicas():
    caracteristicas = []
    for linguagem in data:
        for caracteristica in linguagem["caracteristicas"]:
            if not caracteristica in caracteristicas:
                caracteristicas.append(caracteristica)


    caracteristicas_selecionadas = []
    while True:
        print("0 - Continuar")
        for i in range(len(caracteristicas)):
            print(f"{i + 1} - {caracteristicas[i]}")

        numero = solicitar_numero_dentro_intervalo("Digite a caracteristica: ", 0, len(caracteristicas))
        if numero == 0:
            break

        caracteristicas_selecionadas.append(caracteristicas[numero - 1])
        print()

    return caracteristicas_selecionadas

def calcular_pesos(caracteristicas):
    pesos = []
    for linguagem in data:
        soma_total = 0
        soma_selecionadas = 0
        for caracteristica in linguagem["caracteristicas"]:
            valor_atual = linguagem["caracteristicas"][caracteristica]
            soma_total += valor_atual
            if caracteristica in caracteristicas:
                soma_selecionadas += valor_atual
        porcentagem = soma_selecionadas / soma_total * 100
        pesos.append({
            "linguagem": linguagem["linguagem"],
            "porcentagem": porcentagem
        })
    return pesos

def exibir_resultados(pesos):
    print()
    for peso in pesos:
        print("%s: %.1f%%"%(peso["linguagem"], peso["porcentagem"]))

# Bubble Sort para ordenar os pesos de forma decrescente a partir da porcentagem
def bubble_sort(lista):
    for _ in lista:
        for j in range(len(lista) - 1):
            if lista[j]["porcentagem"] < lista[j + 1]["porcentagem"]:
                inverter(lista, j, j + 1)

def inverter(lista, i, j):
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp

def perguntar(mensagem):
    while True:
        print()
        resposta = input(f"{mensagem} (s/n): ").lower()
        if resposta == "s" or resposta == "n":
            return resposta == "s"
        print("Digite apenas s ou n")

while True:
    caracteristicas = solicitar_caracteristicas()
    pesos = calcular_pesos(caracteristicas)
    bubble_sort(pesos)
    exibir_resultados(pesos)

    continuar = perguntar("Deseja verificar mais alguma caracteristica?")
    if not continuar:
        break

print()
print("Obrigado por usar o programa!")
