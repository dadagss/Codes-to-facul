#atividade de Daniel Guimarães Silva - Turma B
processos = [
    {"processo": "P1", "arrival_time": 0, "tempo_processo": 1},
    {"processo": "P2", "arrival_time": 0, "tempo_processo": 2},
    {"processo": "P3", "arrival_time": 1, "tempo_processo": 1},
    {"processo": "P4", "arrival_time": 0, "tempo_processo": 15},
    {"processo": "P5", "arrival_time": 2, "tempo_processo": 10},
]


tempos_resposta = {}
tempos_retorno = {}
tempos_espera = {}
overhead = 1
tempo_atual = 0
quantum = 2
ordem = []
prontos = []

# Adiciona processos à fila de prontos com base no tempo de chegada
def adicionar_na_fila():
    for processo in processos:
        if processo["arrival_time"] <= tempo_atual and processo["processo"] not in [p["processo"] for p in prontos]:
            prontos.append(processo)

# Executa a simulação Round Robin
while processos or prontos:
    adicionar_na_fila()
    
    if prontos:
        processo_atual = prontos.pop(0)
        nome_processo = processo_atual["processo"]
        
        if nome_processo not in tempos_resposta:
            tempos_resposta[nome_processo] = tempo_atual - processo_atual["arrival_time"]
        
        tempo_execucao = min(quantum, processo_atual["tempo_processo"])
        
        # Atualiza o tempo de execução
        tempo_atual += tempo_execucao
        processo_atual["tempo_processo"] -= tempo_execucao
        
        if processo_atual["tempo_processo"] > 0:
            # Adiciona o processo de volta à fila se ainda restar tempo
            processo_atual["arrival_time"] = tempo_atual
            prontos.append(processo_atual)
        else:
            # Calcula o tempo de retorno
            tempos_retorno[nome_processo] = tempo_atual - processo_atual["arrival_time"]
        
        # Adiciona o processo à ordem de atendimento
        ordem.append(nome_processo)
        
        # Aplica o overhead
        tempo_atual += overhead

# Calcula o tempo de espera para cada processo
for processo in processos:
    nome_processo = processo["processo"]
    if nome_processo in tempos_retorno and nome_processo in tempos_resposta:
        tempos_espera[nome_processo] = tempos_retorno[nome_processo] - processo["tempo_processo"] - tempos_resposta[nome_processo]
    else:
        tempos_espera[nome_processo] = 0  # Se o processo não foi completado

# Calcula as médias dos tempos
media_tempo_resposta = sum(tempos_resposta.values()) / len(tempos_resposta) 
media_tempo_retorno = sum(tempos_retorno.values()) / len(tempos_retorno) 
media_tempo_espera = sum(tempos_espera.values()) / len(tempos_espera) 

# Exibindo os resultados
print("Round Robin:")
print(f"Ordem de atendimento dos processos: {ordem}")
print(f"Tempo de resposta para cada processo: {tempos_resposta}")
print(f"Tempo de retorno para cada processo: {tempos_retorno}")
print(f"Tempo de espera para cada processo: {tempos_espera}")
print(f"Média de tempo de resposta: {media_tempo_resposta:.2f}")
print(f"Média de tempo de retorno: {media_tempo_retorno:.2f}")
print(f"Média de tempo de espera: {media_tempo_espera:.2f}")
