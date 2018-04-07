package Backend;

import java.util.Random;

public class MotorJogoDaVelha {

    private String tabuleiro[];
    public static String charVazio = "-";
    private boolean gameOver;
    private int[][] regrasJogo;
    private String players[];
    private String playerInicial;
    private String playerTurno;
    private String playerGanhador;
    private String semGanhador;
    private int pontuacaoPlayers[];

    public MotorJogoDaVelha(int[] pontuacaoPlayers)
    {
        this.pontuacaoPlayers = pontuacaoPlayers;

        //Para decidir qual primeiro a jogar
        //Instancia tabuleiro com vazio
        tabuleiro = new String[9];
        for (int i = 0; i < tabuleiro.length; ++i)
        {
            tabuleiro[i] = charVazio;
        }
        Random rand = new Random();

        gameOver = false;
        this.semGanhador = "Ninguém";
        playerGanhador = this.semGanhador;
        players = new String[]
        {
            "X", "O"
        };
        //Seleciona dos players o inicial por random
        playerInicial = players[rand.nextInt(players.length)];
        playerTurno = playerInicial;

        //Regras vão ser os conjuntos
        //de index no qual
        //se tiver algum jogador
        //repetido no index da regra
        //o jogo acaba
        regrasJogo = new int[][]
        {
            {0, 1, 2},{3, 4, 5},
            {6, 7, 8},{0, 4, 8},
            {2, 4, 6},{0, 3, 6},
            {1, 4, 7},{2, 5, 8}
        };
    }

    //Sobrecarga
    public MotorJogoDaVelha(int[] pontuacaoPlayers, String[] players, String semGanhador)
    {
        this(pontuacaoPlayers);
        Random rand = new Random();
        this.semGanhador = semGanhador;
        playerGanhador = semGanhador;
        this.players = players;
        //Seleciona dos players o inicial por random
        playerInicial = players[rand.nextInt(players.length)];
        playerTurno = playerInicial;
    }

    public String getGanhador()
    {
        return playerGanhador;
    }

    public boolean isOver()
    {
        return gameOver;
    }

    public String[] getPlayers()
    {
        return players;
    }

    public int[] getPontuacaoPlayers()
    {
        return pontuacaoPlayers;
    }

    public String getPlayerTurno()
    {
        return playerTurno;
    }

    public String[] getTabuleiro()
    {
        return tabuleiro;
    }

    public boolean atualizaPontuacao()
    {
        int indexGanhador = indexGanhador();
        pontuacaoPlayers[indexGanhador]++;
        return true;
    }

    public boolean fimDeJogo()
    {
        //Pra cada regra do jogo
        for (int[] r : regrasJogo)
        {
            //Se a regra encontra ganhador
            if (tabuleiro[r[0]].equals(tabuleiro[r[1]])
                    && tabuleiro[r[1]].equals(tabuleiro[r[2]])
                    && tabuleiro[r[2]].equals(tabuleiro[r[0]])
                    && !tabuleiro[r[0]].equals(charVazio))
            {
                //Atribui ganhador e game over
                playerGanhador = tabuleiro[r[0]];
                gameOver = true;
                return true;
            }
        }

        //Checa se todo tabuleiro é composto de jogadores
        int i = 0;
        while (i < tabuleiro.length && !tabuleiro[i].equals(charVazio))
        {
            i++;
        }

        //Se contagem de players for igual ao tamanho do tabuleiro
        if (i == tabuleiro.length)
        {
            playerGanhador = "Ninguém";
            gameOver = true;
            return true;
        }

        //Se não caiu em nenhum if então não é fim
        gameOver = false;
        return false;
    }

    public void exibeTabuleiro()
    {
        //Para cada celula do tabuleiro imprima
        for (int i = 0; i < tabuleiro.length; ++i)
        {
            if (i % 3 == 0 && i != 0)
            {
                System.out.println();
            }
            System.out.print(tabuleiro[i] + " ");

        }
    }

    public int indexGanhador()
    {
        //Se p0 = 0, se p1 = 1, resto -1
        if (players[0].equals(playerGanhador))
        {
            return 0;
        }
        else if (players[1].equals(playerGanhador))
        {
            return 1;
        }
        else
        {
            return -1;
        }
    }

    public void atualizaPlayerTurno()
    {
        //Inverte o jogador do turno
        if (playerTurno.equals(players[0]))
        {
            playerTurno = players[1];
        }
        else
        {
            playerTurno = players[0];
        }
    }

    public boolean atualizaTabuleiro(int posicao, String player)
    {
        //Validação da posicao, player e disponibilidade
        if (posicao > 8
                || player.equals(charVazio)
                || !tabuleiro[posicao].equals(charVazio))
        {
            return false;
        }

        //Muda pelo index o player;
        tabuleiro[posicao] = player;
        //Atualiza o player à jogar
        atualizaPlayerTurno();
        return true;
    }
}
