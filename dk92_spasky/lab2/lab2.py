import os

os.system('clear')


class energy:
    ''' class energy.
    parameters:

     name
     year
     power
     water_flow
     wind_speed
     coal_cnsmp
    '''

    name = ''
    year = 0
    power = 0
    water_flow = 0
    wind_speed = 0
    coal_cnsmp = 0


    def __init__(self, name='NONE', year=0,
                 water_flow=0, wind_speed=0, coal_cnsmp=0):
        ''' energy constructor'''
        self.name = name
        self.year = year
        self.power = power
        self.water_flow = water_flow
        self.wind_speed = wind_speed
        self.coal_cnsmp = coal_cnsmp

    def get_name(self):
        '''method prints name of station.
        Else prints unknown name
        '''
        if(self.name != 'NONE\n'):
            print('Name of station: ',self.name)
        else:
            print('NO NAME\n')

    def get_year(self):
        '''method prints
        year of foundation'''
        if (self.year != 0):
            print('Name of station: ', self.name, 'founded:', self.year, '\n')

    def get_power(self):
        '''method prints power of station'''
        if (self.name != 'NONE \n'):
            print('Name of station: ', self.name, 'power :', self.power, '\n')

    def __str__(self):
        powerstat = 'Name of station:  ' + str(self.name) + "\n" + \
                    'founded: ' + str(self.year) + '\n'

        if(self.__class__.__name__ == 'hydro_power_plant'):
            powerstat = powerstat + 'water_flow: ' + \
                        str(self.water_flow) + ' m^3/s\n'
        if(self.__class__.__name__ == 'windmill'):
            powerstat = powerstat + 'wind_speed: ' + \
                        str(self.wind_speed) + ' m/s \n'
        if(self.__class__.__name__ == 'thermal_power_plant'):
            powerstat = powerstat + 'coal_cnsmp: ' + \
                        str(self.coal_cnsmp) + 't/m\n'
        powerstat = powerstat + 'power: ' + str(self.power) + ' megWATT \n'

        return powerstat


class hydro_power_plant(energy):
    '''class hydro_power_plant .
     parameters:

     name
     year
     power
     water_flow
    '''

    def __init__(self, name='NONE', year=0, power=0, water_flow=0 ):
        '''hydro_power_plant class constructor'''
        self.name = name
        self.year = year
        self.power = power
        self.water_flow = water_flow

    def get_water_flow(self):
        ''' the method returns
        the value water_flow'''
        print(self.name, ' water flow = ', self.water_flow, ' m^3/s\n')

    def set_water_flow(self, new_water_flow):
        ''' the method sets
        the value water_flow '''
        self.water_flow = new_water_flow
        print(self.name, 'New water_flow:', self.water_flow, ' m^3/s\n')


class windmill(energy):
    ''' class windmill .
     parameters:

     name
     year
     power
     wind_speed
    '''

    def __init__(self, name='NONE', year=0, power=0,
                 wind_speed=0):
        '''windmill class constructor'''

        self.name = name
        self.year = year
        self.power = power
        self.wind_speed = wind_speed

    def get_wind_speed (self):
        '''the method returns
        the value wind_speed  '''
        print(self.name, ' wind speed = ', self.wind_speed, '\n')


class thermal_power_plant(energy):
    '''thermal_power_plant class.
     parameters:
     name
     year
     power
     coal_cnsmp
    '''

    def __init__(self, name='NONE', year=0, power=0, coal_cnsmp=0 ):
        '''thermal_power_plant class constructor'''
        self.name = name
        self.year = year
        self.power = power
        self.coal_cnsmp = coal_cnsmp


    def get_coal_cnsmp (self):
        '''the method returns
        the value coal_cnsmp'''
        print(self.name, ' coal is used :', self.coal_cnsmp, '\n')


if(__name__ == '__main__'):
    TPP_1 = thermal_power_plant('ZTPP', 1973, 3650, 90)
    windmill_1 = windmill('pyriatin windmill', 2020, 80, 25)
    HPP_1 = hydro_power_plant('DTPP', 1932, 838, 300 )

    TPP_1.get_power()
    windmill_1.get_wind_speed()
    HPP_1.get_water_flow()
    windmill_1.get_name()
    HPP_1.set_water_flow(46)
    HPP_1.get_water_flow()

    print(HPP_1)
    print(TPP_1)
    print(windmill_1)



