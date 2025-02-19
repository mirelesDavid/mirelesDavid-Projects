import random
import math
import networkx as nx
import matplotlib.pyplot as plt

def generate_directed_graph(num_nodes, N, M, edge_prob=0.3):
    """
    Generate a directed graph with non-negative weights and nodes placed randomly
    inside the rectangle [0, N] x [0, M].

    Parameters:
    - num_nodes (int): Number of nodes.
    - N (int): Width of the rectangle.
    - M (int): Height of the rectangle.
    - edge_prob (float): Probability of an edge existing between two nodes.

    Returns:
    - G (networkx.DiGraph): A directed graph with nodes and weighted edges.
    """
    # Step 1: Generate random points for nodes
    nodes = [(i, random.uniform(0, N), random.uniform(0, M)) for i in range(num_nodes)]
    
    # Step 2: Create a directed graph
    G = nx.DiGraph()
    
    # Add nodes to the graph
    for node_id, x, y in nodes:
        G.add_node(node_id, pos=(x, y))
    
    # Step 3: Add edges with weights based on Euclidean distance
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and random.random() < edge_prob:
                x1, y1 = G.nodes[i]['pos']
                x2, y2 = G.nodes[j]['pos']
                # Calculate Euclidean distance as weight
                weight = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                G.add_edge(i, j, weight=weight)
    
    return G

def save_graph_to_file(G, filename):
    """
    Save the directed graph to a text file.

    The format is:
    - NodeID X Y
    - SourceNode TargetNode Weight

    Parameters:
    - G (networkx.DiGraph): The graph to save.
    - filename (str): The path to the output file.
    """
    with open(filename, 'w') as f:
        # Save node information
        f.write("# Nodes:\n")
        for node_id, pos in G.nodes(data='pos'):
            f.write(f"{node_id} {pos[0]} {pos[1]}\n")
        
        # Save edge information
        f.write("\n# Edges:\n")
        for u, v, data in G.edges(data=True):
            f.write(f"{u} {v} {data['weight']}\n")

def plot_graph(G):
    """
    Plot the directed graph with node positions and edge weights.
    """
    pos = nx.get_node_attributes(G, 'pos')
    edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in G.edges(data=True)}
    
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Directed Graph with Non-negative Weights")
    plt.show()

# Example usage
N, M = 100, 100     # Rectangle size
num_nodes = 10      # Number of nodes
edge_prob = 0.4     # Edge probability

# Generate the graph
G = generate_directed_graph(num_nodes, N, M, edge_prob)

# Save the graph to a text file
filename = "directed_graph.txt"
save_graph_to_file(G, filename)
print(f"Graph saved to {filename}")

# Plot the graph
plot_graph(G)
