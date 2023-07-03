# Repositório de Teste da API OpenAI - myGpt

## Descrição

Este é um projeto pessoal desenvolvido por João Antônio Nardini Romaniello. O objetivo deste repositório é fornecer exemplos de como interagir com a API OpenAI usando o modelo de linguagem GPT-3. O projeto está estruturado em duas classes principais:

- `imageGPT`: Esta classe é responsável por gerar uma imagem baseada em um prompt fornecido pelo usuário.
- `textGPT`: Esta classe atua de maneira semelhante ao ChatGPT, com a diferença de que é possível ajustar o temperamento e guiar como o modelo deve agir inicialmente.


### Chat
Na tela de chat, os usuários podem digitar mensagens em um campo de entrada e receber respostas geradas pelo modelo GPT-3. A interface exibe as mensagens em um chat convencional, onde as mensagens do usuário são exibidas em verde e as respostas do GPT-3 em azul.

Além disso, há um botão "Selecionar Arquivo" que permite aos usuários fazer upload de arquivos de texto (como arquivos JSON ou TXT) da pasta "local_files". O conteúdo desses arquivos é analisado pelo GPT-3 e utilizado para gerar respostas mais adequadas.

### Geração de Imagens
Na tela de geração de imagens, os usuários podem inserir um texto ou prompt de entrada e o modelo GPT-3 irá gerar uma imagem com base nesse prompt. Após inserir o texto, basta clicar no botão "Gerar Imagem" para visualizar a imagem gerada.

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

Para executar os scripts , use o seguinte comando:

```bash
python textGPT.py
```

Esse scripts lhe apresentará uma interface com as funções do e especificações do projeto


