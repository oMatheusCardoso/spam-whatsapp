import pyautogui as pygui
import tkinter as tk
from tkinter import  messagebox
import time

executando = False
contador = 0

def botao_spam():
  global contador, executando

  executando = True
  contador = 0

  botao_iniciar.config(state=tk.DISABLED)
  botao_parar.config(state=tk.NORMAL)

  msg = entrada_mensagem.get().strip()

  try:
    qtd = int(entrada_quantidade.get())
  except ValueError:
    messagebox.showerror('Por favor, insira um número inteiro.')
    finalizar_envio()
    return

  if not msg:
    messagebox.showerror('Por favor, insira uma mensagem.')
    finalizar_envio()
    return

  if qtd <= 0:
    messagebox.showerror('Por favor, insira um número maior do que 0.')
    finalizar_envio()
    return

  feedback_label.config(text='Em 10 segundos, o envio começará!\n Deixe o input do WhatsApp selecionado.')
  janela.update_idletasks()
  janela.after(10000, lambda: enviar_mensagens(msg, qtd))

def enviar_mensagens(msg, qtd):
  global contador, executando
  if not executando or contador >= qtd:
    finalizar_envio()
    return
  
  pygui.write(msg)
  pygui.press('enter')
  contador += 1
  feedback_label.config(text=f'Enviado {contador} de {qtd} vezes.')
  janela.update_idletasks()
  janela.after(300, lambda: enviar_mensagens(msg, qtd))

def finalizar_envio():
  global executando
  executando = False
  botao_iniciar.config(state=tk.NORMAL)
  botao_parar.config(state=tk.DISABLED)
  feedback_label.config(text='Envio concluído ou interrompido.')


def parar_spam():
  global executando
  executando = False
  feedback_label.config(text='Envio Interrompido!')
  finalizar_envio()

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

botao_parar = tk.Button(janela, text="Parar Spam", command=parar_spam, state=tk.DISABLED)
botao_parar.grid(column=0, row=5, padx=10, pady=10)

feedback_label = tk.Label(janela, text='', fg='blue')
feedback_label.grid(column=0, row=6, padx=10, pady=10, sticky='ew')

janela.columnconfigure(0, weight=1)
janela.mainloop()