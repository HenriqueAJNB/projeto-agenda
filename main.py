"""Solicita e executa todas as operações da agenda."""

# Criar um menu com as opções abaixo.
# Ler a opção do usuário.

# O que é possível de ser feito com uma agenda?
# 1. Criar contato
# 1.1 Informações do contato:
#       - Primeiro nome, sobrenome, telefone.
# 2. Alterar contato
# 3. Excluir contato
# 4. Pesquisar contato
# 5. Mostrar todos contatos
# 6. Sair da agenda
import pandas as pd

from input_output import grava_no_arquivo, imprime_todos_os_contatos
from menu import solicita_opcao_do_usuario
from opcoes import (
    alterar_contato,
    executa_operacao,
    ler_contato,
    ler_dados_de_pesquisa,
    pesquisar_indice_do_contato_na_agenda,
    remover_contato,
)

print("====== Bem vindo à sua agenda de contatos! ======")

opcao_escolhida = solicita_opcao_do_usuario()

while opcao_escolhida != 6:
    match opcao_escolhida:
        case 1:
            contato = ler_contato()

            grava_no_arquivo(contato)

            print("====== Escolha outra opção ======")
            opcao_escolhida = solicita_opcao_do_usuario()

        case 2:
            executa_operacao(alterar_contato, base_de_contatos)

            print("Informação alterada com sucesso.")
            print("====== Escolha outra opção ======")
            opcao_escolhida = solicita_opcao_do_usuario()

        case 3:
            executa_operacao(remover_contato, base_de_contatos)

            print("Contato deletado com sucesso.")
            print("====== Escolha outra opção ======")
            opcao_escolhida = solicita_opcao_do_usuario()

        case 4:
            nome, sobrenome = ler_dados_de_pesquisa()
            pesquisar_indice_do_contato_na_agenda(
                nome_pesquisado=nome,
                sobrenome_pesquisado=sobrenome,
            )

            print("====== Escolha outra opção ======")
            opcao_escolhida = solicita_opcao_do_usuario()

        case 5:
            imprime_todos_os_contatos()
            print("\n\n====== Escolha outra opção ======")
            opcao_escolhida = solicita_opcao_do_usuario()

        case 6:
            print("Até logo!")
            break

        case _:
            print("Opção inválida!")
            print("====== Escolha outra opção ======")
            opcao_escolhida = solicita_opcao_do_usuario()
