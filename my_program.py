import sys

# Function to check if a tree is visible from a given direction
def is_visible(tree_heights, row, col, dr, dc):
    r, c = row + dr, col + dc
    while 0 <= r < len(tree_heights) and 0 <= c < len(tree_heights[0]):
        if tree_heights[r][c] >= tree_heights[row][col]:
            return False
        r, c = r + dr, c + dc
    return True

# Read the tree height map from a text file
def read_tree_height_map(file_name):
    tree_heights = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            row = [int(char) for char in line]
            tree_heights.append(row)
    return tree_heights

# Calculate the number of visible trees from either side
def calculate_visible_trees(tree_heights):
    visible_trees_count = 0
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, right, up, down

    for row in range(len(tree_heights)):
        for col in range(len(tree_heights[0])):
            visible = False
            for dr, dc in directions:
                if is_visible(tree_heights, row, col, dr, dc):
                    visible = True
                    break
            if visible:
                visible_trees_count += 1

    return visible_trees_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python my_program.py <filename>")
        sys.exit(1)

    file_name = sys.argv[1]
    tree_heights = read_tree_height_map(file_name)
    result = calculate_visible_trees(tree_heights)
    print(result)
