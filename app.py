def dimensaoObjeto():
    while True:
        try:
            comprimento = int(
                input("Digite o comprimento do objeto(em cm):\n"))
            largura = int(input("Digite a largura do objeto(em cm):\n"))
            altura = int(input("Digite a altura do objeto(em cm):\n"))
            volume = comprimento*largura*altura
            if 0 <= volume < 1000:
                print("O volume do objeto (em cm): {:.2f}".format(volume))
                return 10.00
            elif (volume >= 1001) and (volume <= 10000):
                print("O volume do objeto (em cm): {:.2f}".format(volume))
                return 20.00
            elif (volume >= 1000) and (volume <= 30000):
                print("O volume do objeto (em cm): {:.2f}".format(volume))
                return 30.00
            elif (volume >= 30001) and (volume <= 100000):
                print("O volume do objeto (em cm): {:.2f}".format(volume))
                return 50.00
            else:
                volume > 100000
                print('Não aceitamos objetos com dimensões tão grande!')
                continue
        except ValueError:
            print('Pare de digitar valores não numericos. Tente novamente')
            continue
def pesoObjeto():
    while True:
        try:
            pesoVolume = float(input("Digite o peso do objeto (em kg): \n"))
            if 0 <= pesoVolume <= 0.1:
                print("Objeto em kilos é de {:.2f}".format(pesoVolume))
                return 1.0
            elif (pesoVolume >= 0.11) and (pesoVolume <= 1.00):
                print("Objeto em kilos é de {:.2f}".format(pesoVolume))
                return 1.5
            elif (pesoVolume >= 1.10) and (pesoVolume <= 10.00):
                print("Objeto em kilos é de {:.2f}".format(pesoVolume))
                return 2.0
            elif (pesoVolume >= 10.01) and (pesoVolume <= 30.00):
                print("Objeto em kilos é de {:.2f}".format(pesoVolume))
                return 3.0
            else:
                pesoVolume > 30.00
                print('Não aceitamos objetos tão pesados.')
                continue
        except ValueError:
            print('Pare de digitar valores não numericos. Tente novamente')
            continue
def rotaObjeto():
    while True:
        rota = input("Selecione a rota: \nRS - De Rio de Janeiro até São Paulo \nSR - De São Paulo até Rio de Janeiro\nBS - De Brasília até São Paulo\nSB - De São Paulo até Brasília\nBR - De Brasília até Rio de Janeiro\nRB - Rio de Janeiro até Brasília\n")
        if rota == "rs":
            return 1.0
        elif rota == "sr":
            return 1.0
        elif rota == "bs":
            return 1.2
        elif rota == "sb":
            return 1.2
        elif rota == "br":
            return 1.5
        elif rota == "rb":
            return 1.5
        else:
            print("Pare de digitar rotas que nao existem")
# continuee digitar valores nao numericos. Tente novamente')
            continue
print('Bem vindo a Logistica RA S.A.')
volumeObjeto = dimensaoObjeto()
pesoKg = pesoObjeto()
rota = rotaObjeto()
total = volumeObjeto * pesoKg * rota
print("O valor total a pagar (R$) {:.2f} (dimensões: {} * peso: {} * rota: {})".format(total,volumeObjeto, pesoKg, rota))
