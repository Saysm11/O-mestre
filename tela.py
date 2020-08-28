# Dica, se vc apertar control + ; comenta a linha selecionada
# temos que fazer
# apresentação(miss)
def criaPersonagem():
#jogador = {nome , inclinaçao, classe, karma, tempo de vida e destreza(aqui entra a força etc) } -> ok vou incluir isso tudo -> mas me diz oq acha
    jogador = {'nome': ' ',
                'vida': 10,
                'inclinacao': 'Lawful good',  
                'classe': ' ',
                'força': 5,
                'karma': 'nulo de inicio', #suas decisoes caso sejam contradizacentes com sua inclinaçao vai ter um karma que vai ser algum Debuff'
                'tempoVida': 100,#Vai ser dado por escolhas(quanto mais coerentes forem elas mais ele vai ter)  
                'especie': 'humano',
                'detreza': 5 #vai escalar com a quantidade de escolhas que a pessoa vai ter no inicio eu penso em 3 sabe mas dps a medida que a pessoa vaise arriscando ela vai tendo opçoes mais perigosas -> hmm entendi, bom temos que anotar tudo isso e decidir certinho pra podermos montar
                }
    return jogador

def inicio():
    nome = input("Seja bem-vindo ao jogo, poderia me dizer seu nome?")
    print("Olá {nome}, vamos começar o jogo, não existem regras, apenas lembre que tudo importa e trás consequências.")
    # entra aqui a função de botar os valores pra variavel de jogador
    # chama a primeira cena - ok 

# personagem(as coisinhas dele e tals) (miss)
# primeira cena (says)
# primeira decisão (says)
