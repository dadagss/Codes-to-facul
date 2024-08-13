#atividade de Daniel Guimarães Silva 22302201 - Turma B

tempos_resposta = []
tempos_retorno = []
overhead = 1
tempo_atual = 0
ordem = []

#tempo_resposta = tempo_inicio_execucao - tempo_chegada 
#tempo_retorno = tempo_fim_execucao - tempo_chegada 

processos = [
 {"processo": "P1", "arrival_time": 0, "tempo_processo": 1},
 {"processo": "P2", "arrival_time": 0, "tempo_processo": 2},
 {"processo": "P3", "arrival_time": 1, "tempo_processo": 1},
 {"processo": "P4", "arrival_time": 0, "tempo_processo": 15},
 {"processo": "P5", "arrival_time": 2, "tempo_processo": 10},
 ]


#Primeiro irei simular o algoritmo de FIFO

#Organizei os processos de acordo com seu tempo de chegada
processos.sort(key=lambda x: x["arrival_time"])

for processo in processos:
    #o tempo inicial de execução sera o tempo em que ele começa a ser processado - o tempo de chegada dele (-1 para o P3 e -2 para o P5)
    tempo_inicio_execucao = max(tempo_atual,  processo["arrival_time"])

    tempo_resposta = tempo_inicio_execucao - processo["arrival_time"]
    tempos_resposta.append(tempo_resposta)

    #agora iremos pegar ate o fim de sua execução
    tempo_fim_execucao = tempo_inicio_execucao + processo["tempo_processo"] + overhead
    tempo_retorno = tempo_fim_execucao - processo["arrival_time"]
    tempos_retorno.append(tempo_retorno)

    tempo_atual = tempo_fim_execucao

    ordem.append(processo["processo"])

# Calculando as médias de tempo de resposta e de retorno
media_tempo_resposta = sum(tempos_resposta) / len(tempos_resposta)
media_tempo_retorno = sum(tempos_retorno) / len(tempos_retorno)

# Exibindo os resultados
print("FIFO:")
print(f"Ordem de atendimento dos processos: {ordem}")
print(f"Tempo de resposta para cada processo: {tempos_resposta}")
print(f"Tempo de retorno para cada processo: {tempos_retorno}")
print(f"Média de tempo de resposta: {media_tempo_resposta:.2f}")
print(f"Média de tempo de retorno: {media_tempo_retorno:.2f}")

