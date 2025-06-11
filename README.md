# Rota

Rota é uma linguagem de programação simples, desenvolvida com o intuito de transformar instruções de caminhos, como vistas em lugares como *Mapas* ou *Google Maps*, em desenhos para visualização fácil do percurso.

Uma das motivações do desenvolvimento dessa linguagem foi o fato de eu ser meio perdido nas ruas de Sâo Paulo. Sempre me vejo olhando rotas em aplicativos, achei que seria interessante uma linguagem que cria um caminho num mapa, poderia ser útil para casos mais específicos (como entregadores).

Feito como APS para a disciplina de Lógica da Computação, 7o semestre de Engenharia da Computação do Insper.

## Como usar

Clone o repositorio
```
git clone https://github.com/rafaelgpaves/LogComp-APS.git
```

Entre na pasta
```
cd LogComp-APS
```

Teste algum arquivo .rota
```
python main.py <arquivo.rota>
```

## EBNF

Veja o [EBNF](EBNF.md)

## Características da linguagem

- "Variáveis" no formato de ruas
    - Cada Rua deve ter apenas uma palavra como nome
- Condicionais
    - Rua esta aberta ou fechada
    - Posição atual é menor ou maior do que um numero
- Se (if) e enquanto (while)
- Output: desenho da rota, mostrado de dois jeitos
    - Após rodar, ele é mostrado automaticamente
    - É salvo num arquivo .png, com o mesmo nome do arquivo de entrada

O "caminho" começa para a direita, mas é possível alterar isso virando em 0 metros.

A condicional de posição atual compara a posição de um eixo só (a de onde está o movimento). Se estiver indo para a direita, a comparação *local maior que 100* irá comparar se x é maior que 100; se estiver indo para baixo, a comparação *local menor que 400* irá comparar se y é menor que 400.

### Algumas peculiaridades

Essa linguagem foi feita para ser o mais próxima possível de uma rota gerada por algum aplicativo de navegação. Isso significa que:
- Não existem comentários
- Não devem existir linhas vazias (só com *\n*), **com exceção da última, que deve ser vazia** (talvez não dê para ver nos exemplos, mas é obrigatório que exista uma linha vazia no final do arquivo)
- Embora na realidade existam avenidas, vias, túneis etc, só foram implementadas ruas.
- Embora na realidade ruas comecem com letra maiúscula e possam ter mais de uma palavra, nesta implementação ruas podem começar com letra minúscula e devem ser uma única palavra

### Exemplos

Veja os exemplos [aqui](./examples/)
