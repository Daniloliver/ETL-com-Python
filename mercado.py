# Dados de um sistema de Supermercado

supermercado = {
    "Bebidas": [
        {"Item": "Água Mineral", "Preço": 2.00, "Quantidade em Estoque": 100},
        {"Item": "Refrigerante Cola", "Preço": 4.50, "Quantidade em Estoque": 50},
        {"Item": "Suco de Laranja", "Preço": 3.00, "Quantidade em Estoque": 75},
        {"Item": "Cerveja", "Preço": 5.50, "Quantidade em Estoque": 40},
        {"Item": "Vinho Tinto", "Preço": 12.99, "Quantidade em Estoque": 25},
    ],
    "Hortifruti": [
        {"Item": "Banana", "Preço": 1.20, "Quantidade em Estoque": 120},
        {"Item": "Maçã", "Preço": 1.50, "Quantidade em Estoque": 90},
        {"Item": "Cenoura", "Preço": 0.75, "Quantidade em Estoque": 150},
        {"Item": "Alface", "Preço": 1.00, "Quantidade em Estoque": 80},
        {"Item": "Brocolis", "Preço": 1.25, "Quantidade em Estoque": 60},
    ],
    "Laticínios": [
        {"Item": "Leite", "Preço": 2.50, "Quantidade em Estoque": 60},
        {"Item": "Manteiga", "Preço": 3.00, "Quantidade em Estoque": 40},
        {"Item": "Queijo Cheddar", "Preço": 5.25, "Quantidade em Estoque": 30},
        {"Item": "Iogurte Natural", "Preço": 1.75, "Quantidade em Estoque": 45},
        {"Item": "Ovos", "Preço": 2.00, "Quantidade em Estoque": 100},
    ],
    "Carnes": [
        {"Item": "Frango", "Preço": 6.99, "Quantidade em Estoque": 35},
        {"Item": "Carne Moída", "Preço": 8.50, "Quantidade em Estoque": 25},
        {"Item": "Peixe", "Preço": 10.99, "Quantidade em Estoque": 20},
        {"Item": "Bife", "Preço": 9.75, "Quantidade em Estoque": 30},
        {"Item": "Salsichas", "Preço": 4.25, "Quantidade em Estoque": 50},
    ],
    "Limpeza": [
        {"Item": "Sabão em Pó", "Preço": 4.00, "Quantidade em Estoque": 40},
        {"Item": "Detergente", "Preço": 2.50, "Quantidade em Estoque": 60},
        {"Item": "Limpador Multiuso", "Preço": 3.75, "Quantidade em Estoque": 30},
        {"Item": "Papel Toalha", "Preço": 1.99, "Quantidade em Estoque": 75},
        {"Item": "Esponjas de Cozinha", "Preço": 1.25, "Quantidade em Estoque": 100},
    ],
}

# Passo 1: Extract

supermercado_data = []

for categoria, itens in supermercado.items():
    for item in itens:
        data = {
            "Categoria": categoria,
            "Item": item["Item"],
            "Preço": item["Preço"],
            "Quantidade_em_Estoque": item["Quantidade em Estoque"],
        }
        supermercado_data.append(data)
        
# Passo 2: Transform
#Atualizando os preços com duas casas decimais

for data in supermercado_data:
    data["Preço"] = round(data["Preço"], 2)

# Passo 3: Load
#Colocando os dados em um arquivo .csv

import csv
nome_arquivo_csv = "supermercado.csv"

with open(nome_arquivo_csv, mode='w', newline='') as arquivo_csv:
    fieldnames = ["Categoria", "Item", "Preço", "Quantidade_em_Estoque"]
    writer = csv.DictWriter(arquivo_csv, fieldnames=fieldnames)
    
    writer.writeheader()  # Escreve o cabeçalho
    
    for data in supermercado_data:
        writer.writerow(data)
