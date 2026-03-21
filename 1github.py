import os


print("✉️  Coisando(configurando) email")
comandoEmail = 'git config user.email "leonardononatobs@gmail.com"'
os.system(comandoEmail)


print("➕  Adicionando modificações...")
comando1 = "git add *"
os.system(comando1)


mensagem = input("🤯  Mensagem do commit: ")
while( len(mensagem) < 5 ):
    print("‼️ Mensagem muito pequena, detalhe mais...")
    mensagem = input("🤯  Mensagem do commit: ")


print("▪️▪️▪️  Registrando alterações")
comando2 = "git commit -m "+mensagem
os.system(comando2)


print("🛜  Enviando projeto ao github")
comando3 = "git push"
os.system(comando3)