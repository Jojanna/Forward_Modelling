__author__ = 'wallisj'
import re
import numpy as np


def data_load(filepath, header_lines):
    #print (filepath)
    file = open(filepath, 'r')
    lines = file.readlines()[header_lines:]


    class columns:
        def __init__(self, scenario, vp, vs, rho, ephi, vsh, sw):
            self.scenario = scenario
            self.vp = vp
            self.vs = vs
            self.rho = rho
            self.ephi = ephi
            self.vsh = vsh
            self.sw = sw

    database = []
    database_2 = []
    dictionary = {}

    for row in lines:
        array = row.strip()
        array = re.split("[\t,]",array)

        database.append(columns(array[0], array[1], array[2], array[3], array[4], array[5], array[6]))

    #print (alllines[0])
    #print (array)
    #print (database[0].code)
    #print (database)
    #print (database.code)

    n = len(database)

    scenario = ([data.scenario for data in database])
    vp = ([float(data.vp) for data in database])
    vs = ([float(data.vs) for data in database])
    rho = ([float(data.rho) for data in database])
    ephi = ([float(data.ephi) for data in database])
    vsh = ([float(data.vsh) for data in database])
    sw = ([float(data.sw) for data in database])


    zipped = [scenario, vp, vs, rho, ephi, vsh, sw]
    zipped = np.array(zipped).T

    return zipped


