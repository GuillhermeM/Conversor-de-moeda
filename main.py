from bcb import currency
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import datetime

def gerar_grafico():
    # Recupera a data selecionada do seletor de data
    data_selecionada = cal.get_date()

    # Define as moedas e o período de tempo
    moedas = ['USD', 'EUR']
    data_inicio = data_selecionada.strftime('%Y-%m-%d')
    data_fim = (data_selecionada + datetime.timedelta(days=365)).strftime('%Y-%m-%d')

    # Recupera as taxas de câmbio usando o módulo bcb.currency
    taxas = currency.get(moedas, start=data_inicio, end=data_fim)

    # Plota as taxas de câmbio em um gráfico usando o matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(taxas.index, taxas['USD'], label='USD')
    ax.plot(taxas.index, taxas['EUR'], label='EUR')
    ax.legend()
    ax.set_xlabel('Data')
    ax.set_ylabel('Taxa de câmbio')
    ax.set_title('Taxas de câmbio USD/EUR')
    plt.show()
    

# Cria a janela Tkinter com o seletor de data e o botão
root = tk.Tk()
root.title('Gráfico de Taxas de Câmbio')
root.geometry('300x200')

# Adiciona o seletor de data
cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.pack(padx=10, pady=10)

# Adiciona o botão para gerar o gráfico
gerar_botao = ttk.Button(root, text="Gerar Gráfico", command=gerar_grafico)
gerar_botao.pack(padx=10, pady=10)

root.mainloop()
