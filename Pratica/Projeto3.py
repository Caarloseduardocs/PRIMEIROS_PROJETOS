veloMaxPerm = 80
veloUsuario = int(input('Coloque a velocidade que estava andando? '))

if veloUsuario <= veloMaxPerm:
    print('Não levou multa')
elif veloUsuario > veloMaxPerm and veloUsuario <= veloMaxPerm + 10:
    print('Levou multa leve')
elif veloUsuario >= veloMaxPerm + 11 and veloUsuario <= veloMaxPerm + 20:
    print('Levou multa grave')
elif veloUsuario > veloMaxPerm + 20:
    print('Levou multa gravíssima')