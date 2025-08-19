def label(colors):
    d1 = color_code(colors[0])
    d2 = color_code(colors[1])
    if (d1 == d2 and d1 == 0):
        return "0 ohms"
    meas_unit = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    trailing_zeros = 0
    base_value = str(value(colors[0:2]))
    if d2 == 0:
        trailing_zeros = 1
        base_value = str(value(colors[0:1]))
    number_of_zeroes = color_code(colors[2]) + trailing_zeros
    result = base_value + number_of_zeroes % 3 * "0" + " " + meas_unit[number_of_zeroes // 3]
    return result
def value(colors):
    colors_str = ""
    item_counter = 0
    for item in colors:
        item_counter += 1
        if item_counter > 2:
            break
        colors_str += str(color_code(item))
    return int(colors_str)
def color_code(color):
    color_list = colors()
    color_id = 0
    for item in color_list:
        if item == color:
            return color_id
        color_id += 1
    return None
def colors():
    list_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return list_colors
#print(label(["red", "black", "red"]))