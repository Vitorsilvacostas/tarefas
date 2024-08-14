velocidade = float(input('qual e a sua velocidade?'))
if velocidade <=88:
    print('ok, sem problemas')
elif velocidade >88:
    print('voçe sera multado!!!!')
    qtdemulta = velocidade - 80.0
    valormulta =7.0 * qtdemulta
    print('voce pagara r${:.2f}'.format(valormulta))
    print('fim do programa')