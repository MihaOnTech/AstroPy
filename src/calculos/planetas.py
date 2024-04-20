import swisseph as swe
import pandas as pd
import numpy as np

from ..utilities import utils as utl
from ..data import dictionaries as dict

def calcular_posiciones_planetas(input_date, latitude, longitude):
    # Set the geoposition for topocentric calculations
    swe.set_topo(lon=longitude, lat=latitude)
    plts_dict = dict.get_planetas_dict()
    

    # Calculate positions
    planet_positions = []
    for planet, id in zip(plts_dict['planetas_es'], plts_dict['planets_ids']):
        pos, ret = swe.calc_ut(input_date, id)
        sign, degrees = utl.zodiac_position(pos[0])
        retrograde = 'Retrogrado' if (pos[3] < 0 ) else 'Directo'
        planet_positions.append([planet, sign, degrees, retrograde, pos[0]])

    # Create DataFrame
    planets_df = pd.DataFrame(planet_positions, columns=['Planeta', 'Signo', 'Grados_Signo', 'Retrogrado','Posicion'])
    return planets_df
