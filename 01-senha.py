nome = input ("digite o nome: ")
senha = input ("digite sua senha: ")
senha_cadastrada = "123"
nome_cadastrado = "ana"

while senha != senha_cadastrada:
    print ("nome ou senha incorreto! Tente novamente.")
    nome = input ("Digite o seu nome: ")
    senha = input ("digite sua senha: ")

print (f"{nome} Bem-vindo ao Sistena...")
