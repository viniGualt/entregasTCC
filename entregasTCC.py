from time import sleep

def limpar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def leiaInt(msm):
    while True:
        try:
            n = int(input(msm)) 
        except (ValueError, TypeError):
            print("[ERRO: por favor, digite um número inteiro válido.]")
            continue
        except (KeyboardInterrupt):
            print("[Usuário preferiu não digitar esse número.]")
            return 0
        else:
            return n

def linha(tam = 100):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(100))
    print(linha())

def menu(lista):
    cabeçalho('Menu Principal')
    c=1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    return leiaInt("Sua Opção: ")

def voltarmenu(menu):
    while True:
        confirmar = input("Deseja voltar ao menu? [s] ou [n]\n").lower()
        if confirmar == 's':
            return 0
        elif confirmar == 'n':
            return menu
        else:
            print("Digite uma opção válida") 