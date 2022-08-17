import dataProvider as prov
import logger as log

def temperatureView(senson):
    data=prov.getTemperature(senson)
    log.temperatureLogger(data)
    return(data)

def pressureView(senson):
    data=prov.getPressure(senson)
    log.pressureLogger(data)
    return(data)

def windSpeedView(senson):
    data=prov.getWindSpeed(senson)
    log.windSpeedLogger(data)
    return(data)