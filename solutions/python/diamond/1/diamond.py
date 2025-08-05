def rows(letter):
    list_of_lines = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter == "A":
        line = "A"
        list_of_lines.append(line)
        return list_of_lines
    if letter == "B":
        list_of_lines = [' A ', 'B B', ' A ']
        return list_of_lines
    letter_index = alphabet.index(letter)
    diamond_line = ""
    points_to_add = letter_index
    points_in_middle = 1
    diamond_line += add_points(points_to_add)
    diamond_line += "A"
    diamond_line += add_points(points_to_add)
    #diamond_line += '\n'
    list_of_lines.append(diamond_line)
    points_to_add -= 1
    for i in range(1, letter_index):
        diamond_line = ""
        diamond_line += add_points(points_to_add)
        diamond_line += alphabet[i]
        diamond_line += add_points(points_in_middle)
        diamond_line += alphabet[i]
        diamond_line += add_points(points_to_add)
        #diamond_line += '\n'
        list_of_lines.append(diamond_line)
        points_to_add -= 1
        points_in_middle += 2
    #if letter_index % 2 == 0:
    diamond_line = ""
    diamond_line += letter
    diamond_line += add_points(points_in_middle)
    diamond_line += letter
    #diamond_line += "\n"
    list_of_lines.append(diamond_line)
    points_to_add += 1
    points_in_middle -= 2
    for i in range(letter_index - 1, 0, -1):
        diamond_line = ""
        diamond_line += add_points(points_to_add)
        diamond_line += alphabet[i]
        diamond_line += add_points(points_in_middle)
        diamond_line += alphabet[i]
        diamond_line += add_points(points_to_add)
        #diamond_line += '\n'
        list_of_lines.append(diamond_line)
        points_to_add += 1
        points_in_middle -= 2
    points_to_add = letter_index
    diamond_line = ""
    diamond_line += add_points(points_to_add)
    diamond_line += "A"
    diamond_line += add_points(points_to_add)
    #diamond_line += '\n'
    list_of_lines.append(diamond_line)
    return list_of_lines
def add_points(number):
    if number == 0:
        return ""
    point_string = ""
    for i in range(number):
        point_string += " "
    return point_string
print(rows("E"))
