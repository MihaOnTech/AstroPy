from .calculos import planetas as plt
from .data import load_data as data


def calcular_carta_astrologica(jdt, lat, long):
    planetas_datos = plt.calcular_posiciones_planetas(jdt, lat, long)
    #casas_datos = casas.calcular_casas(tdjul, lat, long)
    #aspectos_datos = aspectos.calcular_aspectos(planetas_datos)

    print(planetas_datos)
    #print(casas_datos)
    #print(aspectos_datos)

    carta_astrologica = {
        "planetas": planetas_datos,
        #"casas": casas_datos,
        #"aspectos": aspectos_datos
    }
    return carta_astrologica
    

if __name__ == '__main__':
   
    # SETUP INICIAL
    #input_source = 'MockData' Default
    input = data.input_loader()

    # INICIO DEL PROCESO
    carta = calcular_carta_astrologica(*input)
    
    
    # FINALIZA EL PROCESO
    #print(carta)
