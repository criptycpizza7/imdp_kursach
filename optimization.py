from main import simulate
from consts import NUM_OF_FIRST, NUM_OF_SECOND, NUM_OF_THIRD

experiment_number = 1

experiments = []
for _ in range(10):
    experiments.append(simulate(experiment_number=experiment_number))
    experiment_number += 1

avg_q = sum([item for _, item, _ in experiments])

iteration = 0

num_of_first, num_of_second, num_of_third = NUM_OF_FIRST, NUM_OF_SECOND, NUM_OF_THIRD

while avg_q > 0.7 and num_of_third < NUM_OF_FIRST + NUM_OF_SECOND + NUM_OF_THIRD:
    pass
