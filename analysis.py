import matplotlib.pyplot as plt

import json


colors = {
    1: '#1f77b41f',
    2: '#ff7f0e1f',
    3: '#55b2551f'
}

with open('stats_w_union', 'r') as f:
    index = 0
    for line in f:
        index %= 3
        try:
            tmp = json.loads(line)
        except json.JSONDecodeError:
            tmp = None
        if isinstance(tmp, list):
            plt.plot(list(range(len(tmp))), tmp, color=colors[index + 1])
            index += 1

plt.show()