import math
from typing import List

from CGPProgram import CGPProgram


FUNCTION_NAMES = ['+', '-', '*', '/', 'id', 'sin', 'cos', 'log']


class CGPExecutor:
    """Executes CGP programs using a simple node buffer approach."""
    
    def __init__(self, cgp_program: CGPProgram):
        self.cgp = cgp_program
        
    def execute(self, inputs: List[float]) -> List[float]:
        """Execute the CGP program on given inputs using node buffer."""
        function_nodes, output_connections = self.cgp.decode_genome()
        
        # Initialize node buffer: inputs + function nodes
        total_nodes = self.cgp.n_inputs + self.cgp.n_nodes
        node_buffer = [0.0] * total_nodes
        
        # Set input values in buffer
        for i, inp in enumerate(inputs):
            node_buffer[i] = inp
        
        # Calculate function nodes in order (they can reference earlier nodes only)
        for i, (input_x, input_y, func_idx) in enumerate(function_nodes):
            node_id = self.cgp.n_inputs + i
            val_x = node_buffer[input_x]
            val_y = node_buffer[input_y]
            result = self.cgp.function_set[func_idx](val_x, val_y)
            if math.isnan(result) or math.isinf(result):
                result = 0.0
            node_buffer[node_id] = result

        # Get output values by looking up output connections
        outputs = []
        for output_connection in output_connections:
            outputs.append(node_buffer[output_connection])
        
        return outputs
    
    def find_active_nodes(self) -> set:
        """Find which nodes are actually used in computation."""
        function_nodes, output_connections = self.cgp.decode_genome()
        active_nodes = set()
        
        # Start from output connections and work backwards
        to_check = list(output_connections)
        
        while to_check:
            node_id = to_check.pop()
            
            if node_id in active_nodes:
                continue
                
            active_nodes.add(node_id)
            
            # If this is a function node, add its inputs to check
            if node_id >= self.cgp.n_inputs:
                func_node_idx = node_id - self.cgp.n_inputs
                if func_node_idx < len(function_nodes):
                    input_x, input_y, _ = function_nodes[func_node_idx]
                    to_check.extend([input_x, input_y])
        
        return active_nodes
    
    def visualize_execution(self, inputs: List[float]):
        """Visualize the execution process with node buffer."""
        active_nodes = self.find_active_nodes()
        function_nodes, output_connections = self.cgp.decode_genome()
        
        print(f"=== Execution Analysis ===")
        print(f"Test inputs: {inputs}")
        print(f"Active nodes: {sorted(active_nodes)}")
        all_nodes = set(range(self.cgp.n_inputs + self.cgp.n_nodes))
        inactive_nodes = all_nodes - active_nodes
        print(f"Inactive nodes: {sorted(inactive_nodes)}")
        print()
        
        # Execute with detailed output
        total_nodes = self.cgp.n_inputs + self.cgp.n_nodes
        node_buffer = [0.0] * total_nodes
        
        # Set inputs
        print("Node Buffer Initialization:")
        for i, inp in enumerate(inputs):
            node_buffer[i] = inp
            status = "ACTIVE" if i in active_nodes else "inactive"
            print(f"  Node {i} (Input): {inp:.3f} [{status}]")
        
        print("\nFunction Node Computation:")
        # Calculate function nodes
        for i, (input_x, input_y, func_idx) in enumerate(function_nodes):
            node_id = self.cgp.n_inputs + i
            val_x = node_buffer[input_x]
            val_y = node_buffer[input_y]
            result = self.cgp.function_set[func_idx](val_x, val_y)
            if math.isnan(result) or math.isinf(result):
                result = 0.0
            node_buffer[node_id] = result
            
            func_name = FUNCTION_NAMES[func_idx]
            status = "ACTIVE" if node_id in active_nodes else "inactive"
            print(f"  Node {node_id}: {func_name}({val_x:.3f}, {val_y:.3f}) = {result:.3f} [{status}]")
        
        # Show outputs
        print(f"\nFinal Outputs:")
        for i, output_connection in enumerate(output_connections):
            output_value = node_buffer[output_connection]
            print(f"  Output {i}: node_{output_connection} = {output_value:.3f}")