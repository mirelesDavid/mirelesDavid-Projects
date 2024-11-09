import matplotlib.pyplot as plt
import sys

def load_points(file_name):
    points = []
    with open(file_name, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split(','))
            points.append((x, y))
    return points

def plot_points_and_convex_hull(all_points, convex_hull_points, output_file_name="convex.png"):
    x_all, y_all = zip(*all_points)
    x_hull, y_hull = zip(*convex_hull_points)
    
    plt.figure(figsize=(10, 10))
    plt.scatter(x_all, y_all, color='blue', label='Original Points')
    plt.plot(x_hull + (x_hull[0],), y_hull + (y_hull[0],), 'r-', marker='o', label='Convex')

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.title("Convex")
    plt.savefig(output_file_name)
    plt.show()

if __name__ == "__main__":
    points_file = sys.argv[1]
    convex_hull_file = sys.argv[2]

    all_points = load_points(points_file)
    convex_hull_points = load_points(convex_hull_file)

    plot_points_and_convex_hull(all_points, convex_hull_points)
