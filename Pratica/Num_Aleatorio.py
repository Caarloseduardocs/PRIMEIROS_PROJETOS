import random

valorAlatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor aleatorio de 1 a 10: '))
    if chute > valorAlatorio:
        print('Valor maior do que o esperado, tente novamente!')
    elif chute < valorAlatorio:
        print('Valor menor do que o esperado, tente novamente!')
    elif chute == valorAlatorio:
        acertou = True
        print('Acertou na mosca!')