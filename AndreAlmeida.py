# Valor fixo cobrado por cada hora de trabalho
TAXA_HORARIA = 25.0

def ler_dados(nome_ficheiro):
    dados = [] # Lista vazia para guardar a informação
    
    try:
        # Tenta abrir o ficheiro em modo de leitura ('r')
        with open (nome_ficheiro , 'r', encoding='utf-8') as ficheiro:
            
            # Percorre o ficheiro linha a linha
            for linha in ficheiro:
                # Limpa espaços extra e corta a frase onde houver uma vírgula
                partes = linha.strip().split(',')
                
                # Garante que a linha tem exatamente 2 pedaços (Nome do Projeto e Horas)
                if len(partes) == 2:
                    nome_projeto = partes[0].strip() # 1ª parte é o nome
                    horas = float(partes[1].strip()) # 2ª parte são as horas (convertidas para número decimal)
                    
                    # Adiciona o nome e as horas à nossa lista de dados
                    dados.append((nome_projeto, horas))
                    
    # Se o ficheiro não existir, apanha o erro e avisa o utilizador
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{nome_ficheiro}' não foi encontrado.")
    # Se as horas não forem números (ex: texto), apanha o erro
    except ValueError:
        print(f"Erro: O ficheiro '{nome_ficheiro}' contém dados inválidos.")
        
    return dados # Devolve a lista preenchida (ou vazia, se deu erro)

def calcular_custos_totais(dados, taxa):
    totais_por_projeto = {} # Dicionário para ir acumulando os custos
    
    # Passa por cada registo da nossa lista
    for nome_projeto, horas in dados:
        custo_tarefa = horas * taxa # Calcula o valor daquela tarefa
        
        # Se o projeto já existe no dicionário, junta este novo valor ao que já lá estava
        if nome_projeto in totais_por_projeto:
            totais_por_projeto[nome_projeto] += custo_tarefa
        # Se é a primeira vez que vemos este projeto, guardamos este primeiro valor
        else:
            totais_por_projeto[nome_projeto] = custo_tarefa
            
    return totais_por_projeto

def exibir_relatorio(custos):
    print("Relatório de Custos por Projeto:")
    
    # Se o dicionário estiver vazio, avisa e sai da função
    if not custos:
        print("Nenhum dado disponível para exibir.")
        return
        
    # Percorre o dicionário e imprime cada projeto e o seu total
    for projeto, total in custos.items():
        # O :.2f serve para obrigar o número a ter sempre 2 casas decimais (ex: 25.50 em vez de 25.5)
        print(f"{projeto}: {total:.2f}€")

def main():
    # 1. Definir qual é o ficheiro a ler
    ficheiro_entrada = "horas_projetos.txt"
    
    # 2. Ler os dados chamando a primeira função
    dados_lidos = ler_dados(ficheiro_entrada)
    
    # 3. Se conseguiu ler os dados (se a lista não estiver vazia)
    if dados_lidos:
        # Faz os cálculos
        custos_finais = calcular_custos_totais(dados_lidos, TAXA_HORARIA)
        # Mostra o relatório
        exibir_relatorio(custos_finais)

# Este é o "motor de arranque" do Python. 
# Garante que o programa só arranca se formos nós a executá-lo diretamente.
if __name__ == "__main__":  
    main()