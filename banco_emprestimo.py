print(f"Programa de emprestimo\n" f"Responda: (0-Não ou 1-Sim)")
nome_negativado=int(input("Possui nome negativado?: "))
if nome_negativado == 1 :
    print("Não pode realizar emprestimo")
else:
    carteira_assinada=int(input("Possui Carteira Assinada?: "))
    if carteira_assinada == 0 :
        print("Não pode realizar emprestimo")
    else:
        if casa_propria == 0:
            print("Não pode realizar emprestimo")
        else:
            print("Conceder Emprestimo")