def remover_barra_invertida_json(arquivo_entrada, arquivo_saida):
    # Abrir o arquivo JSON de entrada e o arquivo JSON de saída
    with open(arquivo_entrada, 'r', encoding='utf-8') as entrada_json, \
         open(arquivo_saida, 'w', encoding='utf-8') as saida_json:

        # Ler o arquivo linha por linha
        for linha in entrada_json:
            # Remover a barra invertida de cada linha
            linha_limpa = linha.replace('\\', '')
            # Escrever a linha modificada no arquivo de saída
            saida_json.write(linha_limpa)

# Exemplo de uso
arquivo_entrada = 'C:\Jornada\Olimpyc_Games\data\olympics_dataset.json'
arquivo_saida = 'C:\Jornada\Olimpyc_Games\data\olympics_dataset_replace.json'

remover_barra_invertida_json(arquivo_entrada, arquivo_saida)

print("Barra invertida removida com sucesso!")
