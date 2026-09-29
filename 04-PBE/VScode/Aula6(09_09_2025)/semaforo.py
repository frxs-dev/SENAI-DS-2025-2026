carro = input("Carro: ")
placa = input("Placa: ")
velocidade = input("Velocidade registrada(km/h): ")
semaforo = input("Estado do semáforo(vermelho/amarelo/verde): ").lower()

if velocidade > 70 or semaforo == "vermelho":
    resposta = "Multa"