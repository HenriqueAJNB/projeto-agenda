"""Funções utilitárias para leitura e escrita em arquivos."""


def grava_no_arquivo(contato: str) -> None:
    """Adiciona o contato ao aquivo.

    Parameters
    ----------
    contato : str
        Texto com nome, sobrenome e telefone.
    """
    with open("contatos.csv", mode="a", encoding="utf-8") as contacts_file:
        contacts_file.writelines(f"{contato}\n")

    print("Contato adicionado com sucesso.")


def imprime_todos_os_contatos() -> None:
    """Imprime todos os contatos da lista."""
    with open("contatos.csv", mode="r", encoding="utf-8") as contacts_file:
        lista_contatos = contacts_file.readlines()

    for contato in lista_contatos:
        print(contato.replace("\n", ""))
