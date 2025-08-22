import os

# Caminho da pasta principal onde estão as pastas dos clientes
pasta_principal = r'C:\caminho\para\sua\pasta'  # Substitua pelo caminho real

# Percorre todos os itens dentro da pasta principal
for nome_pasta in os.listdir(pasta_principal):
    caminho_pasta = os.path.join(pasta_principal, nome_pasta)

    # Verifica se é uma pasta (e não um arquivo)
    if os.path.isdir(caminho_pasta):
        caminho_subpasta = os.path.join(caminho_pasta, 'NOME_DA_SUBPASTA')

        # Cria a pasta 'NOME_DA_SUBPASTA' se ela ainda não existir
        if not os.path.exists(caminho_subpasta):
            os.makedirs(caminho_subpasta)
            print(f'Criada pasta NOME_DA_SUBPASTA em: {caminho_subpasta}')
        else:
            print(f'A pasta NOME_DA_SUBPASTA já existe em: {caminho_subpasta}')