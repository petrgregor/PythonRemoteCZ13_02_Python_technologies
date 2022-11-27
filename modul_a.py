test = "A nice sentence."

def find_index(collection, element):
    for index, value in enumerate(collection):
        if value == element:
            return index
    return -1

# TODO upravit funkci print_sys_path
def print_sys_path():
    import sys
    print(sys.path)
