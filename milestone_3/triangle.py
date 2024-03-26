def get_triangle(rows: int) -> list[list[int]]:
    triangle = []
    for i in range(rows):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j -1] + prev_row[j])
            row.append(1)
        triangle.append(row)
    return triangle

def print_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

triangle = get_triangle(5)
for row in triangle:
    print(row)

print_triangle(triangle)