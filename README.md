# Repositório de Teste da API OpenAI - myGpt

## Descrição

Este é um projeto pessoal desenvolvido por João Antônio Nardini Romaniello. O objetivo deste repositório é fornecer exemplos de como interagir com a API OpenAI usando o modelo de linguagem GPT-3. O projeto está estruturado em duas classes principais:

- `imageGPT`: Esta classe é responsável por gerar uma imagem baseada em um prompt fornecido pelo usuário.
- `textGPT`: Esta classe atua de maneira semelhante ao ChatGPT, com a diferença de que é possível ajustar o temperamento e guiar como o modelo deve agir inicialmente.

## Requisitos

- Python 3.7+
- Biblioteca `openai`

## Instalação

Primeiro, clone o repositório:

```bash
git clone https://github.com/joaoromaniello/myGpt.git
cd myGpt
```

Em seguida, instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Certifique-se de definir a variável de ambiente `OPENAI_API_KEY` com sua chave API do OpenAI.

Para executar o script principal, use o seguinte comando:

```bash
python main.py
```

Este script irá interagir com a API OpenAI e produzirá resultados baseados no modelo de linguagem GPT-3.

## Contribuições

Contribuições são bem-vindas! Por favor, leia as [regras de contribuição](CONTRIBUTING.md) antes de fazer qualquer alteração.

