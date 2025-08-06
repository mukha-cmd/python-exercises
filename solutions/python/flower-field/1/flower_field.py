def annotate(garden):
    if not garden:
        return []
    valid_chars = [" ", "*"]
    rows, cols = len(garden), len(garden[0])
    for r in garden:
        if len(r) != cols:
            raise ValueError("The board is invalid with current input.")

    deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    output = []

    for i in range(rows):
        new_row = []
        for j in range(cols):
            if not (garden[i][j] in valid_chars):
                raise ValueError("The board is invalid with current input.")
            if garden[i][j] == "*":
                new_row.append("*")
            else:
                count = 0
                for di, dj in deltas:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and garden[ni][nj] == "*":
                        count += 1
                new_row.append(str(count) if count else " ")
        output.append("".join(new_row))

    return output
