from collections import deque
crates = {}
with open('input5.txt', 'r') as source:
    layout, moves = source.read().split('\n\n')
    layers = layout.split('\n')
    for layer in reversed(layers[:-1]):
        layer = layer.split(' ')
        print(layer)
        # for i in layers[-1].split('   '):
        #     print(layer)