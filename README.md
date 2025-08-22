# Criador de Subpastas por Diretório

Este projeto fornece um script simples em Python para automatizar a criação de uma subpasta com nome definido pelo usuário (como `projetos`, por exemplo) dentro de cada pasta existente em um diretório principal. É útil para organizar documentos antigos ou preparar uma estrutura de arquivamento padronizada.

## Funcionalidades

- Percorre todas as pastas em um diretório principal
- Cria automaticamente uma nova subpasta (com nome definido pelo usuário) em cada pasta encontrada
- Verifica se a subpasta já existe antes de criar, evitando duplicações

## Tecnologias utilizadas

- Python 3 (nenhuma biblioteca externa é necessária)

## Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/estelamaillo/automacao_arquivos.git

2. Abra o arquivo Python (ex: `nova_subpasta.py`) e edite:

   - O caminho da variável `pasta_principal`
   - O nome da subpasta que deseja criar (ex: `projetos`)

3. Execute o script:
    ```bash
   python nova_subpasta.py

## Contribuições

Este é um utilitário simples e direto. Sugestões são bem-vindas via pull request ou issue.
