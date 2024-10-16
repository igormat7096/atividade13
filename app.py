if __name__ == "__main__":
 import os 
 from calcularadora import exebir_menu
 from calcularadora import calcular_potencia
 from calcularadora import calcular_raiz


while True:
     nome = input("Informe seu nome: ")
     print(f"{nome} o que vc deseja fazer")
     exebir_menu()
     opcao = input("Opção desejada: ")

     os.system("cls")
 
     match opcao:
        
        case "1":
            numero1 = int(input("Informe o numero base da potência: ").replace(",","."))
            numero2 = int(input("Informe o numero expoente da potência: ").replace(",","."))
            print(calcular_potencia(numero1, numero2))
            continue
        case "2":
            numero3 = int(input("Informe o numero para calcular a raiz quadrada: ").replace(",","."))
            print(calcular_raiz(numero3))
            continue
            
        case "3":
          print("Obrigado volte sempre!")
            break
        case _:
            print("Opção inválida.")
