import math

from CGPProgram import CGPProgram 
from CGPExecutor import CGPExecutor

def visualize_genome_structure(cgp: CGPProgram):
    """Visualize the structure of a CGP genome."""
    function_nodes, output_connections = cgp.decode_genome()
    
    print("=== CGP Program Structure ===")
    print(f"Inputs: {cgp.n_inputs} (node IDs 0-{cgp.n_inputs-1})")
    print(f"Function nodes: {cgp.n_nodes} (node IDs {cgp.n_inputs}-{cgp.n_inputs+cgp.n_nodes-1})")
    print(f"Outputs: {cgp.n_outputs}")
    print()
    
    print("Function Nodes:")
    for i, (input_x, input_y, func_idx) in enumerate(function_nodes):
        node_id = cgp.n_inputs + i
        func_name = FUNCTION_NAMES[func_idx]
        print(f"  Node {node_id}: {func_name}(node_{input_x}, node_{input_y})")
    
    print(f"\nOutput Connections:")
    for i, output_connection in enumerate(output_connections):
        print(f"  Output {i}: connects to node {output_connection}")



# Define a simple function set
def safe_divide(x, y):
    """Safe division that handles division by zero."""
    if abs(y) < 1e-10:
        return 1.0
    return x / y

def safe_log(x):
    """Safe logarithm that handles negative values."""
    return math.log(abs(x) + 1e-10)

def safe_sqrt(x):
    """Safe square root that handles negative values."""
    return math.sqrt(abs(x))

# Function set for symbolic regression
FUNCTION_SET = [
    lambda x, y: x + y,      # Addition
    lambda x, y: x - y,      # Subtraction  
    lambda x, y: x * y,      # Multiplication
    lambda x, y: safe_divide(x, y),  # Safe division
    lambda x, y: x,          # Identity (return first input)
    lambda x, y: math.sin(x), # Sine
    lambda x, y: math.cos(x), # Cosine
    lambda x, y: safe_log(x), # Safe logarithm
]

FUNCTION_NAMES = ['+', '-', '*', '/', 'id', 'sin', 'cos', 'log']

# Create a simple CGP program
cgp = CGPProgram(n_inputs=2, n_outputs=1, n_nodes=4, function_set=FUNCTION_SET)
genome = cgp.create_random_genome()
print("Random genome:", genome)

cgp.create_random_genome()
visualize_genome_structure(cgp)



executor = CGPExecutor(cgp)
test_inputs = [2.0, 3.0, -1.0]
executor.visualize_execution(test_inputs)