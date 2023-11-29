# Web Scraper de Termos de Jogos

Este projeto consiste em um script Python que faz web scraping de nomes de jogos de várias páginas do site 1337, um site de download confiado e verificado pela comunidade de cracking do Reddit. O script realiza pesquisas automáticas no YouTube para cada jogo, facilitando a atualização sobre os jogos mais populares e visualizações de gameplay.

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
