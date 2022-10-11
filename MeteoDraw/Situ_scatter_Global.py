import numpy as np
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import cartopy.crs as ccrs
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator


def global_situ_draw(lon, lat, z, fig_axe):
    '''
        :param lon: longitude vector
        :param lat: latitude vector
        :param   z: 1D-varible vector
        :fig_axe: Artificially set the canvas by matplotlib.
    '''


    fig_axe.set_global()
    # fig_axe.add_feature(cfeature.LAND.with_scale('110m'), edgecolor = 'black', linewidth = 2)
    fig_axe.add_feature(cfeature.COASTLINE.with_scale('110'), edgecolor = 'black', linewidth = 2) 

    fig_axe.set_xticks(np.linspace(-180, 180, 7, endpoint=True))
    fig_axe.set_yticks(np.linspace(-90, 90, 7, endpoint=True))

    longitude = cticker.LongitudeFormatter(zero_direction_label = False, degree_symbol = '')
    latitude = cticker.LatitudeFormatter(degree_symbol = '')
    xminor_locator = AutoMinorLocator(4)
    yminor_locator = AutoMinorLocator(2)
    fig_axe.xaxis.set_minor_locator(xminor_locator)
    fig_axe.yaxis.set_minor_locator(yminor_locator)
    fig_axe.xaxis.set_major_formatter(longitude)
    fig_axe.yaxis.set_major_formatter(latitude)


    fig_axe.tick_params(which='major', length=14, width=3, colors='black')
    fig_axe.tick_params(which='minor',length=7, width=2, colors='black')
    fig_axe.tick_params(which='major', bottom=True, left=True, right=True, top=True)
    fig_axe.tick_params(which='minor', bottom=True, left=True, right=True, top=True)

    [x.set_linewidth(3) for x in fig_axe.spines.values()]
    [x.set_color("black") for x in fig_axe.spines.values()]

    # Draw the point with value. If you just need to draw the situ specific position, pls change "c=z" to "c='specific color'"
    S = 10
    fig_axe.scatter(lon, lat, c=z, s=S, marker='o', cmap='jet', transform=ccrs.PlateCarree())