import tkinter
import requests

#Link da API:
link = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,ARS-BRL"

#Requisitando a API:
req = requests.get(link).json()

#Função de converter as moedas:
def converter(tipo):
    valor_recebido = float(valor.get())

    if(tipo == "dolar"):
        saida = valor_recebido / float(req['USDBRL']['bid'])
    elif(tipo == "euro"):
        saida = valor_recebido / float(req['EURBRL']['bid'])
    else:
        saida = valor_recebido / float(req['ARSBRL']['bid'])
    
    conversao.delete(0, tkinter.END)
    conversao.insert(0, "{:.2f}".format(saida))


#janela do projeto:
janela = tkinter.Tk()
janela.title("Conversor de Moedas")
janela.geometry("500x500")
janela.config(bg="#1E90FF")

#Título e Textos:
tkinter.Label(janela, text="Conversor de Moedas",bg="#1E90FF",fg="white",font=("Tahoma Bold",28)).pack(pady=7)
tkinter.Label(janela, text="Digite o valor em R$:",bg="#1E90FF",fg="white",font=("Tahoma Bold",18)).place(x=10,y=100)

valor = tkinter.Entry(janela, width="40")
valor.place(x=240,y=106)

#Botões:
dolar = tkinter.Button(janela, text="Dólar ($)", command=lambda: converter("dolar"))
dolar.place(x=100,y=230)
euro = tkinter.Button(janela, text="Euro (€)", command=lambda: converter("euro"))
euro.place(x=335,y=230)
peso_argentino = tkinter.Button(janela, text="ARG ($)", command=lambda: converter("arg"))
peso_argentino.place(x=225,y=230)

#Conversão
tkinter.Label(janela, text="Valor Convertido:",bg="#1E90FF",fg="white",font=("Tahoma Bold",24)).place(x=125,y=300)
conversao = tkinter.Entry(janela, width="45")
conversao.place(x=110, y=350)

janela.mainloop()
