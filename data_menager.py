def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = []
    for element in lines:
        table.append(element.replace("\n", ""))
    return table
