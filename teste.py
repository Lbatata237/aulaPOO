import customtkinter
app = customtkinter.CTk()
def butaoClicado():
    resp = customtkinter.CTkLabel(app, text="ai meu butao")
    resp.pack()
app.title("Teste de janela")

botao = customtkinter.CTkButton(app, text="meu botão", command=butaoClicado)

botao.pack(padx=20, pady=20)




app.geometry("400x400")
app.mainloop()