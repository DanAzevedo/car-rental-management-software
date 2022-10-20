import os
import sys

cars: list = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130)
]

rent = []


def show_car_list(cars_list):
    for i, car in enumerate(cars_list):
        print("[{}] {} - R$ {} /por dia".format(i, car[0], car[1]))


while True:
    os.system("Clear")
    print("==========")
    print("Bem vindo à locadora de carros!")
    print("==========")
    print("O que deseja fazer?")
    print("-------------------------------------------------------------------------------\n")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro | 3 - Sair do sistema")
    op = int(input())
    os.system("Clear")
    # =============================================================================================================
    # OPÇÃO 0
    if op == 0:
        show_car_list(cars)
    # =============================================================================================================
    # OPÇÃO 1
    elif op == 1:
        print("[ ALUGAR ] Dê uma olhada em nosso portifólio.\n")
        show_car_list(cars)
        print("\n")
        cod = int(input("Escolha o código do carro:\n"))
        days = int(input("Escolha por quantos dias deseja alugar:\n"))
        os.system("Clear")

        print("Você escolheu {} por {} dias.".format(cars[cod][0], days))
        print("O aluguel totalizaria R$ {}. Deseja alugar?".format(days * cars[cod][1]))
        print("-------------------------------------------------------------------------------")
        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        # OPÇÃO 0.0
        if conf == 0:
            print("Parabéns! Você alugou o {} por {} dias.".format(cars[cod][0], days))
            rent.append(cars.pop(cod))
            print("-------------------------------------------------------------------------------")
    # =============================================================================================================
    # OPÇÃO 2
    elif op == 2:
        if len(rent) == 0:
            print("Não há carros para devolver.")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?\n")
            show_car_list(rent)
            print("\n")
            cod = int(input("Digite o código de qual deseja devolver:"))
            if conf == 0:
                print("Obrigado por devolver o carro {}".format(rent[cod][0]))
                cars.append(rent.pop(cod))
    # =============================================================================================================
    # OPÇÃO 3
    elif op == 3:
        print("Saindo do sistema...")
        sys.exit()
    # =============================================================================================================
    # OPÇÃO INVÁLIDA
    else:
        print("Operação inválida!")
