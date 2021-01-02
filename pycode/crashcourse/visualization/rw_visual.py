#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author : Yihao Lin

'''
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, 
    #     edgecolors = 'none', s=1)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False) 
    
    plt.show()

    flag = int(input("press y to continue or n to stop:"))
    if flag == 0:
        break