#PROGRAMA QUE LÊ O SEXO DE UMA PESSOA E SÓ ACEITA OS VALORES 'M' OU 'F'
#CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE
sex = str(input('Qual o sexo da pessoa?[M/F] ')).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input('Dados inválidos! Qual o sexo da pessoa?[M/F] ')).strip().upper()[0]
