def verificar_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    else:
        return False

def main():
    ano = int(input("Digite o ano que deseja verificar: "))

    if verificar_bissexto(ano):
        print("O ano {} é bissexto, pois segue as seguintes condições:".format(ano))
        print("- É divisível por 4;")
        if ano % 100 == 0 and ano % 400 != 0:
            print("- É divisível por 100, mas não por 400.")
        else:
            print("- Não é divisível por 100 ou é divisível por 400.")
        print("Portanto, possui 366 dias.")
    else:
        print("O ano {} não é bissexto, pois não segue as condições necessárias.".format(ano))
        print("Portanto, possui 365 dias.")

if __name__ == "__main__":
    main()

    # Neste programa a função 'verificar_bissexto()' verifica-se o ano fornecido pelo usuário é bissexto, seguindo as regras do calendário gregoriano.
    # Em seguida, na função principal'main()', soliciamos ao usuário que insira o ano desejado. Se o ano for bissexto, explicamos 
    # as condições que ela atende para ser considerado bissexto e que possui 366 dias . Caso contrário , explicamos que ele não atende
    # as condições e que possui 365 dias 