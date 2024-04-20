# Calcula en que signo y que grado cae un planeta.
def zodiac_position(degrees):
    sign_index = int(degrees / 30)
    sign_names = ["Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo",
                  "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"]
    sign = sign_names[sign_index]
    sign_degrees = degrees % 30
    return sign, sign_degrees
