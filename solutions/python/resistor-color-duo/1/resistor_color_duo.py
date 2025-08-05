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
def colors():
    list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return list