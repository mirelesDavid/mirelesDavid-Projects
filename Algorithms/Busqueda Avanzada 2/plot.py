import sys
import matplotlib.pyplot as plt

def load_graph(file_name):
    nodes = {}
    edges = []
    with open(file_name, 'r') as f:
        section = None
        for line in f:
            if line.strip() == "# Nodes":
                section = "nodes"
            elif line.strip() == "# Edges":
                section = "edges"
            elif section == "nodes" and line.strip():
                node_id, x, y = line.split()
                nodes[int(node_id)] = (float(x), float(y))
            elif section == "edges" and line.strip():
                u, v, _ = line.split()
                edges.append((int(u), int(v)))
    print("Nodes loaded:", nodes)  # Debugging: Print nodes
    return nodes, edges

def load_path(file_name):
    path = []
    with open(file_name, 'r') as f:
        for line in f:
            if line.strip() and line[0] != "#":
                node_id, _, _ = line.split()
                path.append(int(node_id))
    print("Path loaded:", path)  # Debugging: Print path
    return path

def plot_graph(nodes, edges, path):
    plt.figure(figsize=(10, 7))

    # Plot all edges
    for u, v in edges:
        x1, y1 = nodes[u]
        x2, y2 = nodes[v]
        plt.plot([x1, x2], [y1, y2], "gray")

    # Highlight the path
    if path:
        valid_path = [node for node in path if node in nodes]
        if len(valid_path) < len(path):
            print(f"Warning: Some nodes in the path are not defined in the graph: {set(path) - set(valid_path)}")
        path_x = [nodes[node][0] for node in valid_path]
        path_y = [nodes[node][1] for node in valid_path]
        plt.plot(path_x, path_y, "r-", linewidth=2, label="Shortest Path")

    # Plot the nodes
    plt.scatter(
        [n[0] for n in nodes.values()],
        [n[1] for n in nodes.values()],
        c="blue",
        label="Nodes"
    )

    # Add labels and legend
    for node_id, (x, y) in nodes.items():
        plt.text(x, y, str(node_id), fontsize=10, ha='center', va='center', color="black")
    plt.legend()
    plt.title("Graph with Shortest Path")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python plot.py <path_file> <graph_file>")
        sys.exit(1)

    path_file = sys.argv[1]
    graph_file = sys.argv[2]

    nodes, edges = load_graph(graph_file)
    path = load_path(path_file)

    missing_nodes = [node for node in path if node not in nodes]
    if missing_nodes:
        print(f"Warning: These nodes are missing from the graph: {missing_nodes}")

    plot_graph(nodes, edges, path)
