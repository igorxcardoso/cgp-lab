import numpy as np
import random
import math
import matplotlib.pyplot as plt
from typing import List, Callable, Tuple, Any

random.seed(1)  # for reproducibility of the examples in this tutorial

class CGPProgram:
    """A simple CGP implementation with standard node indexing."""
    
    def __init__(self, n_inputs: int, n_outputs: int, n_nodes: int, function_set: List[Callable]):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.n_nodes = n_nodes
        self.function_set = function_set
        self.n_functions = len(function_set)
        
        # Node indexing:
        # 0 to n_inputs-1: input nodes
        # n_inputs to n_inputs+n_nodes-1: function nodes
        # n_inputs+n_nodes to n_inputs+n_nodes+n_outputs-1: output nodes (virtual)
        
        # Genome: [function_node_genes..., output_genes...]
        # Each function node has 3 genes: [input_x, input_y, function_idx]
        self.genome_length = n_nodes * 3 + n_outputs
        self.genome = None
        
    def create_random_genome(self) -> List[int]:
        """Create a random genome for the CGP program."""
        genome = []
        
        # Create function nodes (node IDs: n_inputs to n_inputs+n_nodes-1)
        for i in range(self.n_nodes):
            node_id = self.n_inputs + i
            # Input connections can point to any previous node (inputs or function nodes)
            max_connection_id = node_id - 1  # Can connect to any node with smaller ID
            
            input_x = random.randint(0, max_connection_id)
            input_y = random.randint(0, max_connection_id)
            function_idx = random.randint(0, self.n_functions - 1)
            genome.extend([input_x, input_y, function_idx])
        
        # Create output genes (point to any node: inputs or function nodes)
        for _ in range(self.n_outputs):
            # Outputs can connect to any input or function node
            output_connection = random.randint(0, self.n_inputs + self.n_nodes - 1)
            genome.append(output_connection)
            
        self.genome = genome
        return genome
    
    def decode_genome(self) -> Tuple[List[Tuple], List[int]]:
        """Decode genome into function node definitions and output connections."""
        function_nodes = []
        
        # Decode function nodes
        for i in range(self.n_nodes):
            start_idx = i * 3
            input_x = self.genome[start_idx]
            input_y = self.genome[start_idx + 1]
            function_idx = self.genome[start_idx + 2]
            function_nodes.append((input_x, input_y, function_idx))
        
        # Decode output connections
        output_start = self.n_nodes * 3
        output_connections = self.genome[output_start:output_start + self.n_outputs]
        
        return function_nodes, output_connections

