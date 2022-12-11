"""Funções relacionadas às opções do menu da agenda."""

from typing import Callable

from menu import solicita_opcao_do_usuario


def ler_contato() -> str:
    """Lê nome, sobrenome e telefone informado pelo usuario.

    Returns
    -------
    str
        Lista com nome, sobrenome e telefone fonecidos pelo usuario.
    """
    print("Informações do novo contato:")
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    print("Para o telefone, digite neste formato: DDD (sem o zero) + somente números")
    print("Exemplo: 9933332222 ou 11912345678")

    # TODO: validar se o telefone informado contém apenas números
    # TODO: validar se tem 10 ou 11 dígitos
    telefone = int(input("Digite o telefone: "))

    contato = f"{nome},{sobrenome},{telefone}"

    return contato


def adicionar_contato_na_agenda(base_de_contatos: list) -> int:
    """Lê um contato do usuário e o coloca na agenda.

    Parameters
    ----------
    base_de_contatos : list
        Agenda

    Returns
    -------
    int
        Opção para próxima operação
    """
    contato = ler_contato()

    base_de_contatos.append(contato)

    print("Contato adicionado com sucesso.")

    print("====== Escolha outra opção ======")
    opcao_escolhida = solicita_opcao_do_usuario()
    return opcao_escolhida


def ler_dados_de_pesquisa() -> tuple[str, str]:
    """Lê do usuário o nome e sobrenome a ser buscados.

    Returns
    -------
    tuple[str, str]
        Tupla com nome e sobrenome informados pelo usuário
    """
    nome = input("Digite o nome do contato procurado: ")
    sobrenome = input("Digite o sobrenome do contato procurado: ")
    return nome, sobrenome


def imprime_informacoes_contato(contato: list) -> None:
    """Imprime as informações de nome, sobrenome e telefone de contato.

    Parameters
    ----------
    contato : list
        Lista do contato.
    """
    nome = contato[0]
    sobrenome = contato[1]
    telefone = contato[2]
    print(f"Nome: {nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Telefone: {telefone}")


def pesquisar_indice_do_contato_na_agenda(
    nome_pesquisado: str, sobrenome_pesquisado: str
) -> int | None:
    """Busca o contato de acordo com a linha do arquivo.

    Parameters
    ----------
    nome_pesquisado : str
        Nome informado pelo usuário a ser pesquisado.
    sobrenome_pesquisado : str
        Sobrenome informado pelo usuário a ser pesquisado.

    Returns
    -------
    int | None
        Caso ele encontre, retorna o índice do contato na agenda. Se não encontrar, retorna None
    """

    with open("contatos.csv", mode="r", encoding="utf-8") as contacts_file:
        lista_contatos = contacts_file.readlines()

    # ["Henrique,Branco,123456789", "Silvio,Cezarotto,987654321", ...]

    for idx, contato in enumerate(lista_contatos):

        nome = contato.split(",")[0]
        sobrenome = contato.split(",")[1]

        contato_foi_encontrado = (
            nome == nome_pesquisado and sobrenome == sobrenome_pesquisado
        )
        if contato_foi_encontrado:
            return idx

    if not contato_foi_encontrado:
        print("Seu contato não foi encontrado na base.")
        return None


def alterar_contato(indice_contato):
    """Altera uma das informações (nome, sobrenome ou telefone) de um contato que o usuário fornecer

    Parameters
    ----------
    indice_contato : int
        Indice do contato a ser alterado na lista de contatos
    """
    print("O que você deseja alterar?")
    print("[1] Nome")
    print("[2] Sobrenome")
    print("[3] Telefone")
    opcao = int(input("Selecione uma opção: "))
    nova_info = input("Qual será a nova informação?")

    with open("contatos.csv", mode="w", encoding="utf-8") as contacts_file:
        lista_contatos = contacts_file.readlines()

    contato_a_ser_alterado = lista_contatos[indice_contato]

    # contato_a_ser_alterado = "Silvio,Cezarotto,987654321"

    nome = contato_a_ser_alterado.split(",")[0]
    sobrenome = contato_a_ser_alterado.split(",")[1]
    telefone = contato_a_ser_alterado.split(",")[2]

    match opcao:
        case 1:
            nome = nova_info
        case 2:
            sobrenome = nova_info
        case 3:
            telefone = nova_info


def remover_contato(base_de_contatos: list, indice_contato: int):
    """Remove um contato da base.

    Parameters
    ----------
    base_de_contatos : list
        Agenda de contatos
    indice_contato : int
        Indice do contato a ser removido.
    """
    del base_de_contatos[indice_contato]


def executa_operacao(operacao: Callable, base_de_contatos: list):
    """Executa uma das operações do menu da agenda.

    Parameters
    ----------
    operacao : Callable
        Operação a ser executada
    base_de_contatos : list
        Agenda de contatos.
    """
    nome, sobrenome = ler_dados_de_pesquisa()
    indice_contato = pesquisar_indice_do_contato_na_agenda(
        nome_pesquisado=nome,
        sobrenome_pesquisado=sobrenome,
    )

    operacao(base_de_contatos, indice_contato)


indice = pesquisar_indice_do_contato_na_agenda("Mirian", "Guerra")

if indice is not None:
    with open("contatos.csv", mode="r", encoding="utf-8") as file:
        print(file.readlines()[indice])
