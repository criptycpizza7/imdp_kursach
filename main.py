import random
import numpy.random as np_random

from consts import *

# np_random.seed(SEED)
# random.seed(SEED)

import matplotlib.pyplot as plt

from classes import Tablet, fixed_tabs, env, workshop_stats, q_stats, num_of_tablets

def simulate(num_of_first = NUM_OF_FIRST, num_of_second = NUM_OF_SECOND, num_of_third = NUM_OF_THIRD, experiment_number = 1):

    print('Сид:', SEED)


    tablets1 = [Tablet(env=env, type=1, name=f'Tablet t1, no {index + 1}') for index in range(num_of_first)]
    tablets2 = [Tablet(env=env, type=2, name=f'Tablet t2, no {index + 1}') for index in range(num_of_second)]
    tablets3 = [Tablet(env=env, type=3, name=f'Tablet t3, no {index + 1}') for index in range(num_of_third)]

    env.run(until=24 * DAYS)


    tabs1 = fixed_tabs[0]
    tabs2 = fixed_tabs[1]
    tabs3 = fixed_tabs[2]

    t1 = []
    for index in range(len(tabs1)):
        if index == len(tabs1) - 1:
            t1.extend([tabs1[index][0]] * (24 * DAYS - tabs1[index][1]))
        else:
            if tabs1[index + 1][1] == tabs1[index][1]:
                t1.extend([tabs1[index + 1][0]])
            t1.extend([tabs1[index][0]] * (tabs1[index + 1][1] - tabs1[index][1]))

    t2 = []
    for index in range(len(tabs2) - 1):
        if index == len(tabs2) - 1:
            t2.extend([tabs2[index][0]] * (24 * DAYS - tabs2[index][1]))
        else:
            if tabs2[index + 1][1] == tabs2[index][1]:
                t2.extend([tabs2[index + 1][0]])
            t2.extend([tabs2[index][0]] * (tabs2[index + 1][1] - tabs2[index][1]))

    t3 = []
    for index in range(len(tabs3) - 1):
        if index == len(tabs3) - 1:
            t3.extend([tabs3[index][0]] * (24 * DAYS - tabs3[index][1]))
        else:
            if tabs3[index + 1][1] == tabs3[index][1]:
                t3.extend([tabs3[index + 1][0]])
            t3.extend([tabs3[index][0]] * (tabs3[index + 1][1] - tabs3[index][1]))


    avg_tabs = 0

    for index in range(len(tabs1) - 1):
        avg_tabs += (tabs1[index + 1][1] - tabs1[index][1]) * tabs1[index][0]

    for index in range(len(tabs2) - 1):
        avg_tabs += (tabs2[index + 1][1] - tabs2[index][1]) * tabs2[index][0]

    for index in range(len(tabs3) - 1):
        avg_tabs += (tabs3[index + 1][1] - tabs3[index][1]) * tabs3[index][0]

    avg_tabs /= (24 * DAYS)
    print('Среднее количество рабочих планшетов:', avg_tabs)


    avg_q = 0

    for index in range(len(q_stats) - 1):
        avg_q += (q_stats[index + 1][1] - q_stats[index][1]) * q_stats[index][0]

    avg_q /= (24 * DAYS)
    print('Средняя заполненность очереди:', avg_q)


    avg_ws = []

    for index in range(len(workshop_stats) - 1):
        avg_ws.extend([workshop_stats[index][0]] * (workshop_stats[index + 1][1] - workshop_stats[index][1]))

    print('Средняя загруженность мастерской:', sum(avg_ws) / (len(avg_ws) * 20))

    with open('avg_ws_stats', 'a') as f:
        f.write(str(sum(avg_ws) / (len(avg_ws) * 20)))
        f.write('\n')


    with open('stats_w_union', 'a') as f:

        print('\n\n\n\n\n', file=f)
        print(SEED, file=f)
        print(t1, file=f)
        print(t2, file=f)
        print(t3, file=f)



    import scipy.stats as sps
    import numpy as np


    # print(np.var(t1))
    # print(np.var(t2))
    # print(np.var(t3))
    # print('')
    # print(np.mean(t1))
    # print(np.mean(t2))
    # print(np.mean(t3))

    # ks_statistic, ks_p_value = sps.kstest(t1, t2)
    # print('')
    # print('t1-t2')
    # print(ks_statistic)
    # print(ks_p_value)

    # ks_statistic, ks_p_value = sps.kstest(t1, t3)
    # print('')
    # print('t1-t3')
    # print(ks_statistic)
    # print(ks_p_value)

    # ks_statistic, ks_p_value = sps.kstest(t2, t3)
    # print('')
    # print('t2-t3')
    # print(ks_statistic)
    # print(ks_p_value)


    # plt.plot([item[1] for item in tabs1], [item[0] for item in tabs1])
    # plt.plot([item[1] for item in tabs2], [item[0] for item in tabs2])
    # plt.plot([item[1] for item in tabs3], [item[0] for item in tabs3])
    # plt.plot([item[1] for item in workshop_stats], [item[0] for item in workshop_stats])
    # plt.plot([item[1] for item in q_stats], [item[0] for item in q_stats])

    # plt.ylabel('Количество планшетов')
    # plt.xlabel('Дни')
    # plt.legend(['1 тип', '2 тип', '3 тип', 'Мастерская', 'Очередь'])

    # plt.show()


    # import scipy.stats as sps


    # degree = 1

    # z = np.polyfit([item[1] for item in tabs1], [item[0] for item in tabs1], degree)
    # p = np.poly1d(z)

    # while sps.kstest([item[0] for item in tabs1], p([item[1] for item in tabs1]))[1] < 0.05 and degree < 78:

    #     degree += 1

    #     z = np.polyfit([item[1] for item in tabs1], [item[0] for item in tabs1], degree)
    #     p = np.poly1d(z)

    # plt.subplot(221)
    # plt.plot([item[1] for item in tabs1], [item[0] for item in tabs1])
    # plt.plot([item[1] for item in tabs1], p([item[1] for item in tabs1]))
    # plt.legend(['Планшеты', f'Аппроксимация полиномом {degree} степени'])
    # plt.title('Планшеты 1 типа')


    # degree = 1

    # z = np.polyfit([item[1] for item in tabs2], [item[0] for item in tabs2], degree)
    # p = np.poly1d(z)

    # while sps.kstest([item[0] for item in tabs2], p([item[1] for item in tabs2]))[1] < 0.05 and degree < 78:

    #     degree += 1

    #     z = np.polyfit([item[1] for item in tabs2], [item[0] for item in tabs2], degree)
    #     p = np.poly1d(z)

    # plt.subplot(222)
    # plt.plot([item[1] for item in tabs2], [item[0] for item in tabs2])
    # plt.plot([item[1] for item in tabs2], p([item[1] for item in tabs2]))
    # plt.legend(['Планшеты', f'Аппроксимация полиномом {degree} степени'])
    # plt.title('Планшеты 2 типа')


    # degree = 1

    # z = np.polyfit([item[1] for item in tabs3], [item[0] for item in tabs3], degree)
    # p = np.poly1d(z)

    # while sps.kstest([item[0] for item in tabs3], p([item[1] for item in tabs3]))[1] < 0.05 and degree < 78:

    #     degree += 1

    #     z = np.polyfit([item[1] for item in tabs3], [item[0] for item in tabs3], degree)
    #     p = np.poly1d(z)

    # z = np.polyfit([item[1] for item in tabs2], [item[0] for item in tabs2], 4)
    # p = np.poly1d(z)
    # plt.subplot(223)
    # plt.plot([item[1] for item in tabs3], [item[0] for item in tabs3])
    # plt.plot([item[1] for item in tabs3], p([item[1] for item in tabs3]))
    # plt.legend(['Планшеты', f'Аппроксимация полиномом {degree} степени'])
    # plt.title('Планшеты 3 типа')

    # plt.subplots_adjust(top=0.92, bottom=0.05, left=0.10, right=0.95, hspace=0.25, wspace=0.35)

    # plt.show()


    return avg_tabs, avg_q, sum(avg_ws) / (len(avg_ws) * 20)


simulate()