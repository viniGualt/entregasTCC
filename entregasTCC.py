from time import sleep
from datetime import datetime

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

def cabecalho(txt):
    print(linha())
    print(txt.center(100))
    print(linha())

def menu(lista):
    cabecalho('Menu Principal')
    for i, item in enumerate(lista, 1):
        print(f"{i} - {item}")
    print(linha())
    return leiaInt("Sua opção: ")

def voltarMenu():
    while True:
        confirmar = input("Deseja voltar ao menu? [s] ou [n]\n").lower()
        if confirmar == 's':
            return True
        elif confirmar == 'n':
            return False
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

def validaOrientador() -> str:
    while True:  
      orientador = input("Digite o nome do orinteador: ")
      if orientador not in orientadores:
          print("Digite um orientador válido")
      else:
          return orientador    

def registrarEntrega() -> tuple:
    apresentacao = input("Digite a numeração aprese")

alunos = []

def cadastrarAluno() -> None:
    while True:
        limpar()
        nome = str(input("Digite o nome do aluno que deseja cadastrar: "))
        matricula = str(input("Digite a matrícula do aluno: "))
        orientador = validaOrientador()
        entregas = []
        aluno = {
            "nome": nome,
            "matricula": matricula,
            "orientador": orientador,
            "entregas": entregas
        }
        alunos.append(aluno)
        orientador[orientadores].append(aluno)
        sleep(1)
        sair = input("Deseja cadastrar outro aluno? (Digite 'q' para sair): ").strip().lower()
        if sair == 'q':
            break

def buscar_aluno_por_matricula(matricula: str):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None

def registrarEntrega():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno_por_matricula(matricula)
    
    if aluno:
        for entrega in aluno["entregas"]:
            if entrega[2] is None:
                print("Há uma entrega pendente de avaliação. Não é possível registrar uma nova entrega.")
                return
        numero_versao = len(aluno["entregas"]) + 1
        data_entrega = input("Digite a data de entrega (YYYY-MM-DD): ")
        try:
            datetime.strptime(data_entrega, "%Y-%m-%d")
        except ValueError:
            print("Data inválida. Utilize o formato YYYY-MM-DD.")
            return
        aluno["entregas"].append((numero_versao, data_entrega, None))
        print("Entrega registrada com sucesso!")
    else:
        print("Aluno não encontrado.")
