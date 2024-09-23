#pyenv local 3.12.1
#poetry init
#poetry shell
#criar .gitignore (.venv)

import pandas as pd
from sqlalchemy import create_engine

# Caminho para o arquivo CSV e o arquivo JSON de saída
csv_file = r'C:\Jornada\Olimpyc_Games\data\olympics_dataset.csv'
json_file = r'C:\Jornada\Olimpyc_Games\data\olympics_dataset.json'

# Ler o arquivo CSV
df = pd.read_csv(csv_file)
df_json = pd.read_json(json_file)

# Converter o DataFrame para JSON e salvar o arquivo
df.to_json(json_file, orient='records', indent=4)


engine = create_engine('postgresql://postgres:admin@localhost:5432/Olympic_games')
#Importar arquivo Json para o database.
#df_json.to_sql('olympics_dataset', engine, if_exists='append', index=False)
df.to_sql('olympics_dataset', engine, if_exists='append', index=False)

print("Importação completada com sucesso!")
