# Regras
#   O jogo começa com um número N de pedras (exemplo: 21).
#   Cada jogador pode retirar entre 1 e M pedras por turno (exemplo: entre 1 e 3 pedras).
#   O jogador que retirar a última pedra perde o jogo.

# O jogo pode ter dois modos:
#   Jogador vs. Jogador
#   Jogador vs. Computador (com estratégia)

# user = 0
# computer = 0
# round = 0

# ==============================
# def computerEscolhe (n,m):
#     n=n-m
#     if(n==1):
#         print("computador tirou {n} pedras")
#         print("agora restam {}")

def jogar ():
    n = int(input("Total de pedras:"))
    m = int(input("Max de pedras por turno:"))
    modo = int(input("Modo de jogo: 1- J vs J | 2- J vs Bot"))
    jogador = 0
    
    while n>0:
        print(f'\nPedras Restantes: {n}')
        if modo==2 and jogador==1:
            jogada=1 if n<=m else (n%(m+1) or 1)
            print(f"Bot Tirou {jogada} pedras")
        else:
            jogada = int(input(f"Jogador { jogador + 1 }, retire entre 1 e {min(m,n)} pedras:"))   
            
            
        n -= jogada
        jogador = 1 - jogador
        
    print (f"\nJogador {2 if jogador == 0 else 1} perdeu!")
    
if __name__ == "__main__":
    jogar()