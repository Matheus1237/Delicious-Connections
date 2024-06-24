from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5, 'grande')
prato_paozinho = Prato('Paozinho', 2, 'O melhor pão da cidade')
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapip(bebida_suco)
restaurante_praca.adicionar_no_cardapip(prato_paozinho)



def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
