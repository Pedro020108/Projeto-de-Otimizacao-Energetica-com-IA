# Entradas simuladas
rede = int(input("Rede elétrica disponível? (1 = sim, 0 = não): "))
bateria = int(input("Bateria em nível seguro? (1 = sim, 0 = não): "))

# Processamento lógico
if not rede or not bateria:
    print("Modo sobrevivência ativado!")
    print("Ligar apenas cargas essenciais: Iluminação, Roteador")
    print("Desligar cargas não essenciais: Ventilador, Bomba")
else:
    print("Modo normal ativado.")
    print("Todas as cargas estão ligadas.")