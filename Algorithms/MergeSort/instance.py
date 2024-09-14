import sys

def write_descending_numbers_to_file(n, filename):
    # Generate a list of numbers from n to 1 in descending order
    numbers = list(range(n, 0, -1))
    
    # Open the file for writing
    with open(filename, 'w') as file:
        # Write the count of numbers on the first line
        file.write(f"{len(numbers)}\n")
        
        # Write the numbers, each on a new line
        for number in numbers:
            file.write(f"{number}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Syntax error! {0} N".format(sys.argv[0]))
        exit(-1)
    # Example usage
    n = int(sys.argv[1])
    filename = f'numbers_{n:d}.txt'
    write_descending_numbers_to_file(n, filename)
    print(f"Numbers from {n} to 1 have been written to {filename}.")
