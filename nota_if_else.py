nota1 = int(input("Informe a nota do 1º Bimestre (0-100): "))
nota2 = int(input("Informe a nota do 2º Bimestre (0-100): "))
media = (nota1+nota2) / 2 
if media >= 60:
    print(f"Voce foi aprovado com a media {media}")
else:
    print(f"Voce não foi aprovado, sua média é {media}")