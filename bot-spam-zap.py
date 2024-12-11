import pyautogui
import time

contador = 0
msg = input('Escreva a mensagem no qual irá se repetir: ')
qtd = int(input('Quantas vezes repetirá a mensagem? '))
print('Em 10 segundos começará a repetição da mensagem!', 'Deixe selecionado o input de mensagem do whatsapp.')
time.sleep(10)

while contador < qtd:
  pyautogui.write(f'{msg}')
  time.sleep(0.5)  
  pyautogui.press('enter')
  print(f'Mensagem repetida {contador + 1} vezes.')
  contador += 1


