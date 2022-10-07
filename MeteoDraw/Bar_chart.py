'''
Drawing series: Bar chart

    by KingLee 2022.10.7

    A series of drawing methods to present specific data in a picture as quick as you can.

    This is for bar chart.
'''

import matplotlib.pyplot as plt


def Bar_chart(x, y, width, fig_axe):
    '''
    :param x:  Abscissa, 1-D array
    :param y:  Ordinate, 1-D array
    :param width:  bar's width
    :fig_axe:  Artificially set the canvas by matplotlib

    :return:  This function don't have any return, you can call it repeatedly.
    '''

    fig_axe.bar(x, y, width, alpha=0.7)

    [x.set_linewidth(1.5) for x in fig_axe.spines.values()]
    [x.set_color("black") for x in fig_axe.spines.values()]

'''
Example: draw two datasets in one axe.

fig, fig_axe = plt.subplots()
width = 0.5
Bar_chart(x-width/2, y1, width, fig_axe)
Bar_chart(x+width/2, y2, width, fig_axe)

'''
