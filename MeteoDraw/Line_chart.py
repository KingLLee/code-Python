'''
Drawing series: Line chart

    by KingLee 2022.10.6

    A series of drawing methods to present specific data in a picture as quick as you can.

    This is for line chart.
'''

import matplotlib.pyplot as plt


def Line_chart(x, y, axe):
    '''
    :param x:   Abscissa, 1-D array
    :param y:   Ordinate, 1-D array
    :param axe: Artificially set the canvas by matplotlib
                Example, 
                        fig = plt.figure(figsize=(16, 10), dpi=100)
                        axe = fig.add_axes([0.1, 0.1, 0.8, 0.8])
                        Line_chart(x, y, axe)
    
    :return:  This function don't have any return, you can call it repeatedly.

    '''

    axe.spines['bottom'].set_linewidth(2)
    axe.spines['left'].set_linewidth(2)
    axe.spines['right'].set_linewidth(2)
    axe.spines['top'].set_linewidth(2)

    S = 100
    axe.plot(x, y, color='black', linewidth=3, zorder=0)
    axe.scatter(x, y, s=S, marker='o')

    # Set the grid lines
    plt.grid(axis='both', linestyle='--', linewidth=1.5)
    axe.set_axisbelow(True)
