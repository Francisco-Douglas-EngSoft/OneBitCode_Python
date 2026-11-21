# Carrinho de pedidos usando dicionarios.

produtos = {
    "1": {"nome": "Caderno", "preco": 15.90},
    "2": {"nome": "Caneta", "preco": 3.50},
    "3": {"nome": "Mochila", "preco": 89.90},
}

# Cada chave do carrinho e o codigo do produto. O valor guarda produto e quantidade.
carrinho = {}


def listar_produtos():
    print("\n--- Produtos ---")
    for codigo, produto in produtos.items():
        print(f'{codigo} - {produto["nome"]}: R$ {produto["preco"]:.2f}')


def adicionar_ao_carrinho():
    listar_produtos()
    codigo = input("\nDigite o codigo do produto: ")
    produto = produtos.get(codigo)

    if produto is None:
        print("Produto nao encontrado.")
        return

    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Digite uma quantidade valida.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    item = carrinho.setdefault(
        codigo,
        {"nome": produto["nome"], "preco": produto["preco"], "quantidade": 0},
    )
    item["quantidade"] += quantidade
    print(f'{quantidade} unidade(s) de {produto["nome"]} adicionada(s).')


def remover_do_carrinho():
    codigo = input("\nDigite o codigo do produto que deseja remover: ")
    item_removido = carrinho.pop(codigo, None)

    if item_removido is None:
        print("Esse produto nao esta no carrinho.")
    else:
        print(f'{item_removido["nome"]} removido do carrinho.')


def exibir_carrinho():
    if not carrinho:
        print("\nO carrinho esta vazio.")
        return

    print("\n--- Seu carrinho ---")
    total = 0

    for codigo, item in carrinho.items():
        subtotal = item["preco"] * item["quantidade"]
        total += subtotal
        print(
            f'{item["nome"]} (codigo {codigo}) - '
            f'{item["quantidade"]} x R$ {item["preco"]:.2f} = R$ {subtotal:.2f}'
        )

    print(f"Total do pedido: R$ {total:.2f}")


def finalizar_pedido():
    if not carrinho:
        print("\nAdicione pelo menos um produto antes de finalizar.")
        return

    exibir_carrinho()
    print("\nPedido finalizado. Obrigado pela compra!")


def main():
    while True:
        print(
            "\n=== Carrinho de pedidos ==="
            "\n1 - Listar produtos"
            "\n2 - Adicionar produto"
            "\n3 - Remover produto"
            "\n4 - Ver carrinho"
            "\n5 - Finalizar pedido"
            "\n0 - Sair"
        )
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            adicionar_ao_carrinho()
        elif opcao == "3":
            remover_do_carrinho()
        elif opcao == "4":
            exibir_carrinho()
        elif opcao == "5":
            finalizar_pedido()
            if carrinho:
                break
        elif opcao == "0":
            print("Ate mais!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
