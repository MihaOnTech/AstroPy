import datetime
import swisseph as swe
from data import mock_data as md

def input_loader(source='MockData'):
    if source == 'MockData':
        input_data = md.createUserInputMockData()
        dt = datetime.datetime.strptime(f"{input_data["date"]} {input_data["time"]}", "%d/%m/%Y %H:%M")
        utc_time = dt - datetime.timedelta(input_data["tzone"])
        jd_time = swe.julday(utc_time.year, utc_time.month, utc_time.day, utc_time.hour + utc_time.minute/60)
        return (jd_time, input_data['lat'], input_data['long'])
    else:
        return 
    