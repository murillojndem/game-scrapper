# Web Scraper de Jogos no 1337

Este projeto consiste em um script Python que faz web scraping de nomes de jogos de várias páginas do site 1337, um site de download confiado e verificado pela comunidade de cracking do Reddit. O script realiza pesquisas automáticas no YouTube para cada jogo, facilitando a atualização sobre os jogos mais populares e visualizações de gameplay.

## Estrutura do Projeto

O projeto está dividido nos seguintes arquivos:

- `main.py`: Ponto de entrada do programa. Coordena o processo de scraping e o tratamento dos termos pesquisados.
- `scraper.py`: Contém toda a lógica de web scraping, incluindo a extração de nomes de jogos das páginas e a pesquisa no YouTube.
- `utils.py`: Funções auxiliares para carregar e salvar os termos pesquisados em um arquivo `.txt`.


## Funcionalidades

- **Web Scraping Eficiente:** Utiliza sessões do `requests` para otimizar as solicitações HTTP e `BeautifulSoup` para análise dos dados.
- **Logging e Tratamento de Exceções:** Implementação robusta de logging e tratamento de exceções para melhor depuração e confiabilidade.
- **Manipulação de Arquivos:** Gerenciamento eficiente de arquivos `.txt` para armazenar termos de pesquisa.
- **Automatização de Pesquisas no YouTube:** Abre automaticamente pesquisas no YouTube com base nos termos raspados.


## Instalação

Para instalar as dependências necessárias, execute os seguintes comandos no console:

```bash
pip install requests
pip install beautifulsoup4
```

## Uso

Para executar o script, certifique-se de que todas as dependências estejam instaladas e execute o arquivo principal do projeto. O script irá automaticamente fazer web scraping dos nomes dos jogos, filtrar conforme especificado, e realizar pesquisas no YouTube.

## Aviso sobre Uso de Memória RAM

**Disclaimer**: A execução deste programa pode consumir uma quantidade significativa de memória RAM, especialmente se estiver processando uma grande quantidade de dados. Certifique-se de que seu sistema tenha recursos suficientes para executá-lo de maneira eficiente.


