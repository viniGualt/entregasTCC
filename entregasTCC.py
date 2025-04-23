from time import sleep

def limpar() -> None:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def leiaInt(msm) -> None:
    while True:
        try:
            n = int(input(msm)) 
        except (ValueError, TypeError):
            print("Por favor, digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("Usuário preferiu não digitar esse número.")
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
            
orientadores = {}

def cadastrarOrientador() -> None:
    while True:
        limpar()
        nome = input("Digite o nome do orientador que deseja cadastrar: ")
        if nome not in orientadores:
            orientadores[nome] = []
            print(f"Orientador {nome} cadastrado com sucesso!")
            sleep(1)
        else:
            print(f"Orientador já cadastrado.")
            sleep(1)
        
        sair = input("Deseja sair? (Caso sim, digite 'q'): ")
        if sair.lower() == "q":
            break
        
cadastrarOrientador()
print(orientadores)