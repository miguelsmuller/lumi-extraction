# Teste Desenvolvedor Full Stack - Lumi

O projeto `Lumi Extraction` é uma das partes integrantes do monorepo `Lumi Challenge`. Esse projeto é responsável por extrair informações específicas de faturas de energia e processá-las para armazenamento em um banco de dados PostgreSQL.

## **Monorepo e Projetos Relacionados**

- **[Monorepo Lumi Challenge](https://github.com/miguelsmuller/lumi-challenge)**
  
- **[Lumi Back](https://github.com/miguelsmuller/lumi-back)**

- **[Lumi Front](https://github.com/miguelsmuller/lumi-front)**

## **Aspectos Técnicos**

- A biblioteca `pdfplumber` é utilizada para a extração precisa de dados de faturas de energia no formato PDF.
- A arquitetura do projeto foi cuidadosamente planejada e implementada para garantir escalabilidade, manutenção e desempenho.
- O projeto faz uso do `PostgreSQL` para armazenar e gerenciar as informações extraídas das faturas de energia.
- O `SQLAlchemy` é adotado como ORM para facilitar a interação com o PostgreSQL, proporcionando uma camada de abstração robusta e eficiente.


## **Estrutura do Projeto**
```
.
├── app
│   ├── __main__.py
│   ├── tasks
│   │    └── Extraction.py
│   ├── dtos
│   │   └── EnergyInvoiceDTO.py
│   ├── models
│   │   └── EnergyInvoiceModel.py
│   ├── services
│   │   ├── ExportToJSON.py
│   │   ├── ExportToPostgreSQL.py
│   │   ├── ExtractFromAI.py
│   │   ├── ExtractFromCroppedImage.py
│   │   ├── ExtractFromJSON.py
│   │   ├── ExtractFromString.py
│   │   ├── IExport.py
│   │   └── IExtract.py
│   └── config
│       ├── ArgumentParser.py
│       └── DataBaseManager.py
├── .flake8
├── .gitignore
├── .pylintrc
├── .python-version
├── Makefile
├── pyrightconfig.json
├── README.md
└── requirements.txt
```

## **Makefile do Projeto**

O Makefile desse projeto inclui as seguintes metas:

- `help`: Exibe uma lista de todos os comandos disponíveis neste Makefile.
- `setup`: Instala as dependências listadas no arquivo requirements.txt.
- `extraction`: Inicia o processo de extração usando o script Python, especificando o diretório de entrada e saída.
- `build-image`: Constrói uma imagem Docker para o projeto.
- `run-image`: Inicia um contêiner Docker com o projeto em execução.
- `stop-image`: Para e remove o contêiner Docker do projeto.
- `tag-image`: Adiciona uma tag à imagem Docker.
- `publish-image`: Publica a imagem Docker em um registro (é necessário configurar o registro).


## **Rodando Localmente**

Para executar a extração de dados localmente, utilize os seguintes comandos:

```bash
python app --extraction --input "caminho/para/diretorio" --output "caminho/para/saida"
```

ou, se preferir:

```bash
make extraction
```
