def reverse_rows(matrix):
    return matrix[::-1]


def reverse_columns(matrix):
    return [row[::-1] for row in matrix]   # reverse each row to flip columns


def border_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total = 0

    for i in range(rows):
        for j in range(cols):
            # Check if element is on the border
            if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                total += matrix[i][j]
    return total


def diagonal_product(matrix):
    rows = len(matrix)
    product = 1

    for i in range(rows):
        product *= matrix[i][i]  # main diagonal
    return product


# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Perform operations
rev = reverse_rows(matrix)
rev_cols = reverse_columns(matrix)
border = border_sum(matrix)
diag_prod = diagonal_product(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nReversed Rows:")
for row in rev:
    print(row)

print('\nReversed Columns:')
for row in rev_cols:
    print(row)

print("\nSum of Border Elements:", border)
print("Product of Diagonal Elements:", diag_prod)