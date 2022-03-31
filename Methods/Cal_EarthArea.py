"""
    Calculate the Area of Earth
        In this part, you can see two def: cal_EarthArea.
        Attention: this func ask for a homogeneous grid. And
        this is an attempt for matrix manipulation.
        You can see an example in the last section.
"""
import numpy as np

def cal_EarthArea(lat, lon):
    '''
    Calculate the Area of Earth
        :param lat: each grids latitude vector
        :param lon: each grids longitude vector
        :return
                S: the metrix of each grid area(unit: m**2)
                   the dimension include [lat, lon]
                S_total: the sum of each grid area(unit: m**2)
    '''
    ##  Data Processing
    delta_theta = np.abs(np.diff(lat)*np.pi/180)
    delta_phi = np.abs(np.diff(lon)*np.pi/180)
    cos_theta1 = np.abs(np.cos(lat[0:-1]*np.pi/180))
    cos_theta2 = np.abs(np.cos(lat[1::]*np.pi/180))

    ##  Calculate each grid area
    R = 6371007.181  # the Radius of Earth(unit: m)
    delta_theta, delta_PHI = np.meshgrid(delta_theta, delta_phi, indexing = 'ij')
    cos_theta1, temp = np.meshgrid(cos_theta1, delta_phi, indexing = 'ij')
    cos_theta2, temp = np.meshgrid(cos_theta2, delta_phi, indexing = 'ij')
    S = R*delta_theta*(R*cos_theta1*delta_PHI+R*cos_theta2*delta_PHI)/2
    S_total = np.sum(S)

    return S, S_total


if __name__ == "__main__":
    lat = np.linspace(20, 1, 40, endpoint=True)
    lon = np.linspace(120, 1, 140, endpoint=True)
    S, S_total = cal_EarthArea(lat, lon)