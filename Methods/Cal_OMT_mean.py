import numpy as np
import xarray as xr
import time

def time_to_cal(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print("the running time is {:.4}".format(t2-t1))
        return result
    return wrapper

@time_to_cal
def cal_OMT_mean(lat, lon, lev1, ts):
    '''
    This function is to calculate the Monthly ocean mean temperature:
    include the surface(OSMT) and the total ocean(OMT).
    It use the Trapezoid Formula to calculate the grid area, and
    Cuboid Formula to calculate the grid volume.
        :param lat: the latitude vector
        :param lon: the longitude vector
        :param lev1: the depth vector(on V grids, which is
                        different with lev: depth on T grids)
        :param ts: the sea temperature matrix (lev, lat, lon)
        :return
                OSMT: the Ocean Surface Mean Temerature
                OMT: the Ocean Mean Temerature
    Attention:
        This is an atempt of matrix manipulation without circulation.
    '''
    ## initialize the value
    tempa = np.append(lon, lon[-1]+(lon[-1]-lon[-2]))
    tempb = np.insert(lon, 0, lon[0]+(lon[0]-lon[1]))
    lonn = (tempa+tempb)/2

    tempa = np.append(lat, lat[-1]+(lat[-1]-lat[-2]))
    tempb = np.insert(lat, 0, lat[0]+(lat[0]-lat[1]))
    latt = (tempa+tempb)/2

    delta_lev1 = np.diff(lev1)

    ##  calculate the grid area: S (unit: m**2)
    delta_theta = np.abs(np.diff(latt)*np.pi/180)
    delta_phi = np.abs(np.diff(lonn)*np.pi/180)
    cos_theta1 = np.abs(np.cos(latt[0:-1]*np.pi/180))
    cos_theta2 = np.abs(np.cos(latt[1::]*np.pi/180))

    R = 6371007.181  # the default radius of the earth (unit: m)
    delta_theta, delta_PHI = np.meshgrid(delta_theta, delta_phi, indexing = 'ij')
    cos_theta1, A = np.meshgrid(cos_theta1, delta_phi, indexing = 'ij')
    cos_theta2, A = np.meshgrid(cos_theta2, delta_phi, indexing = 'ij')
    S = R*delta_theta*(cos_theta1*delta_PHI+cos_theta2*delta_PHI)*R/2

    # calculate the Ocean Surface Mean Temerature
    temp_t = ts[0,:,:]
    S_nansum = np.nansum(S[~np.isnan(temp_t)])
    OSMT = np.nansum(S*temp_t)/S_nansum

    # calculate the volume
    dle = np.tile(delta_lev1[:,np.newaxis,np.newaxis], [np.size(latt)-1,np.size(lonn)-1])
    V = dle * S

    # calculate the Ocean Mean Temerature
    V_nansum = np.nansum(V[~np.isnan(ts)])
    OMT = np.nansum(V*ts)/V_nansum

    return OSMT, OMT


if __name__ == "__main__":
    path = "D:\\Data\\"
    data = xr.open_dataset(path + "MMEAN0001-01.nc", decode_times=False)
    ts = np.array(data["ts"])[0, :, :, 0:-2]
    lev = np.array(data["lev"])
    lev1 = np.array(data["lev1"])
    lat = np.array(data["lat"])
    lon = np.array(data["lon"])[0:-2]
    print(cal_OMT_mean(lat, lon, lev1, ts))