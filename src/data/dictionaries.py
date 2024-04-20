import swisseph as swe 

def get_planetas_dict():
    return {
        "planet_ids": [swe.SUN, swe.MOON, swe.MERCURY, swe.VENUS, swe.MARS,swe.JUPITER, swe.SATURN, swe.URANUS, swe.NEPTUNE, swe.PLUTO, swe.MEAN_NODE],
        "planets": ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto','Node'],
        "planetas_es": ['Sol','Luna','Mercurio','Venus','Marte','Jupiter','Saturno','Urano','Neptuno','Pluton','Nodo']
    }
