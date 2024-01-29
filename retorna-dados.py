import subprocess
import json
import sys

# python3 teste.py "response.infos[0].envGroups"

# Obtenha o caminho do campo desejado do argumento de linha de comando
field_path = sys.argv[1]

# Substitua 'ls' pelo comando que você deseja executar
command = '/home/ubuntu/jelastic/environment/control/getenvs --silent true'

# Execute o comando
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Analise a saída como JSON
output_json = json.loads(result.stdout)

# Acesse o campo especificado
field_value = output_json
try:
    for field in field_path.split('.'):
        if "[" in field:
            index = int(field.split("[")[1].replace("]", ""))
            field = field.split("[")[0]
            field_value = field_value[field][index]
        else:
            field_value = field_value[field]
    # Imprima o valor do campo especificado
    print(field_value)
except (KeyError, IndexError) as e:
    print(f"O campo '{field_path}' não foi encontrado no JSON retornado.")
