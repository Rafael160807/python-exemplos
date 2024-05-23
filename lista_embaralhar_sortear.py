import random
aluno=['Rafael', 'Joao', 'Lucas', 'Gabriel', 'Mateus', 'Mariana']
# Embaralhar a lista
random.shuffle(aluno)
print(f"Lista Embaralhada: {aluno}")
# Escolher um aluno sorteado
aluno_sorteado = random.choice(aluno)
prinf(f"Aluno sorteado: {aluno_sorteado}")