#atividade de Daniel Guimarães Silva - Turma B -
# Dados dos processos
processos = [
    {"processo": "P1", "arrival_time": 0, "tempo_processo": 1},
    {"processo": "P2", "arrival_time": 0, "tempo_processo": 2},
    {"processo": "P3", "arrival_time": 1, "tempo_processo": 1},
    {"processo": "P4", "arrival_time": 0, "tempo_processo": 15},
    {"processo": "P5", "arrival_time": 2, "tempo_processo": 10},
]

# Configurações do Round Robin
quantum = 2
overhead = 1

# Inicializando variáveis
tempo_atual = 0
fila = []
ordem_atendimento = []
tempos_resposta = {}
tempos_retorno = {}
tempo_restante = {p["processo"]: p["tempo_processo"] for p in processos}
tempo_inicio_execucao = {}
processos_na_fila = {p["processo"]: False for p in processos}

# Função para adicionar processos que chegaram na fila
def adicionar_processos_na_fila(tempo_atual):
    for p in processos:
        if p["arrival_time"] <= tempo_atual and not processos_na_fila[p["processo"]]:
            fila.append(p)
            processos_na_fila[p["processo"]] = True

# Simulação do Round Robin
while fila or any(tempo_restante[p["processo"]] > 0 for p in processos):
    adicionar_processos_na_fila(tempo_atual)
    
    if fila:
        processo_atual = fila.pop(0)
        p_nome = processo_atual["processo"]

        # Tempo de resposta (se o processo ainda não começou a ser executado)
        if p_nome not in tempo_inicio_execucao:
            tempo_inicio_execucao[p_nome] = tempo_atual
            tempos_resposta[p_nome] = tempo_inicio_execucao[p_nome] - processo_atual["arrival_time"]

        # Executa o processo por um quantum ou pelo tempo restante, o que for menor
        tempo_execucao = min(quantum, tempo_restante[p_nome])
        tempo_restante[p_nome] -= tempo_execucao
        tempo_atual += tempo_execucao

        # Se o processo terminou, calcula o tempo de retorno
        if tempo_restante[p_nome] == 0:
            tempos_retorno[p_nome] = tempo_atual - processo_atual["arrival_time"]

        ordem_atendimento.append(p_nome)

        # Adiciona o overhead de troca de contexto
        tempo_atual += overhead

        # Se o processo não terminou, volta para a fila
        if tempo_restante[p_nome] > 0:
            adicionar_processos_na_fila(tempo_atual)
            fila.append(processo_atual)
    else:
        # Se a fila estiver vazia, avance o tempo até o próximo processo chegar
        tempo_atual += 1

# Cálculo das médias de tempo de resposta e retorno
media_tempo_resposta = sum(tempos_resposta.values()) / len(processos)
media_tempo_retorno = sum(tempos_retorno.values()) / len(processos)

# Exibição dos resultados
print("Ordem de Atendimento dos Processos:", ordem_atendimento)
print("\nTempos de Resposta:")
for p in processos:
    print(f"{p['processo']}: {tempos_resposta[p['processo']]} unidades de tempo")
#retorna o tempo de retorno
print("\nTempos de Retorno:")
for p in processos:
    print(f"{p['processo']}: {tempos_retorno[p['processo']]} unidades de tempo")

print(f"\nMédia do Tempo de Resposta: {media_tempo_resposta:.2f} unidades de tempo")
print(f"Média do Tempo de Retorno: {media_tempo_retorno:.2f} unidades de tempo")
