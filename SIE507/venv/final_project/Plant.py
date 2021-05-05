from abc import ABC, abstractmethod
from PlantList import PlantList

class Plant():
    def __init__(self, plant_name, zone, **kwargs):
        super().__init__(**kwargs)
        self.count_per_square = None
        self.should_direct_seed = None
        self.start_indoors_month = None
        self.transplant_month = None
        self.direct_seed_month = None
        self.months_in_ground = None
        self.is_perennial = None
        self.plant_name = plant_name
        self.zone = zone
        self.plantlist = PlantList('data/all_plants.csv')
        self.initialize_plant()

    '''Initialize a plant object with information based on its zone'''
    def initialize_plant(self):
        df_plant = self.plantlist.df_plant
        df_this_plant = df_plant[(df_plant.name == self.plant_name) & (df_plant.zone == int(self.zone))]
        self.count_per_square = df_this_plant.count_per_square.values[0]
        self.start_indoors_month = df_this_plant.start_indoors_month.values[0]
        self.transplant_month = df_this_plant.transplant_month.values[0]
        self.direct_seed_month = df_this_plant.direct_seed_month.values[0]
        self.is_perennial = df_this_plant.is_perennial.values[0]

        if df_this_plant.direct_seed_month.values[0] != 0:
            self.should_direct_seed = True
        else:
            self.should_direct_seed = False

    '''Method to return plant name'''
    def get_plant_name(self):
        return self.plant_name

    @abstractmethod
    def get_months_in_ground(self):
        pass


class Perennial(Plant):
    def __init__(self, is_new, plant_name, zone, **kwargs):
        super().__init__(plant_name, zone, **kwargs)
        self.is_new = is_new
        self.get_months_in_ground()

    '''Find the months that the perennial is in the ground'''
    def get_months_in_ground(self):
        if self.is_new == True:
            if self.should_direct_seed == True:
                self.months_in_ground = list(range(self.direct_seed_month,13))
            elif self.should_direct_seed == False:
                self.months_in_ground = list(range(self.transplant_month,13))
        elif self.is_new == False:
            self.months_in_ground = list(range(1,13))


class Annual(Plant):
    def __init__(self, plant_name, zone, **kwargs):
        super().__init__(plant_name, zone, **kwargs)
        self.get_months_in_ground()

    '''Return the months that the plant is in the ground'''
    def get_months_in_ground(self):
        if self.should_direct_seed == True:
            self.months_in_ground = list(range(self.direct_seed_month, 13))
        elif self.should_direct_seed == False:
            self.months_in_ground = list(range(self.transplant_month, 13))
