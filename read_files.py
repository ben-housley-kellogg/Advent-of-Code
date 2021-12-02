import os

def read_one_item_per_line(input_file):

    path = os.path.join(os.path.dirname(__file__),"puzzle_inputs")
    with open(os.path.join(path, input_file)) as f:
        data = f.read()
    data = data.split('\n')
    return data