medias = []
for bimestre in range(1, 5):
    print (str (bimestre)+" Bimestre")
   
    nota1 = float (input("Digite a primeira nota"))
    nota2 = float (input("Digite a segunda nota"))
    media = (nota1 + nota2) / 2
    medias.append(media)
soma = medias[0] + medias[1] + medias[2] + medias[3]
mediaFinal = soma/4

print(f"Média final é"+ str (mediaFinal))

if mediaFinal > 6:
    print("Aprovado")
if 4 < mediaFinal < 6:
    print("Recuperação")
if mediaFinal < 3.5:
    print("Reprovado")