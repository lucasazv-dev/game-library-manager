import json

def carregar_jogos():
    try:
        with open('listgames.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('ERRO: arquivo corrompido. Iniciando lista vazia.')
        return []

def salvar_jogos(jogos):
    with open('listgames.json', 'w', encoding='utf-8') as arquivo:
        json.dump(jogos, arquivo, indent=4, ensure_ascii=False)

jogos = carregar_jogos()

while True:
    comando = input('Digite um comando. (ABOUT/ADD/LIST/UPDATE/DELETE/QUIT) ').upper()

    if comando == 'ABOUT':
        print('Seja bem vindo(a) ao software de jogos de Lucas Azevedo!')

    elif comando == 'QUIT':
        salvar_jogos(jogos)
        print('Saindo do sistema!')
        break

    elif comando == 'ADD':
        try:
            total_jogos = int(input('Quantos jogos você gostaria de adicionar para jogar futuramente? '))
        except ValueError:
            print('ERRO: formato inválido.')
            continue
        if total_jogos <= 0:
            print('Total de jogos inválidos! Tente novamente!')
        else:
            for jogo in range(total_jogos):
                nome_jogo = input('Qual o nome do jogo que você gostaria de adicionar a lista? ')

                cadastro_nome_jogo = {
                    'nome': nome_jogo,
                    'concluido': False,
                    'historico': []
                }

                if nome_jogo:
                    jogos.append(cadastro_nome_jogo)
                    print(f'Legal, "{nome_jogo}" adicionado a lista de jogos com sucesso!')

    elif comando == 'LIST':
        if len(jogos) == 0:
            print('Sua lista de jogos está vazia! Que tal adicionarmos algum? ')
        else:
            print(' Lista de jogos:')

            for jogo in jogos:
                print(f'Nome: {jogo['nome']}')
                print(f'Concluído: {"Sim" if jogo["concluido"] else "Não"}')

                if len(jogo['historico']) == 0:
                    print('Histórico: vazio')
                else:
                        print('Histórico')
                        for data, nome, concluido in jogo['historico']:
                            print(f' - {data} | {nome} | {"Sim" if concluido else "Não"}')

                print('-' * 30)

    elif comando == 'UPDATE':
        nome_jogo_para_modificar = input('Qual o nome do jogo que você gostaria de modificar? ')
        jogo_para_modificar = None

        for jogo in jogos:
            if jogo['nome'] != nome_jogo_para_modificar:
                continue
            jogo_para_modificar = jogo
            break
        else:
            print('Jogo não encontrado!')

        if jogo_para_modificar is not None:
            jogo_para_modificar['nome'] = input('Qual o novo nome para o jogo? ')

        while True:
            try:
                valor = int(input('Esse jogo já foi jogado antes? (1 = SIM / 0 = NÃO) '))
                if valor in (0, 1):
                    jogo_para_modificar['concluido'] = bool(valor)
                    break
                else:
                    print('Por favor, digite apenas 1 ou 0.')
            except ValueError:
                print('ERRO: formato inválido.')

        data_modificacao = input('Qual a data de hoje? ')
        atualizacao = (data_modificacao, jogo_para_modificar['nome'], jogo_para_modificar['concluido'])
        jogo_para_modificar['historico'].append(atualizacao)

    elif comando == 'DELETE':
        nome_jogo_para_deletar = input('Qual o jogo que você gostaria de deletar? ')
        jogo_para_deletar = None

        for jogo in jogos:
            if jogo['nome'] == nome_jogo_para_deletar:
                jogo_para_deletar = jogo
                break

        if jogo_para_deletar is not None:
            jogos.remove(jogo_para_deletar)
            print(f'Jogo {jogo_para_deletar["nome"]} deletado com sucesso!')
        else:
            print('Jogo não encontrado!')

    else:
        print('ERRO:Comando desconhecido.')

print('Até a próxima!')