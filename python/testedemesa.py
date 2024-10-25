# Produtor-Consumidor

N = 10
buffer[N]
count = 0

procedure producer():
    while TRUE:
        if count < N:
            item = produce_item()
            buffer[count] = item
            count = count + 1

procedure consumer():
    while TRUE:
        if count > 0:
            item = buffer[count - 1]
            consume_item(item)