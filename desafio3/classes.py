class JogoDaVelha():
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.escolhaDoJogador1 = "X"
        self.escolhaDoJogador2 = "O"
        self.matriz = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        self.listaDeJogada = []
        self.rodadas = 1
        self.vitoriaDoJogador1 = 0
        self.vitoriaDoJogador2 = 0

    def imprimir_matriz(self):
        for x in range(3):
            for y in range(3):
                print(self.matriz[x][y], end=" ")
            print()
        print()

    def verificar_vencedor(self, escolha):
        matriz = self.matriz
        return ((matriz[0][0] == escolha and matriz[0][1] == escolha and matriz[0][2] == escolha) or
                (matriz[1][0] == escolha and matriz[1][1] == escolha and matriz[1][2] == escolha) or
                (matriz[2][0] == escolha and matriz[2][1] == escolha and matriz[2][2] == escolha) or
                (matriz[0][0] == escolha and matriz[1][0] == escolha and matriz[2][0] == escolha) or
                (matriz[0][1] == escolha and matriz[1][1] == escolha and matriz[2][1] == escolha) or
                (matriz[0][2] == escolha and matriz[1][2] == escolha and matriz[2][2] == escolha) or
                (matriz[0][0] == escolha and matriz[1][1] == escolha and matriz[2][2] == escolha) or
                (matriz[0][2] == escolha and matriz[1][1] == escolha and matriz[2][0] == escolha))

    def resultado(self):
        print(f"{self.jogador1} = X \n{self.jogador2} = O")
        self.imprimir_matriz()

        while self.rodadas <= 3:
            if self.vitoriaDoJogador1 == 2:
                print(f" {self.jogador1} venceu")
                break
            elif self.vitoriaDoJogador2 == 2:
                print(f"{self.jogador2} venceu")
                break

            print(f"Início da {self.rodadas}ª Rodada:")
            self.rodadas += 1

            for rodada in range(9):

                jogadaDoJogador1 = input(f"Escolha entre 1 e 9 \nQual é a sua jogada {self.jogador1}? ")
                while jogadaDoJogador1 in self.listaDeJogada or jogadaDoJogador1 not in [str(i) for i in range(1, 10)]:
                    jogadaDoJogador1 = input(f"Jogada inválida ou já escolhida. \nQual é a sua jogada {self.jogador1}?v")

                self.listaDeJogada.append(jogadaDoJogador1)
                self.atualizar_matriz(jogadaDoJogador1, self.escolhaDoJogador1)
                self.imprimir_matriz()

                if rodada >= 2 and self.verificar_vencedor(self.escolhaDoJogador1):
                    print(f"{self.jogador1} Venceu")
                    self.vitoriaDoJogador1 += 1
                    print(f"{self.jogador1} - {self.vitoriaDoJogador1} X {self.vitoriaDoJogador2} - {self.jogador2}")
                    self.resetar_jogo()
                    break
                elif rodada == 8:
                    print("Empate")
                    self.resetar_jogo()
                    break


                jogadaDoJogador2 = input(f"Escolha entre 1 e 9 \nQual é a sua jogada {self.jogador2}: ")
                while jogadaDoJogador2 in self.listaDeJogada or jogadaDoJogador2 not in [str(i) for i in range(1, 10)]:
                    jogadaDoJogador2 = input(f"Jogada inválida ou já escolhida. \nQual é a sua jogada {self.jogador2}: ")

                self.listaDeJogada.append(jogadaDoJogador2)
                self.atualizar_matriz(jogadaDoJogador2, self.escolhaDoJogador2)
                self.imprimir_matriz()

                if rodada >= 2 and self.verificar_vencedor(self.escolhaDoJogador2):
                    print(f"{self.jogador2} Venceu")
                    self.vitoriaDoJogador2 += 1
                    print(f"{self.jogador1} - {self.vitoriaDoJogador1} X {self.vitoriaDoJogador2} - {self.jogador2}")
                    self.resetar_jogo()
                    break
                elif rodada == 8:
                    print("Empate")
                    self.resetar_jogo()
                    break

        else:
            if self.vitoriaDoJogador1 < self.vitoriaDoJogador2:
                print(f"Vitória do {self.jogador2}")
            elif self.vitoriaDoJogador1 > self.vitoriaDoJogador2:
                print(f"Vitória do {self.jogador1}")
            else:
                print(f"Jogo encerrado em empate")

    def atualizar_matriz(self, jogada, escolha):
        posicoes = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (2, 0), "8": (2, 1), "9": (2, 2)}
        x, y = posicoes[jogada]
        self.matriz[x][y] = escolha

    def resetar_jogo(self):
        self.matriz = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        self.listaDeJogada = []
        self.imprimir_matriz()