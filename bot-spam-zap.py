import pyautogui as pygui
import tkinter as tk
from tkinter import  messagebox
import time

def botao_spam():
  global contador

  contador = 0
  msg = entrada_mensagem.get().strip()

  try:
    qtd = int(entrada_quantidade.get())
  except ValueError:
    messagebox.showerror('Por favor, insira um número inteiro.')
    return

  if not msg:
    messagebox.showerror('Por favor, insira uma mensagem.')
    return

  if qtd <= 0:
    messagebox.showerror('Por favor, insira um número inteiro positivo.')
    return

  feedback_label.config(text='Em 10 segundos, o envio começará!\n Deixe o input do WhatsApp selecionado.')
  janela.update_idletasks()
  time.sleep(10)

  
  for i in range(qtd):
    pygui.write(msg)
    pygui.press('enter')
    contador += 1
    feedback_label.config(text=f'Enviado {contador} de {qtd} vezes.')
    janela.update_idletasks()
    time.sleep(0.3)

  feedback_label.config(text='Envio Concluído!')
  botao_iniciar.config(state=tk.NORMAL)

janela = tk.Tk()
janela.title('Spam message for WhatsApp')
janela.geometry('400x300')

texto_orientacao = tk.Label(janela, text="Escreva a mensagem no qual irá se repetir.")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

entrada_mensagem = tk.Entry(janela, width=50)
entrada_mensagem.grid(column=0, row=1, padx=10, pady=10)

texto_orientacao_qtd = tk.Label(janela, text="Selecione a quantidade de vezes que irá repetir a mensagem.")
texto_orientacao_qtd.grid(column=0, row=2, padx=10, pady=10, sticky='ew')

entrada_quantidade = tk.Spinbox(janela, from_=1, to=1000, width=10)
entrada_quantidade.grid(column=0, row=3, padx=10, pady=10)

botao_iniciar = tk.Button(janela, text="Iniciar Spam", command=botao_spam)
botao_iniciar.grid(column=0, row=4, padx=10, pady=10)

feedback_label = tk.Label(janela, text='', fg='blue')
feedback_label.grid(column=0, row=5, padx=10, pady=10, sticky='ew')

janela.columnconfigure(0, weight=1)
janela.mainloop()