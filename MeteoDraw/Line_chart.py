'''
Drawing series: Line chart

    by KingLee 2022.10.6

    A series of drawing methods to present specific data in a picture as quick as you can.

    This is for line chart.
'''

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def Line_chart(x, y, fig_axe):
    '''
    :param x:   Abscissa, 1-D array
    :param y:   Ordinate, 1-D array
    :param fig_axe: Artificially set the canvas by matplotlib
                Example, 
                        fig = plt.figure(figsize=(16, 10), dpi=100)
                        fig_axe = fig.add_axes([0.1, 0.1, 0.8, 0.8])
                        Line_chart(x, y, fig_axe)
    
    :return:  This function don't have any return, you can call it repeatedly.

    '''

    #Set tick
    '''
    xstep, xmajor_step, xminor_step = 4, 4, 1  # set the x-axis step
    ystep, ymajor_step, yminor_step = 4, 4, 1  # set the y-axis step

    xmajorLocator = MultipleLocator(xmajor_step)  # x-axis major tick step length
    xminorLocator = MultipleLocator(xminor_step)  # x-axis minor tick step length
    ymajorLocator = MultipleLocator(ymajor_step)  # y-axis major tick step length
    yminorLocator = MultipleLocator(yminor_step)  # y-axis minor tick step length

    fig_axe.xaxis.set_major_locator(xmajorLocator)
    fig_axe.xaxis.set_minor_locator(xminorLocator)
    fig_axe.yaxis.set_major_locator(ymajorLocator)
    fig_axe.yaxis.set_minor_locator(yminorLocator)

    fig_axe.tick_params(which = 'major', length = 8, width = 1.5)  # Set the major tick properties.
    fig_axe.tick_params(which = 'minor', length = 4, width = 1)  # Set the minor tick properties.
    # fig_axe.tick_params(which = 'major', top=True, right = True)  # Set which axis to display the major tick
    # fig_axe.tick_params(which = 'minor', top=True, right = True)  # Set which axis to display the minor tick
    '''

    [x.set_linewidth(1.5) for x in fig_axe.spines.values()]
    [x.set_color("black") for x in fig_axe.spines.values()]
    
    S = 100
    fig_axe.plot(x, y, color='black', linewidth=3, zorder=0)
    fig_axe.scatter(x, y, s=S, marker='o')

    # Set the grid lines
    plt.grid(axis='both', linestyle='--', linewidth=1.5)
    fig_axe.set_axisbelow(True)
