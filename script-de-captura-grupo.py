from datetime import datetime
import math
import time as t
import psutil as p
from mysql.connector import connection

db = connection.MySQLConnection(
    host="localhost",
    port=3306,
    user="aluno2",
    passwd="sptech",
    database="grupo10"
)

cursor = db.cursor()

print("\n_______________________________________________________________")


def menuCaptura(id):
    while True:
        print("\n Menu de Captura e Análise")

        selecao1 = str(input("\n\n Selecione o número respectivo a categoria que deseja analisar: \n1- CPU \n2- RAM \n3- Disco \n4- Rede \n5- Histórico de Dados \n6- Sair do Programa\n\nOpção: "))

        if selecao1 == '1':
            print("\nCapturando dados de CPU. Pressione 'ctrl + c' para voltar ao menu.\n")
            while True:
                try:

                    # Sessão da CPU -------------------------

                    # Definir todas as variaveis, para possivel inserção de todos os dados, para o banco não ficar com null

                    # CPU -

                    uso_cpu = p.cpu_percent(interval=0)
                    freq_cpu = int(p.cpu_freq().current)
                    nucleo_cpu = p.cpu_percent(interval=1, percpu=True)

                    # a coluna cpuUsoPorNucleo usa varios valores para cada nucleo por isso precisa converter pra string

                    nucleo_cpu_str = ",".join(str(valor) for valor in nucleo_cpu)

                    # Memoria RAM -

                    ram = p.virtual_memory()
                    ram_percentual = ram.percent
                    ram_usada_gb = int(ram.used / (1024**3))
                    ram_disponivel_gb = int(ram.available / (1024**3))

                    # Disco -

                    disco = p.disk_usage('/')
                    disco_percentual = disco.percent
                    disco_usado_gb = int(disco.used / (1024**3))
                    disco_livre_gb = int(disco.free / (1024**3))

                    #Rede
                    
                    rede = p.net_io_counters()
                    download_bytes = rede.bytes_recv
                    upload_bytes = rede.bytes_sent

                    download_bytesF = round(download_bytes / 1000000, 1)
                    upload_bytesF = round(upload_bytes / 1000000, 1)

                    print("Uso da CPU: ", uso_cpu, "%")
                    print("Frequência atual da CPU: ", freq_cpu, "Mhz\n\n")

                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = agora.strftime("%H:%M:%S")

                    print("Data e Hora da Captura: ")
                    print(data_formatada, hora_atual, '\n')

                    print("Uso por Núcleo da CPU: ")
                    print(nucleo_cpu, '\n')

                    comando_sql = """
                        INSERT INTO registro 
                        (fkMaquina, cpuPorcentagemUso, cpuFrequenciaAtual, cpuUsoPorNucleo,
                         ramDisponivel, ramUsada, ramPercentualUso,
                          discoEspacoUsado, discoEspacoLivre,
                          downloadRede, uploadRede,
                           dtRegistro) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, NOW())"""
                    valores = (id, uso_cpu, freq_cpu, nucleo_cpu_str, 
                               ram_disponivel_gb, ram_usada_gb, ram_percentual,
                                 disco_usado_gb, disco_livre_gb,
                                 download_bytesF, upload_bytesF)

                    cursor.execute(comando_sql, valores)
                    db.commit()

                    print("\nO Programa está em funcionamento. Pressione 'ctrl + c' para voltar ao menu.\n\n")

                    t.sleep(3)

                except KeyboardInterrupt:
                    print("\nCaptura de CPU interrompida. Voltando ao menu...\n")
                    break

        elif selecao1 == '2':
            print("\nCapturando dados de RAM. Pressione 'ctrl + c' para voltar ao menu.\n")
            while True:
                try:

                    # Sessão da memoria ram

                    # Definir todas as variaveis, para possivel inserção de todos os dados, para o banco não ficar com null

                    # Memoria RAM

                    ram = p.virtual_memory()
                    ram_percentual = ram.percent
                    ram_usada_gb = int(ram.used / (1024**3))
                    ram_disponivel_gb = int(ram.available / (1024**3))

                    # CPU

                    uso_cpu = p.cpu_percent(interval=0)
                    freq_cpu = int(p.cpu_freq().current)
                    nucleo_cpu = p.cpu_percent(interval=1, percpu=True)
                                        
                    nucleo_cpu_str = ",".join(str(valor) for valor in nucleo_cpu)

                    # DISCO

                    disco = p.disk_usage('/')
                    disco_percentual = disco.percent
                    disco_usado_gb = int(disco.used / (1024**3))
                    disco_livre_gb = int(disco.free / (1024**3))

                    #Rede
                    
                    rede = p.net_io_counters()
                    download_bytes = rede.bytes_recv
                    upload_bytes = rede.bytes_sent

                    download_bytesF = round(download_bytes / 1000000, 1)
                    upload_bytesF = round(upload_bytes / 1000000, 1)

                    print("Uso da RAM: ", ram_percentual, "%")
                    print("RAM em uso: ", round(ram.used / 1000000000, 1), "GB\n\n")

                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = agora.strftime("%H:%M:%S")
                    print("Data e Hora da Captura: ")
                    print(data_formatada, hora_atual, '\n')

                    comando_sql = """
                        INSERT INTO registro 
                        (fkMaquina, cpuPorcentagemUso, cpuFrequenciaAtual, cpuUsoPorNucleo,
                         ramDisponivel, ramUsada, ramPercentualUso,
                          discoEspacoUsado, discoEspacoLivre,
                          downloadRede, uploadRede,
                           dtRegistro) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, NOW())"""
                    valores = (id, uso_cpu, freq_cpu, nucleo_cpu_str, 
                               ram_disponivel_gb, ram_usada_gb, ram_percentual,
                                 disco_usado_gb, disco_livre_gb,
                                 download_bytesF, upload_bytesF)
                    
                    cursor.execute(comando_sql, valores)
                    cursor.execute(comando_sql, valores)
                    db.commit()

                    print("\nO Programa está em funcionamento. Pressione 'ctrl + c' para voltar ao menu.\n\n")

                    t.sleep(3)

                except KeyboardInterrupt:
                    print("\nCaptura de RAM interrompida. Voltando ao menu...\n")
                    break

        elif selecao1 == '3':
            print("\nCapturando dados de Disco. Pressione 'ctrl + c' para voltar ao menu.\n")
            while True:
                try:

                    # Sessão do Disco

                    # Definir todas as variaveis, para possivel inserção de todos os dados, para o banco não ficar com null

                    # Disco

                    disco = p.disk_usage('/')
                    disco_percentual = disco.percent
                    disco_usado_gb = int(disco.used / (1024**3))
                    disco_livre_gb = int(disco.free / (1024**3))

                    # CPU

                    uso_cpu = p.cpu_percent(interval=0)
                    freq_cpu = int(p.cpu_freq().current)
                    nucleo_cpu = p.cpu_percent(interval=1, percpu=True)
                                        
                    nucleo_cpu_str = ",".join(str(valor) for valor in nucleo_cpu)

                    # Memoria RAM

                    print("Uso do Disco: ", disco_percentual, "%")
                    print("Espaço de Disco em uso: ", round(disco.used / 1000000000, 1), "GB\n\n")

                    #Rede

                    rede = p.net_io_counters()
                    download_bytes = rede.bytes_recv
                    upload_bytes = rede.bytes_sent

                    download_bytesF = round(download_bytes / 1000000, 1)
                    upload_bytesF = round(upload_bytes / 1000000, 1)

                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = agora.strftime("%H:%M:%S")
                    print("Data e Hora da Captura: ")
                    print(data_formatada, hora_atual, '\n')

                    comando_sql = """
                        INSERT INTO registro 
                        (fkMaquina, cpuPorcentagemUso, cpuFrequenciaAtual, cpuUsoPorNucleo,
                         ramDisponivel, ramUsada, ramPercentualUso,
                          discoEspacoUsado, discoEspacoLivre,
                          downloadRede, uploadRede,
                           dtRegistro) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, NOW())"""
                    valores = (id, uso_cpu, freq_cpu, nucleo_cpu_str, 
                               ram_disponivel_gb, ram_usada_gb, ram_percentual,
                                 disco_usado_gb, disco_livre_gb,
                                 download_bytesF, upload_bytesF)

                    cursor.execute(comando_sql, valores)
                    cursor.execute(comando_sql, valores)
                    db.commit()

                    print("\nO Programa está em funcionamento. Pressione 'ctrl + c' para voltar ao menu.\n\n")

                    t.sleep(3)

                except KeyboardInterrupt:
                    print("\nCaptura de Disco interrompida. Voltando ao menu...\n")
                    break

        elif selecao1 == '4':
            print("\nCapturando dados de Rede. Pressione 'ctrl + c' para voltar ao menu.\n")
            while True:
                try:
                    #Sessão de rede

                    # Rede -

                    rede = p.net_io_counters()
                    download_bytes = rede.bytes_recv
                    upload_bytes = rede.bytes_sent

                    download_bytesF = round(download_bytes / 1000000, 1)
                    upload_bytesF = round(upload_bytes / 1000000, 1)

                    # CPU -

                    uso_cpu = p.cpu_percent(interval=0)
                    freq_cpu = int(p.cpu_freq().current)
                    nucleo_cpu = p.cpu_percent(interval=1, percpu=True)

                    nucleo_cpu_str = ",".join(str(valor) for valor in nucleo_cpu)

                    # Memoria RAM -

                    ram = p.virtual_memory()
                    ram_percentual = ram.percent
                    ram_usada_gb = int(ram.used / (1024**3))
                    ram_disponivel_gb = int(ram.available / (1024**3))

                    # Disco -

                    disco = p.disk_usage('/')
                    disco_percentual = disco.percent
                    disco_usado_gb = int(disco.used / (1024**3))
                    disco_livre_gb = int(disco.free / (1024**3))

                    print("Bytes Enviados na Rede: ", upload_bytesF, "MB")
                    print("Bytes Recebidos na Rede: ", download_bytesF, "MB\n\n")

                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = agora.strftime("%H:%M:%S")
                    print("Data e Hora da Captura: ")
                    print(data_formatada, hora_atual, '\n')

                    comando_sql = """
                        INSERT INTO registro 
                        (fkMaquina, cpuPorcentagemUso, cpuFrequenciaAtual, cpuUsoPorNucleo,
                         ramDisponivel, ramUsada, ramPercentualUso,
                          discoEspacoUsado, discoEspacoLivre,
                          downloadRede, uploadRede,
                           dtRegistro) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, NOW())"""
                    valores = (id, uso_cpu, freq_cpu, nucleo_cpu_str, 
                               ram_disponivel_gb, ram_usada_gb, ram_percentual,
                                 disco_usado_gb, disco_livre_gb,
                                 download_bytesF, upload_bytesF)

                    cursor.execute(comando_sql, valores)
                    db.commit()

                    print("\nO Programa está em funcionamento. Pressione 'ctrl + c' para voltar ao menu.\n\n")
                    t.sleep(3)

                except KeyboardInterrupt:
                    print("\nCaptura de Rede interrompida. Voltando ao menu...\n")
                    break

        elif selecao1 == '5':
            print(f"\nHistórico de Dados da Máquina (ID: {id})")

            cursor_dict = db.cursor(dictionary=True)

            comando_sql = """
                SELECT idRegistro, cpuPorcentagemUso, ramPercentualUso, discoEspacoUsado, downloadRede, uploadRede, dtRegistro 
                FROM registro 
                WHERE fkMaquina = %s 
                ORDER BY dtRegistro DESC 
                LIMIT 10
            """

            cursor_dict.execute(comando_sql, (id,))
            historico = cursor_dict.fetchall()

            if historico:
                print("\nÚltimos 10 registrs da máquina:")
                for registro in historico:
                    data = registro['dtRegistro'].strftime("%d/%m/%Y %H:%M:%S") if registro['dtRegistro'] else "N/D"

                    print(f"ID: {registro['idRegistro']} | CPU: {registro['cpuPorcentagemUso']}% | RAM: {registro['ramPercentualUso']}% | Disco: {registro['discoEspacoUsado']} GB | Download: {registro['downloadRede']} B | Upload: {registro['uploadRede']} B | Data: {data}")
            else:
                print("\nNenhum histórico encontrado para esta Máquina no Banco de Dados.")

            cursor_dict.close()

        elif selecao1 == '6':
            print("Saindo do Menu de Captura...")
            break
        else:
            print("Opção inválida!")


