
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Resposta inválida, porfavor informe seu sexo: '))
print(f'Sexo {sexo} registrado com sucesso.')
