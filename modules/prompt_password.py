import getpass
passwd = getpass.getpass(prompt="Digite a senha: ")

if passwd.lower() == 'rodrigo':
    print("Bem vindo !")
else:
    print("Senha incorreta ")