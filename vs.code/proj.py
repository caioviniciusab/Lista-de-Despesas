from datetime import date
rec = {}
des = {}
cont = []
dev = []
tor = 0
tod = 0
agora = date.today().year
print('-' * 30)
print(f'{'OPÇÕES':^30}')
while True:
    print('-' * 30)
    print('1 - ADICIONAR RECEITA')
    print('2 - ADICIONAR DESPESA')
    print('3 - VER SALDO')
    print('4 - VER RESUMO POR CATEGORIA')
    print('5 - SAIR')
    op = int(input('Escolha uma opção: '))
    print('-' * 30)
    if op == 1:
        rec['valor'] = int(input('Digite o valor: R$'))
        rec['descrição'] = input('Tipo: ')
        while True:
            rec['mês'] = input('Mês (1 a 12): ')
            if rec['mês'].isnumeric():
                rec['mês'] = int(rec['mês'])
                if (rec['mês'] >= 1) and (rec['mês'] <= 12):
                    break
                else:
                    print('\033[31mEsse mês não existe. Tente novamente.\033[m')
            else:
                print('\033[31mEscreva em forma numérica.\033[m')
        while True:
            rec['ano'] = input('Ano ex.(2025): ')
            if rec['ano'].isnumeric():
                rec['ano'] = int(rec['ano'])
                if rec['ano'] <= agora:
                    break
                else:
                    print('\033[31mEsse ano é maior que o atual. Tente novamente\033[m.')
            else:
                print('\033[31mEscreva em forma numérica.\033[m')
        tor += rec['valor']
        cont.append(rec.copy())
    elif op == 2:
        des['valor'] = float(input('Digite o valor: R$'))
        des['categoria'] = input('Categoria: ')
        while True:
            des['mês'] = (input('Mês (1 a 12): '))
            if des['mês'].isnumeric():
                des['mês'] = int(des['mês'])
                if (des['mês'] >= 1) and (des['mês'] <= 12):
                    break
                else:
                    print('\033[31mEsse mês não existe. Tente novamente\033[m.')
            else:
                print('\033[31mEscreva em forma numérica.\033[m')
        while True:
            des['ano'] = input('Ano ex.(2025): ')
            if des['ano'].isnumeric():
                des['ano'] = int(des['ano'])
                if des['ano'] <= agora:
                    break
                else:
                    print('\033[31mEsse ano é maior que o atual. Tente novamente\033[m.')
            else:
                print('\033[31mEscreva em forma numérica.\033[m')
        dev.append(des.copy())
        tod += des['valor']
    elif op == 3:
        tot = tor - tod
        if tot >= 0:
            print(f'Seu saldo é \033[32m{tot:.2f}R$\033[m')
        else:
            print(f'Seu saldo é \033[31m{tot:.2f}R$\033[m')
    elif op == 4:
        if tod == 0:
            print('Você não adicionou nenhuma despesa ainda. Tente novamente.')
        else:
            for c in range(0, len(dev)):
                print(f'Você gastou \033[31m{dev[c]['valor']:.2f}R$\033[m em \033[33m{dev[c]['categoria']}\033[m.')
    elif op > 5 or op < 1:
        print('Essa opção não existe. Tente novamente.')
    elif op == 5:
        print('Volte sempre. Tenha um ótimo dia!')
        break