def create_formatted_string(name, value, new_line_count):
    new_lines = "\n" * new_line_count
    formatted_string = "{}{}{}".format(name, new_lines, value)
    return formatted_string