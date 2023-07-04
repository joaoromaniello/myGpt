import os
from tkinter import filedialog

import openai
import requests
import json
import tkinter as tk

import variables

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

API_KEY = variables.API_KEY
openai.api_key = variables.API_KEY

messages = [
    {"role": "system",
     "content": "oVocê será um robô capaz de responder com exatidão às minhas perguntas.Além diss, você vai ser capaz de analisar dados sem precisar de contexto envolvido"}
]

def fetchDataFromFolder(arq):
    folder_path = "local_files"  # Caminho da pasta que contém o arquivo
    file_path = os.path.join(folder_path, arq)  # Caminho completo do arquivo

    with open(file_path, "r") as file:
        data = file.read()

    return data

def generate_chat_completion(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

def create_instructions_window():

    instruction_text = """
1. Texto:
- Use a tela de chat para interagir com o GPT.
- Clique em "Enviar Arquivo" para upload de json, txt, etc. (certifique-se de que estejam na pasta "local_files").
- O GPT analisa e responde com base no conteúdo do arquivo.

2. Imagem:

- Insira o prompt de texto na tela de geração de imagens.
- Clique em "Gerar Imagem" e a aplicação criará uma imagem a partir do texto.
    """


    window = tk.Toplevel()
    window.title("Instruções")
    lbl = tk.Label(window, text=instruction_text,anchor='w',width=90)
    lbl.pack(fill='both')

def reset_messages():
    global messages
    messages = [
        {"role": "system",
         "content": "Você será um robô capaz de responder com exatidão às minhas perguntas. Além disso, você será capaz de analisar dados sem precisar de contexto envolvido"}
    ]

def create_CPC():
    window = tk.Tk()
    window.title("My GPT")

    def select_file():
        file_path = filedialog.askopenfilename(initialdir=".", title="Selecione um arquivo", filetypes=(
            ("Arquivos de Texto", "*.txt"), ("Arquivos JSON", "*.json"), ("Todos os arquivos", "*.*")))
        if file_path:
            user_input.delete(0, tk.END)
            file_string = f"Arquivo  {file_path} enviado\n"
            user_input.insert(tk.END,file_string)

            # Ler o conteúdo do arquivo
            with open(file_path, "r") as file:
                file_content = file.read()

            mensagem = {"role": "user", "content": file_content}
            messages.append(mensagem)
            send_file_message(file_string)
    def send_file_message(string):
        user_input.delete(0, tk.END)

        chat_textbox.config(state="normal")
        chat_textbox.insert(tk.END, "Você: " + string + "\n", "green")
        chat_textbox.config(state="disabled")

        response = generate_chat_completion(messages)
        chat_textbox.config(state="normal")
        chat_textbox.insert(tk.END, "GPT: " + response + "\n", "blue")
        chat_textbox.config(state="disabled")

        chat_textbox.see(tk.END)

        num_lines = chat_textbox.get("1.0", tk.END).count("\n")
        if num_lines > 100:
            chat_textbox.delete("1.0", "2.0")
    def send_message(event=None):
        message = user_input.get()
        mensagem = {"role": "user", "content": message}
        messages.append(mensagem)
        user_input.delete(0, tk.END)

        # Atualizando o chat_textbox com a mensagem do usuário
        chat_textbox.config(state="normal")
        chat_textbox.insert(tk.END, "Você: " + message + "\n", "green")
        chat_textbox.config(state="disabled")

        # Gerando e atualizando o chat_textbox com a resposta do GPT
        response = generate_chat_completion(messages)
        chat_textbox.config(state="normal")
        chat_textbox.insert(tk.END, "GPT: " + response + "\n", "blue")
        chat_textbox.config(state="disabled")

        # Movendo a barra de rolagem para exibir a última mensagem
        chat_textbox.see(tk.END)

        # Reduzindo o número de linhas exibidas no chat_textbox
        num_lines = chat_textbox.get("1.0", tk.END).count("\n")
        if num_lines > 100:  # Ajuste o número conforme necessário
            chat_textbox.delete("1.0", "2.0")
    def reset_messages():
        global messages
        messages = [
            {"role": "system",
             "content": "Você será um robô capaz de responder com exatidão às minhas perguntas. Além disso, você será capaz de analisar dados sem precisar de contexto envolvido"}
        ]

        print(messages)

    chat_textbox = tk.Text(window, height=25, width=80)
    chat_textbox.config(state="disabled")
    chat_textbox.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    chat_textbox.tag_config("green", foreground="green")
    chat_textbox.tag_config("blue", foreground="blue")

    user_input = tk.Entry(window, width=70)
    user_input.grid(row=1, column=0, padx=10, pady=10)

    file_button = tk.Button(window, text="Selecionar Arquivo", command=select_file)
    file_button.grid(row=2, column=1, padx=10, pady=10)

    send_button = tk.Button(window, text="Enviar", command=send_message)
    send_button.grid(row=1, column=1, padx=10, pady=10,ipadx=30)

    reset_button = tk.Button(window, text="Resetar cache", command=reset_messages, bg="red")

    reset_button.grid(row=2, column=0, padx=10, pady=10)

    window.mainloop()

def create_interface():
    window = tk.Tk()
    window.title("My local GPT")
    window.geometry("800x300")

    # Cria um rótulo com o texto
    lbl = tk.Label(window, text="MY LOCAL GPT",font=("Courier New", 24,'underline'))
    lbl.grid(row=0, column=0, columnspan=3, pady=(20, 10),padx=(150, 5))

    # Cria os botões
    btn_instrucoes = tk.Button(window, text="Instruções", width=20, height=5, bd=10, highlightbackground="blue",command=create_instructions_window)
    btn_imagem = tk.Button(window, text="Imagem", width=15, height=3, bd=10, highlightbackground="blue")
    btn_texto = tk.Button(window, text="Texto", width=15, height=3, bd=10, highlightbackground="blue",command = create_CPC)

    # Posiciona os botões na grade
    btn_imagem.grid(row=1, column=0, padx=(160, 5), pady=(60, 10))
    btn_instrucoes.grid(row=1, column=1, padx=(10, 5), pady=(60, 10))
    btn_texto.grid(row=1, column=2, padx=(10, 10), pady=(60, 10))

    window.mainloop()

def main():
    print("========CHAT GPT========")
    while 1:
        _input = input("USER: ")
        messages[1]["content"] = _input
        response_text = generate_chat_completion(messages)
        print("SYSTEM: " + response_text)


if __name__ == "__main__":
    create_interface()
    # main()
