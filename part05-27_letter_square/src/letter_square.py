# Write your solution here
def reverse_and_append(sequence: str):
    return sequence + sequence[len(sequence)-2::-1]

def main():
    num_layers = int(input('Layers:'))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    layers = {}
    last_layer = num_layers * alphabet[num_layers-1]
    layers[num_layers] = reverse_and_append(last_layer)

    for i in range(num_layers - 1, 0, -1):
        prefix = layers[i + 1][0:num_layers - i]
        layers[i] = reverse_and_append(prefix + (alphabet[i-1] * i))

    for i in range(num_layers, 0, -1):
        print(layers[i])
    for i in range(2, num_layers + 1, 1):
        print(layers[i])

main()