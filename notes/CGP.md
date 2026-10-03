## Mutation (mutação)

No CGP padrão, pode-se utilizar muatação pontual (point mutation) ou mutação probabilística (probabilistic mutation).

Point Mutation: O usuário determina a porcentagem de número total de genes de um genótipo parental a ser mutado para criar descendentes.

Probabilistic Mutation: O usuário define uma probabilidade em que cada gene é considerado para mutação.

A Point Mutation é mais fácil de implementar e mais eficiente do que a Probabilistic Mutation, pois não é necessário percorrer linearmente os genes para decidir quais devem sofrer mutação.

Como muito genes no CGP são redundantes (inativos), frequentemente as mutações ocorrem apens nas regiões reduntantes, o que siginfica que o genótipo mutado possui o mesmo fenótipo que o parental. No entanto, quanto a saída do programa passa vir de um nó anteriormente redundante, que, por sua vez, pode se conectar a genes anteriormente redudantes isso pode causar grande mudanças no fenótipo.


<!-- Gene redundante ou inativo:  -->

### Estratégias de mutação (Goldman e Punch)

*Normal*: Mutação padrão (probabilística), sem verificar se os descendentes (filhos) possuem genótipos idênticos aos parentais (pais).

*Skip*: verifica os descendentes (filhos) para saber se o fenótipo é idêntico ao do parental (comparando os genes ativos) e, se for, retorna a aptidão do parental.

*Accumulate*: Realiza a mutação nos descendentes até que algum de seus genes ativos seja diferente do parental.

*Single **(SAM)***: Realiza mutações no descendente até que um gene ativo seja alterado.


`Viés posicional no CGP`: É muito mais provável que nós no lado esquerdo do genótipo (próximo às estradas) sejam ativos. Isso ocorre simplesmente porque as entradas de qualquer nó à direita de um determinado nó podem ser conectadas a ele. **Por exemplo, o primeiro nó pode ser conectado pela entrada de qualquer nó à sua direita, enquanto o penúltimo nó à direita só pode receber uma conexão do último nó ou de uma saída externa**. Esses vieses fazem com que a localização dos nós inativos no genótipo não seja distribuída uniformemente, e os nós mais à direita (em direção às saídas) tendam a ter muitos nós inativos entre eles.

