def holder():
    layers = [
                ["input", 1], # 0 - 1
                ["conv", 32], # 1 - 33
                ["pool", 32], # 33 - 65
                ["conv", 64], # 65 - 129
                ["pool", 64], # 129 - 193
                ["full", 10], # 193 - 203
             ]
    start = 0
    for i in layers:
        end = start + i[1]
        i.append((start, end))
        start = end
        
    dot_string = "dinetwork {"
    for i in range(len(layers)):
        if layers[i][0] == "input":
            continue
        elif layers[i][0] == "conv":
            for j in range(layers[i][2][0], layers[i][2][1]):
                for k in range(layers[i - 1][2][0], layers[i - 1][2][1]):
                    dot_string += str(k) + " -> " + str(j) + ";"
        elif layers[i][0] == "pool":
            for j, k in zip(range(layers[i][2][0], layers[i][2][1]), range(layers[i - 1][2][0], layers[i - 1][2][1])):
                dot_string += str(k) + " -> " + str(j) + ";"
        elif layers[i][0] == "full":
            for j in range(layers[i][2][0], layers[i][2][1]):
                for k in range(layers[i - 1][2][0], layers[i - 1][2][1]):
                    dot_string += str(k) + " -> " + str(j) + ";"
    dot_string += "}"