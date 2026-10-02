## Mutation (mutação)

No CGP padrão, pode-se utilizar muatação pontual (point mutation) ou mutação probabilística (probabilistic mutation).

Point Mutation: O usuário determina a porcentagem de número total de genes de um genótipo parental a ser mutado para criar descendentes.

Probabilistic Mutation: O usuário define uma probabilidade em que cada gene é considerado para mutação.

A Point Mutation é mais fácil de implementar e mais eficiente do que a Probabilistic Mutation, pois não é necessário percorrer linearmente os genes para decidir quais devem sofrer mutação.

Como muito genes no CGP são redundantes (inativos), frequentemente as mutações ocorrem apens nas regiões reduntantes, o que siginfica que o genótipo mutado possui o mesmo fenótipo que o parental. No entanto, quanto a saída do programa passa vir de um nó anteriormente redundante, que, por sua vez, pode se conectar a genes anteriormente redudantes isso pode causar grande mudanças no fenótipo.


<!-- Gene redundante ou inativo:  -->

Estratégias de mutação