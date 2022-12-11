"""Funções utilitárias para o menu da agenda."""


def solicita_opcao_do_usuario():
    """Solicita uma das opcoes de 1 a 6 do usuario.

    [1] - Criar um contato novo
    [2] - Alterar um contato existente
    [3] - Excluir um contato
    [4] - Pesquisar por um contato
    [5] - Mostrar todos os contatos armazenados
    [6] - Sair da agenda

    Returns
    -------
    int
        Opcao escolhida pelo usuario
    """
    print(" [1] - Criar um contato novo")
    print(" [2] - Alterar um contato existente")
    print(" [3] - Excluir um contato")
    print(" [4] - Pesquisar por um contato")
    print(" [5] - Mostrar todos os contatos armazenados")
    print(" [6] - Sair da agenda")

    # TODO: incluir validações de entrada do usuário.

    opcao_escolhida = int(input("Selecione o número da opção acima desejada: "))

    return opcao_escolhida
