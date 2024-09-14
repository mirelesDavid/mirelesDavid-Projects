import sys
import math
import matplotlib.pyplot as plt  

def eucledianDistance(x, y):
    return math.sqrt(sum((xi - yi) ** 2 for xi, yi in zip(x, y)))

def kRiesz(x, y, dimension):
    return 1 / (eucledianDistance(x, y) ** (dimension + 1))

def fgra(n, A):
    length = len(A)
    kMatrix = [[0.0 for _ in range(length)] for _ in range(length)]
    r = [0.0] * length
    mask = [True] * length
    removed = 0
    for i in range(length):
        for j in range(length):
            if i != j:
                kMatrix[i][j] = kRiesz(A[i], A[j], len(A[i]))
            else:
                kMatrix[i][j] = 0

    for i in range(length):
        r[i] = sum(kMatrix[i][j] for j in range(length))

    while (length - removed) > n:
        remove = -1
        removeIdx = 0
        for i in range(length):
            if mask[i] and r[i] > remove:
                remove = r[i]
                removeIdx = i
        for i in range(length):
            if mask[i]:
                r[i] -= kMatrix[i][removeIdx]
        mask[removeIdx] = False
        removed += 1
    res = [A[i] for i in range(length) if mask[i]]
    return res

def plotSubset(A, res, outputDir):
    cartessian = len(A[0])
    plt.figure()

    if cartessian == 2:
        plt.scatter(*zip(*A), color='blue', label='Original Points')
        plt.scatter(*zip(*res), color='red', label=f'Subset of {len(res)} Points')
    elif cartessian == 3:
        ax = plt.axes(projection='3d')
        ax.scatter3D(*zip(*A), color='blue', label='Original Points')
        ax.scatter3D(*zip(*res), color='red', label=f'Subset of {len(res)} Points')

    plt.title(f'Subset Plot - {len(res)} Points')
    plt.legend()
    plt.savefig(f"{outputDir}_subset_plot.png")
    plt.show()

def main():
    if len(sys.argv) != 5:
        print("Usage: python fgra.py <input_file> <n> <alpha> <output_directory>")
        return

    inputFile = sys.argv[1]
    n = int(sys.argv[2])
    outputDir = sys.argv[4]

    with open(inputFile, 'r') as file:
        firstLine = file.readline().strip()
        _, numEntries, cartessian = firstLine.split()
        numEntries, cartessian = int(numEntries), int(cartessian)

        A = []
        for line in file:
            if line.strip() and not line.startswith("#"):
                A.append(list(map(float, line.split())))

    res = fgra(n, A)

    outputFilePath = f"{outputDir}.txt"
    with open(outputFilePath, 'w') as out:
        for line in res:
            out.write(" ".join(f"{value:.6e}" for value in line) + "\n")

    print(f"Reduced array written to '{outputFilePath}'")

    plotSubset(A, res, outputDir)

if __name__ == "__main__":
    main()
