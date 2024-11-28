# Projeto de Web Scraping de Citações Famosas

Este repositório contém um projeto simples de web scraping desenvolvido em Python utilizando as bibliotecas **Requests**, **BeautifulSoup4**, e **CSV**. O objetivo é acessar o site [Quotes to Scrape](http://quotes.toscrape.com), extrair citações e seus respectivos autores, e salvar essas informações em um arquivo CSV. Este projeto é ideal para iniciantes que desejam aprender a trabalhar com web scraping e manipulação de arquivos em Python.

## Tecnologias Utilizadas

- **Python**
- **Requests**: Para fazer requisições HTTP e acessar o conteúdo do site.
- **BeautifulSoup4**: Para analisar e extrair informações do HTML.
- **CSV**: Para salvar os dados coletados em um arquivo CSV.

## Funcionalidades

- **Acessar uma página web** e obter o código HTML.
- **Extrair citações e seus respectivos autores** do site "Quotes to Scrape".
- **Salvar as citações e autores em um arquivo CSV** de maneira organizada.

## Como Este Projeto Pode Ser Útil

- **Aprendizado de Web Scraping**: Este projeto é uma introdução perfeita ao web scraping para quem está começando. Ele demonstra como acessar uma página da web, entender o HTML e extrair as informações desejadas.
- **Automatização de Coleta de Dados**: A técnica mostrada aqui pode ser expandida para outros sites (respeitando sempre os termos de uso), ajudando a automatizar a coleta de informações.
- **Manipulação de Dados com CSV**: Aprende-se a manipular e salvar dados no formato CSV, que é um formato amplamente utilizado para intercâmbio de dados entre sistemas.

## Como Usar o Projeto

### Pré-requisitos

- **Python 3** instalado na máquina.
- Instalar as bibliotecas necessárias:
  ```sh
  pip install requests
  pip install beautifulsoup4
  ```

### Execução

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/web-scraping-citacoes.git
   ```

2. Navegue até a pasta do projeto:
   ```sh
   cd web-scraping-citacoes
   ```

3. Execute o script Python:
   ```sh
   python scrap_citacoes.py
   ```

4. Após a execução, o arquivo **citacoes.csv** será gerado no diretório do projeto, contendo as citações e autores extraídos.

## Estrutura do Repositório

- **scrap_citacoes.py**: Script Python que realiza o web scraping e salva os dados em um CSV.
- **citacoes.csv**: Arquivo gerado que contém as citações e os autores.

## Observações

- Respeite os termos de uso dos sites. Muitos sites não permitem scraping ou limitam o acesso automático. O site "Quotes to Scrape" é feito para prática, mas isso nem sempre é o caso em outros sites.
- Este projeto foi desenvolvido para fins educacionais e não deve ser usado para atividades que violem as leis de privacidade ou os termos de uso dos sites.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests** com melhorias.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

