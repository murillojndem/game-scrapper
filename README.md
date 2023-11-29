# Web Scraper de Termos de Jogos

Este projeto consiste em um script Python que faz web scraping de nomes de jogos de várias páginas do site 1337, um site de download confiado e verificado pela comunidade de cracking do Reddit. O script realiza pesquisas automáticas no YouTube para cada jogo, facilitando a atualização sobre os jogos mais populares e visualizações de gameplay.

## Estrutura do Projeto

O projeto está dividido nos seguintes arquivos:

- `main.py`: Ponto de entrada do programa. Coordena o processo de scraping e o tratamento dos termos pesquisados.
- `scraper.py`: Contém toda a lógica de web scraping, incluindo a extração de nomes de jogos das páginas e a pesquisa no YouTube.
- `utils.py`: Funções auxiliares para carregar e salvar os termos pesquisados em um arquivo `.txt`.


## Funcionalidades

- **Web Scraping de Dados de Múltiplas Páginas do Site 1337:** O script faz web scraping de nomes de jogos de várias páginas, incluindo listas de jogos populares e tendências.
- **Filtragem de Termos:** Remove termos específicos dos nomes dos jogos, como números de versão e a palavra "update".
- **Pesquisa Automática no YouTube:** Para cada jogo encontrado, o script abre uma nova aba no navegador Chrome com a pesquisa de gameplay do jogo no YouTube.
- **Prevenção de Pesquisas Repetidas:** Mantém um registro dos jogos já pesquisados em um arquivo `.txt`, evitando pesquisas repetidas.
- **Armazenamento de Termos Pesquisados:** Salva os termos pesquisados em um arquivo `.txt` para referência em execuções futuras.
- **Notificação de Termos já Pesquisados:** Notifica no console se todos os termos já foram pesquisados anteriormente.

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


