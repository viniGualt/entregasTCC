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
    c=1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    return leia_int("Sua Opção: ")
            
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
        
        sair = input("Deseja sair? (Caso sim, digite 'q'): ").lower()
        if sair.lower() == "q":
            break

def valida_orientador() -> str:
    while True:  
        orientador = input("Digite o nome do orientador: ")
        if orientador not in orientadores:
            print("Digite um orientador válido")
            resposta1 = input("Se deseja cadastrar um novo orientador digite '1', se escreveu o nome errado digite '2': ")
            while True:
                if resposta1 == '1':
                    print("Indo cadastrar um orientador")
                    sleep(1)
                    cadastrar_orientador()
                    break
                elif resposta1 == '2':
                    print("Digite o nome novamente")
                    sleep(1)
                    valida_orientador()
                    break
                else:
                    print("Opção inválida. Digite '1' para cadastrar um novo orientador ou '2' para corrigir o nome.")
                    
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

def solicitar_data_entrega():
    while True:
        data_entrega = input("Digite a data de entrega (YYYY-MM-DD) ou deixe vazio para cancelar: ")
        if data_entrega == "":
            print("Operação cancelada pelo usuário.")
            return None
        try:
            datetime.strptime(data_entrega, "%Y-%m-%d")
            return data_entrega
        except ValueError:
            print("Data inválida. Utilize o formato YYYY-MM-DD.")

def registrar_entrega():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno_por_matricula(matricula)
    
    if aluno:
        for entrega in aluno["entregas"]:
            if entrega[2] is None:
                print("Há uma entrega pendente de avaliação, sendo assim não é possível registrar uma nova entrega.")
                return
        numero = len(aluno["entregas"]) + 1
        data_entrega = solicitar_data_entrega()
        if data_entrega is None:
            return
        aluno["entregas"].append((numero, data_entrega, None))
        print("Entrega registrada com sucesso!")
    else:
        print("Aluno não encontrado.")
        sleep(1)
        operacoes()

def registrar_nota():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno_por_matricula(matricula)

    if aluno:
        pendentes = [entrega for entrega in aluno['entregas'] if entrega[2] is None]
        if not pendentes:
            print("Não há entregas para esse aluno")
            sleep(1)
            return
        nota = float(input("Digite a nota para a entrega pendente do aluno: "))
        for i in range(len(aluno['entregas'])):
            if aluno['entregas'][i][2] is None:
                numero, data_entrega, _ = aluno['entregas'][i]
                aluno['entregas'][i] = (numero, data_entrega, nota)
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
        sleep(1)
        operacoes()

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

def media_por_aluno():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno_por_matricula(matricula)
    
    if aluno:
        entregas_com_nota = [entrega for entrega in aluno["entregas"] if entrega[2] is not None]
        
        if entregas_com_nota:
            media = sum(entrega[2] for entrega in entregas_com_nota) / len(entregas_com_nota)
            print(f"A média do aluno {aluno['nome']} é: {media:.2f}")
        else:
            print(f"O aluno {aluno['nome']} ainda não tem nenhuma entregas avaliadas por seu orientador.")
    else:
        print("Aluno não encontrado.")

def media_geral_por_orientador():
    for orientador, alunos_orientados in orientadores.items():
        notas = []
        for aluno_nome in alunos_orientados:
            aluno = next((a for a in alunos if a["nome"] == aluno_nome), None)
            if aluno:
                entregas_com_nota = [entrega for entrega in aluno["entregas"] if entrega[2] is not None]
                
                if entregas_com_nota:
                    media = sum(entrega[2] for entrega in entregas_com_nota) / len(entregas_com_nota)
                    notas.append(media)

        if notas:
            media_geral = sum(notas) / len(notas)
            print(f"A média geral dos alunos orientados por {orientador} é: {media_geral:.2f}")
        else:
            print(f"Não há entregas avaliadas para os alunos orientados por {orientador}.")


def operacoes():
    limpar()
    print("1. Registrar nova entrega.")
    print("2. Registrar nota.")
    print("3. Listar alunos por orientador.")
    print("4. Listar versões entregas por aluno.")
    print("5. Listar pendências de avaliações.")
    print("6. Listar média por aluno.")
    print("7. Listar média geral por orientador.")
    print("q. Sair.")
    resposta2 = input("\nInsira o número para a operação que deseja ou 'q' para ir para o menu: ").lower()
    while True:
        if resposta2 == "1":
            limpar()    
            registrar_entrega()
        elif resposta2 == "2":
            limpar()
            registrar_nota()
        elif resposta2 == "3":
            limpar()
            listar_alunos_por_orientador()
        elif resposta2 == "4":
            limpar()
            listar_entregas_por_aluno()
        elif resposta2 == "5":
            limpar()
            listar_pendencias_avaliacao()
        elif resposta2 == "6":
            limpar()
            media_por_aluno()
        elif resposta2 == "7":
            limpar()
            media_geral_por_orientador()
        elif resposta2 == "q":
            limpar()
            print("Voltando ao menu...")
            sleep(1)
            break
        else:
            print("Opção inválida.")

while True:
    limpar()
    resposta3 = menu(["Cadastrar aluno", "Cadastrar orientador", "Demais operações"])
    if resposta3 == 1:
        limpar()
        cadastrar_aluno()
    elif resposta3 == 2:
        limpar()
        cadastrar_orientador()
    elif resposta3 == 3:
        limpar()
        operacoes()
    elif resposta3 == "q":
        print("Saindo do programa...")
        sleep(1)
        break
    else:
        print("Opção inválida.")