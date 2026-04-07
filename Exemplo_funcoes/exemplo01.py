# Funções no Python

# Criar uma função para exibir uma mensagem na tela - DEF = Define

def exibir_mensagem(): 
    print("Olá, esta é uma função em Python!")

# Chamada de funcao exibir_mensagem
exibir_mensagem()

# Criar uma funcao  para exibir uma mensagem customizada
def exibir_mensagem_custom(mensagem):
    print(mensagem)

# Chamada da função exibir_mensagem_custom
msg = input("Digite a mensagem que deseja exibir: ")
exibir_mensagem_custom(msg)