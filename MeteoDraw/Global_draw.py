"""
    Use python modules to draw basic Meteorological mapping.
    This script introduces how to draw the global distribution of
    different geoscience data, especially for the atmpospheric 
    science.
    Also, this script is just for drawing one map.
"""
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import cartopy.crs as ccrs
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator
import cmaps

def Global_draw(lon, lat, z, central_degree, levels, unit, title):
    '''
        :param lon: longitude vector
        :param lat: latitude vector
        :param   z: varible matrix, (lat, lon)
        :param central_degree: longitude central degree. It belongs to your
                         selected area. For example, if your target area
                         is the Pacific, so you should turn the central_degree
                         to 180.
        :param levels: It is the colorbar parameter - levels. You can adjust your
                        levels which would be suitable for your data. Also, from 
                        setting the levels number, you would change the colorbar 
                        total color number, which will help you to oberseve and 
                        anylise your pic more clearly. 
        :param unit: data unit
        :param title: Adjust your desirable pic title.
    '''
    size = 32
    plt.rc('font',family='Times New Roman', size=size)
    fig = plt.figure(figsize=(16, 10), dpi=300)
    ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection = ccrs.PlateCarree(central_longitude=central_degree))
    #ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=central_degree))

    ax1.set_global()
    # ax1.add_feature(cfeature.LAND.with_scale('110'), edgecolor = 'black', linewidth = 2)
    ax1.add_feature(cfeature.COASTLINE.with_scale('110'), edgecolor = 'black', linewidth = 2) 

    ax1.set_xticks(np.linspace(-180, 180, 7, endpoint=True))
    ax1.set_yticks(np.linspace(-90, 90, 7, endpoint=True))

    longitude = cticker.LongitudeFormatter(zero_direction_label = False, degree_symbol = '')
    latitude = cticker.LatitudeFormatter(degree_symbol = '')
    xminor_locator = AutoMinorLocator(4)
    yminor_locator = AutoMinorLocator(2)
    ax1.xaxis.set_minor_locator(xminor_locator)
    ax1.yaxis.set_minor_locator(yminor_locator)
    ax1.xaxis.set_major_formatter(longitude)
    ax1.yaxis.set_major_formatter(latitude)

    plt.xticks(fontproperties = 'Times New Roman', size = size)
    plt.yticks(fontproperties = 'Times New Roman', size = size)

    ax1.tick_params(which='major', length=14, width=3, colors='black')
    ax1.tick_params(which='minor',length=7, width=2, colors='black')
    ax1.tick_params(which='major', bottom=True, left=True, right=True, top=True)
    ax1.tick_params(which='minor', bottom=True, left=True, right=True, top=True)

    [x.set_linewidth(3) for x in ax1.spines.values()]
    [x.set_color("black") for x in ax1.spines.values()]

    tb = ax1.contourf(lon, lat, z, levels=levels, transform = ccrs.PlateCarree(), cmap = cmaps.NCV_jet)

    plt.title(title, fontsize = size+5, loc = 'center', y=1.025)
    plt.title("unit: "+unit, fontsize = size-3, loc = 'right', y=1.025)

    # gl = ax1.gridlines(crs = ccrs.PlateCarree(), draw_labels = False, linewidth = 1.5, color = 'black', alpha = 0.5, linestyle = '--')
    
    cb = plt.colorbar(tb, shrink = 0.8, orientation='horizontal', fraction=0.1, pad=0.08, aspect=25, drawedges=True)
    cb.outline.set_edgecolor('black')
    cb.outline.set_linewidth(2)
    cb.ax.tick_params(size=7, width=2)
    # print(cb.ax.get_children())
    cb.ax.get_children()[1].set_linewidths(2.0)

    # plt.show()
    # plt.savefig("D:\\Data\\test.png", bbox_inches='tight', dpi=600)

if __name__ == "__main__":
    data = xr.open_dataset("D:\\Data\\LICOM\\MMEAN0061-12_CTL.nc", decode_times=False)
    ss = np.array(data["ss"])[0,0,:,:]
    lat = np.array(data["lat"])
    lon = np.array(data["lon"])
    levels = np.linspace(np.nanmean(ss), np.nanmax(ss), 12, endpoint=True)
    Global_draw(lon, lat, ss, 180, levels, "psu", "TEST")
