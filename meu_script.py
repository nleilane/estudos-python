altura = float( input("Digite sua altura"))
peso = float(input("Digite seu peso"))
imc = peso / (altura*altura)
print(imc)
if imc < 18.5:
    print("Seu IMC é abaixo do peso ideal")
if imc >= 18.5 and imc < 25:
    print("Seu IMC está ideal")
if imc >= 25 and imc < 30:
    print("Seu IMC é sobrepeso")
if imc >= 30 and imc < 40:
    print("Seu IMC é obesidade")
if imc >= 40:
    print("Seu IMC é obesidade grave")