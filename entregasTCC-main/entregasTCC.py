from time import sleep
from datetime import datetime

def limpar() -> None:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def leia_int(msm) -> None:
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
    return leia_int("Sua opção: ")

def voltar_menu():
    while True:
        confirmar = input("Deseja voltar ao menu? [s] ou [n]\n").lower()
        if confirmar == 's':
            return True
        elif confirmar == 'n':
            return False
        else:
            print("Digite uma opção válida") 
            
orientadores = {}
alunos = []

def cadastrar_orientador() -> None:
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

def valida_orientador() -> str:
    while True:  
        orientador = input("Digite o nome do orientador: ")
        if orientador not in orientadores:
            print("Digite um orientador válido")
        else:
            return orientador    

def cadastrar_aluno() -> None:
    while True:
        limpar()
        nome = str(input("Digite o nome do aluno que deseja cadastrar: "))
        matricula = str(input("Digite a matrícula do aluno: "))
        orientador = valida_orientador()
        entregas = []
        aluno = {
            "nome": nome,
            "matricula": matricula,
            "orientador": orientador,
            "entregas": entregas
        }
        alunos.append(aluno)
        orientadores[orientador].append(nome)
        print(f"Aluno {nome} cadastrado com sucesso!")
        sleep(1)
        sair = input("Deseja cadastrar outro aluno? (Digite 'q' para sair): ").strip().lower()
        if sair == 'q':
            break

def buscar_aluno_por_matricula(matricula: str):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None

def registrar_entrega():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno_por_matricula(matricula)
    
    if aluno:
        for entrega in aluno["entregas"]:
            if entrega[2] is None:
                print("Há uma entrega pendente de avaliação, sendo assim ão é possível registrar uma nova entrega.")
                return
        numero = len(aluno["entregas"]) + 1
        data_entrega = input("Digite a data de entrega (YYYY-MM-DD): ")
        try:
            datetime.strptime(data_entrega, "%Y-%m-%d")
        except ValueError:
            print("Data inválida. Utilize o formato YYYY-MM-DD.")
            return
        aluno["entregas"].append((numero, data_entrega, None))
        print("Entrega registrada com sucesso!")
    else:
        print("Aluno não encontrado.")

def registar_nota():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno_por_matricula(matricula)

    if aluno:
        pendentes = [entrega for entrega in aluno['entrega'] if entrega[2] is None]
        if not pendentes:
            print("Não há entregas para esse aluno")
            return
        nota = float(input("Digite a nota para  a entrega pendente do aluno"))
        for i in range (len(alunos['entregas'])):
            if aluno['entrega'][i][2] is None:
                numero, data_entrega, _ = aluno['entrega']
                aluno['entrega'][i] = (numero, data_entrega, nota)
                print("Nota registrada com sucesso")
                break

def listar_alunos_por_orientador():
    limpar()
    for orientador, alunos_orientados in orientadores.items():
        print(f"Orientador: {orientador}")
        print("Alunos:")
        for aluno in alunos_orientados:
            print(f" - {aluno}")
        print(linha())
    input("Pressione qualquer tecla para voltar ao menu...")

def listar_entregas_por_aluno():
    limpar()
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno_por_matricula(matricula)
    if aluno:
        print(f"Entregas do aluno {aluno['nome']}:")
        for entrega in aluno["entregas"]:
            print(f"Versão: {entrega[0]}, Data: {entrega[1]}, Nota: {entrega[2]}")
    else:
        print("Aluno não encontrado.")
    input("Pressione qualquer tecla para voltar ao menu...")

def listar_pendencias_avaliacao():
    limpar()
    for orientador, alunos_orientados in orientadores.items():
        print(f"Orientador: {orientador}")
        for aluno_nome in alunos_orientados:
            aluno = next((a for a in alunos if a["nome"] == aluno_nome), None)
            if aluno:
                pendencias = [entrega for entrega in aluno["entregas"] if entrega[2] is None]
                if pendencias:
                    print(f" - Aluno: {aluno['nome']} possui {len(pendencias)} entrega(s) pendente(s).")
        print(linha())
    input("Pressione qualquer tecla para voltar ao menu...")
