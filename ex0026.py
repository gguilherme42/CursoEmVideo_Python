print('=== DESAFIO 026 ===')
fr = str(input('Digite uma pequena frase: ')).strip().lower()
print('A letra "A" aparece {} vezes'.format(fr.count('a')))
print('A primeira posição que ela aparece é {}'.format(fr.find('a') + 1))
print('A última posição que ela aparece é {}'.format(fr.rfind('a') + 1 - fr.count(' ')))