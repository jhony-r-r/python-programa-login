login = ["Nome_usuário", "E-mail", "Senha"]

msgEmail = "Digite seu melhor E-mail: "
msgConfirmarEmail = "Confirme seu E-mail: "
msgSenha = "Digite uma senha: "
msgConfirmarSenha = "Confirme sua senha: "

nome = str(input('Digite seu nome de usuário: '))
email = str(input('{}'.format(msgEmail)))
emailC = str(input('{}'.format(msgConfirmarEmail)))
senha = str(input('{}'.format(msgSenha)))
senhaC = str(input('{}'.format(msgConfirmarSenha)))

if email != '' and emailC != '' and senha != '' and senhaC != '':
    if email == emailC and senha == senhaC:
        print('Olá {}, seja Bem Vindo!'.format(nome))

        req = [nome, emailC, senhaC]

        user = dict(zip(login, req))

        entrar = str(input('Deseja entrar em sua conta (Sim ou Não): '))

        if entrar == 'SIM' or entrar == 'Sim' or entrar == 'sim' or entrar == 'S' or entrar == 's':

            reqEmail = str(input('E-mail: '))
            reqSenha = str(input('Senha: '))

            if reqEmail == user.get('E-mail') and reqSenha == user.get('Senha'):
                print('Usuário {} logado com sucesso.'.format(user.get('Nome_usuário')))
            
            else:
                print('E-mail ou senha incorretos.')

        else:
            print('Encerrando sistema...')

    else:
        print('E-mail deve ser idêntico ao confirmar e-mail, mesmo equivale para senha.')

else:
    print('Os campos não devem ser vazios !')