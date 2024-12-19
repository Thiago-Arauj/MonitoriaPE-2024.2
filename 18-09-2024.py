# 1047 beecrowd Arthur Marques

hora_init, min_init, hora_end, min_end = input().split()

# Horas
hora_init = int(hora_init)
hora_end = int(hora_end)

# Minutos
min_init = int(min_init)
min_end = int(min_end)


#Transformando as horas em minutos
hora_to_min_init = hora_init * 60
hora_to_min_end = hora_end * 60

# Somando tudo
total_init = hora_to_min_init + min_init
total_end = hora_to_min_end + min_end

if total_end < total_init:
    total_min = total

elif total_end > total_init:
    pass

else:
    pass 