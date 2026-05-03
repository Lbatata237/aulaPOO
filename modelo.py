import customtkinter as ctk

# Configurar aparência -----------------------------------------------------------------------------------------------|
ctk.set_appearance_mode('dark')


# Criar as funções de funcionalidades --------------------------------------------------------------------------------|

def clicarBotao():
    def validarLogin():
        usuario = campoUsuario.get()
    respBotaoOla = ctk.CTkLabel(app, text='uau parabens 👏')
    respBotaoOla.pack(pady=10)


# Criar janela principal ---------------------------------------------------------------------------------------------|
app = ctk.CTk()
app.title('Sistema de Matriz')
app.geometry('400x400')
# Criar os campos ----------------------------------------------------------------------------------------------------|
# Label:
labelUsuario = ctk.CTkLabel(app,text='Usuário:')
labelUsuario.pack(pady=10)
# Entry:
campoUsuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campoUsuario.pack(pady=10)

#novoLabel = ctk.CTkLabel(app,text='campoUsuario')
#novoLabel.pack(pady=10)


# Button:
botaoOla = ctk.CTkButton(app, text='ola', command=clicarBotao)
botaoOla.pack(pady=10)

# Iniciar a aplicação ------------------------------------------------------------------------------------------------|
app.mainloop()
