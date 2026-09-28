def decodificar_e_avaliar_cgp(genotipo, entradas, funcoes):
    """
    Decodifica o genótipo do CGP (ativação reversa) e avalia o fenótipo.
    """
    num_entradas = len(entradas)
    genes_nos = genotipo[:-1]       # Lista de tuplas com os nós funcionais
    no_saida_idx = genotipo[-1]    # Endereço apontado pelo gene de saída
    
    # -------------------------------------------------------------
    # 1. BUSCA REVERSA: Identifica apenas os nós ativos (Fenótipo)
    # -------------------------------------------------------------
    nos_ativos = set()
    a_visitar = [no_saida_idx]
    
    while a_visitar:
        atual = a_visitar.pop()
        # Se for um nó funcional (endereço >= número de entradas)
        if atual >= num_entradas:
            nos_ativos.add(atual)
            idx_no = atual - num_entradas
            f, in1, in2 = genes_nos[idx_no]
            
            # Adiciona as conexões para verificação se ainda não foram visitadas
            if in1 >= num_entradas and in1 not in nos_ativos:
                a_visitar.append(in1)
            if in2 >= num_entradas and in2 not in nos_ativos:
                a_visitar.append(in2)

    # -------------------------------------------------------------
    # 2. AVALIAÇÃO: Executa os nós na ordem de criação
    # -------------------------------------------------------------
    valores_nos = dict(entradas) # Guarda valores {endereço: valor}
    
    print("--- PROCESSAMENTO DO GENÓTIPO ---")
    for idx, (f, in1, in2) in enumerate(genes_nos):
        no_id = num_entradas + idx
        e_ativo = no_id in nos_ativos
        
        if e_ativo:
            v1 = valores_nos[in1]
            v2 = valores_nos[in2]
            op_func, op_simbolo = funcoes[f]
            resultado = op_func(v1, v2)
            valores_nos[no_id] = resultado
            print(f"Nó {no_id} [ATIVO]   : Nó({in1}) {op_simbolo} Nó({in2})  =>  {v1} {op_simbolo} {v2} = {resultado}")
        else:
            print(f"Nó {no_id} [INATIVO] : Ignorado (não conectado à saída)")

    resultado_final = valores_nos[no_saida_idx]
    print(f"\nResultado Final na Saída (Nó {no_saida_idx}): {resultado_final}")
    return resultado_final, nos_ativos


# =====================================================================
# CONFIGURAÇÃO DO EXPERIMENTO
# =====================================================================

# Tabela de Funções: {ID: (função_lambda, símbolo_str)}
funcoes = {
    0: (lambda a, b: a + b, "+"),
    1: (lambda a, b: a - b, "-"),
    2: (lambda a, b: a * b, "*"),
    3: (lambda a, b: a / b if b != 0 else 1.0, "/")
}

# Genótipo do Exemplo:
# Estrutura de cada nó: (código_função, entrada_1, entrada_2)
genotipo = [
    (0, 0, 1),  # Nó 2: Soma x0 (0) e x1 (1)
    (1, 1, 0),  # Nó 3: Subtrai x0 (0) de x1 (1)
    (2, 2, 3),  # Nó 4: Multiplica Nó 2 e Nó 3
    (3, 0, 1),  # Nó 5: Divisão (Nó Inativo)
    4           # Gene de Saída: Aponta para o Nó 4
]

# Entradas Primárias: x0 (endereço 0) = 3, x1 (endereço 1) = 5
entradas = {0: 3, 1: 5}

# Execução
print(f"Entradas: x0 = {entradas[0]}, x1 = {entradas[1]}\n")
resultado, ativos = decodificar_e_avaliar_cgp(genotipo, entradas, funcoes)