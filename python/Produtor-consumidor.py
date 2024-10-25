import threading
import time
import random

# Definindo o tamanho do buffer
N = 10
buffer = [None] * N
in_pos = 0  # Posição para inserir no buffer
out_pos = 0  # Posição para remover do buffer

# Semáforos
mutex = threading.Semaphore(1)    # Semáforo para exclusão mútua
empty = threading.Semaphore(N)     # Controla espaços vazios (começa com N)
full = threading.Semaphore(0)      # Controla itens no buffer (começa com 0)

# Contadores para total de itens produzidos e consumidos
items_produced = 0
items_consumed = 0

# Tempo de execução do programa
execution_time = 30
start_time = time.time()

def produce_item():
    return random.randint(30,60)

def consume_item(item):
    print(f"Consumindo {item}")

def producer(id):
    global in_pos, items_produced
    while time.time() - start_time < execution_time:
        item = produce_item()  # Produz um item

        # Aguarda espaço no buffer
        empty.acquire()
        # Exclusão mútua para acessar o buffer
        mutex.acquire()

        # Coloca o item no buffer na posição 'in_pos'
        buffer[in_pos] = item
        in_pos = (in_pos + 1) % N  # Move a posição de entrada circularmente
        items_produced += 1

        # Exibe o estado do buffer após a inserção
        print(f"Inserido {item} | {buffer} | {in_pos} | {out_pos} | {empty._value + 1} | {full._value}")

        # Libera acesso ao buffer e sinaliza que há um item no buffer
        mutex.release()
        full.release()

        time.sleep(random.randint(2,3))   # Simula o tempo de produção

def consumer(id):
    global out_pos, items_consumed
    while time.time() - start_time < execution_time:
        # Aguarda por um item no buffer
        full.acquire()
        # Exclusão mútua para acessar o buffer
        mutex.acquire()

        # Remove o item do buffer na posição 'out_pos'
        item = buffer[out_pos]
        buffer[out_pos] = None  # Limpa o buffer na posição removida
        out_pos = (out_pos + 1) % N  # Move a posição de saída circularmente
        items_consumed += 1

        # Exibe o estado do buffer após a remoção
        print(f"Removido {item} | {buffer} | {in_pos} | {out_pos} | {empty._value + 1} | {full._value}")

        # Libera acesso ao buffer e sinaliza que há espaço disponível
        mutex.release()
        empty.release()

        consume_item(item)
        time.sleep(random.randint(2,3))  # Simula o tempo de consumo

def main():
    # Criando e iniciando threads produtoras e consumidoras
    print("Ação  |  inserido  |  Buffer  |  in_Pos  |  out_pos  |  empty | Full")
    producer_threads = [threading.Thread(target=producer, args=(i,)) for i in range(1)]  # numero no final e o numero de produtores
    consumer_threads = [threading.Thread(target=consumer, args=(i,)) for i in range(1)]  # numero no final e o numero de consumidores

    for t in producer_threads:
        t.start()
    for t in consumer_threads:
        t.start()

    # Espera o término das threads
    for t in producer_threads:
        t.join()
    for t in consumer_threads:
        t.join()

    # Exibindo o total de itens produzidos e consumidos
    print(f"Total de itens produzidos: {items_produced}")
    print(f"Total de itens consumidos: {items_consumed}")

if __name__ == '__main__':
    main()
