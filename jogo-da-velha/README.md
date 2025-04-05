# Jogo da Velha

Este projeto é uma implementação do clássico jogo da velha em Python. O jogo permite que dois jogadores se alternem para marcar espaços em um tabuleiro 3x3, com o objetivo de alinhar três de suas marcas em uma linha, coluna ou diagonal.

## Estrutura do Projeto

O projeto possui a seguinte estrutura de arquivos:

```
jogo-da-velha
├── src
│   ├── main.py       # Ponto de entrada do jogo
│   ├── game.py       # Lógica do jogo
│   └── utils.py      # Funções auxiliares
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
```

## Como Executar o Jogo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos.
3. Navegue até o diretório do projeto.
4. Instale as dependências, se houver, usando o comando:
   ```
   pip install -r requirements.txt
   ```
5. Execute o jogo com o seguinte comando:
   ```
   python src/main.py
   ```

## Funcionamento

- O jogo inicia e solicita que os jogadores escolham suas marcas (X ou O).
- Os jogadores se alternam para fazer suas jogadas.
- O tabuleiro é exibido após cada jogada.
- O jogo verifica se há um vencedor ou se ocorreu um empate após cada jogada.
- Os jogadores podem reiniciar o jogo a qualquer momento.

Divirta-se jogando!