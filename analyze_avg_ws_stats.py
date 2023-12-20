stats = []

with open('avg_ws_stats', 'r') as f:
    for line in f:
        stats.append(float(line))

print(sum(stats) / len(stats))