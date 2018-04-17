import os

def input_sample_1d():
    sample = get_sample()

    sample_1d = list()
    for data in sample:
        sample_1d.append(float(data))

    return (28,28) , sample_1d

def input_sample_2d():

    sample = get_sample()

    sample_2d = list()
    for i, data in enumerate(sample):
        if (i % 28 == 0):
            sample_2d.append(list())
        sample_2d[-1].append(float(data))

    return (28,28) , sample_2d

def get_sample():

    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, 'sample_input.txt')

    with open(file_path, "r") as file_obj:
        temp = file_obj.read()
        sample = temp.split()

    return sample
