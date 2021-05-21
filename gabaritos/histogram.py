import csv
import numpy as np
from time import sleep

# Lendo o hex da imagem em grayscale
with open('histogram-grayscale.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# Cada entrada do contador armazena a quantidade de vezes que a intensidade
# de cinza se repete
contador = np.zeros(255)

# Contagem da intensidade de cada pixel
for num in data:
    hex_val = num[0][0:2]
    index = int(hex_val, 16) # convertendo hex -> dec
    contador[index] += 1


# Print no formato do simulador visUAL
for num in contador:
    #print(int(num)) # contagem em decimal
    print(hex(int(num)), end=', ') # contagem em hex
