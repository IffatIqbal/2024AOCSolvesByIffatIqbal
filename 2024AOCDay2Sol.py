def count_xmas(grid):

    rows, cols = len(grid), len(grid[0])
    target = "XMAS"
    target_len = len(target)
    count = 0

    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right diagonal
        (1, -1),  # down-left diagonal
        (-1, 1),  # up-right diagonal
        (-1, -1)  # up-left diagonal
    ]

    def check_direction(start_row, start_col, row_offset, col_offset):
        for i in range(target_len):
            r, c = start_row + i * row_offset, start_col + i * col_offset
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != target[i]:
                return False
        return True


    for row in range(rows):
        for col in range(cols):
            for row_offset, col_offset in directions:
                if check_direction(row, col, row_offset, col_offset):
                    count += 1

    return count


def load_grid(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file]
    return grid


if __name__ == "__main__":
    grid = load_grid("aocday2.txt")
    result = count_xmas(grid)
    print(f"Total occurrences of 'XMAS': {result}")