def menu():
    while True:
        print("\n Seja Bem-Vindo ao Programa de Captura de Dados de Hardware!")

        selecao2 = str(input("\n\n Selecione o número respectivo a categoria que deseja acessar: \n\n1- Entrar ao Programa \n2- Cadastrar Máquina ao Programa \n3- Sair do Programa\n\nOpção: "))

        if selecao2 == '1':
            while True:

                idMaquina = int(input("\nID da Máquina: "))
                nomeMaquina = str(input("Nome da Máquina: "))

                comando_sql = "SELECT nome FROM maquina WHERE id = %s"
                valores = (idMaquina,)

                cursor.execute(comando_sql, valores)
                resultados = cursor.fetchone()

                if resultados is not None and resultados[0] == nomeMaquina:
                    print("\nAcesso Liberado! O Programa irá realizar a Consulta de Dados respectivos a sua Máquina.")

                    menuCaptura(idMaquina)
                    return idMaquina
                else:
                    print("\nAcesso Negado! ID ou Nome da Máquina incorretos.\n")
                    break

        elif selecao2 == '2':

            nome = str(input("Nome da máquina: "))
            nucleosFisicos = p.cpu_count(logical=False)
            nucleosLogicos = p.cpu_count(logical=True)
            capacidadeDisco = p.disk_usage('/').total
            ramTotal = p.virtual_memory().total

            capacidadeDiscoFormatado = capacidadeDisco / 1000000000
            ramTotalFormatada = ramTotal / 1000000000

            print(f"\n\nDados Capturados: \nNúcleos Físicos: {nucleosFisicos} \nNúcleos Lógicos: {nucleosLogicos} \nCapacidade de Disco Formatado: {round(capacidadeDiscoFormatado, 1)} GB \nCapacidade de RAM Total: {round(ramTotalFormatada, 1)} GB")

            comando_sql = "INSERT INTO maquina (nome, nucleosFisicos, nucleosLogicos, capacidadeTotal, ramTotal, dtCadastro) VALUES (%s, %s, %s, %s, %s, NOW())"
            valores = (nome, nucleosFisicos, nucleosLogicos, round(capacidadeDiscoFormatado, 1), round(ramTotalFormatada, 1))

            cursor.execute(comando_sql, valores)
            db.commit()

            print("\n\nOs Dados da Máquina foram Cadastrados!")
            print(f"ID da máquina cadastrada: {cursor.lastrowid}\n")
            print("Faça o login acessando a Opção 1!\n")

        elif selecao2 == '3':
            print("Até a Próxima!")
            break

        else:
            print("Opção Inválida!")


menu()