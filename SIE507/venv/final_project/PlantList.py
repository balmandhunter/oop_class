import pandas as pd

class PlantList:
    def __init__(self, filename):
        self.filename = filename
        self.import_plant_data()

    def import_plant_data(self):
        # data if from https://gardeninminutes.com/plant-spacing-chart-raised-bed-gardening/ and
        # https://www.almanac.com/gardening/planting-calendar/zipcode/04347 and
        # https://www.ufseeds.com/maine-vegetable-planting-calendar.html
        headers = ['name','zone','is_perennial','count_per_square','start_indoors_month',
                   'transplant_month','direct_seed_month','harvest_month']
        dtypes = {'name':'str', 'zone':'int', 'is_perennial':'int', 'count_per_square':'int',
                  'start_indoors_month': 'int', 'transplant_month':'int', 'direct_seed_month':'int',
                  'harvest_month':'int'}
        self.df_plant = pd.read_csv(self.filename,
                                    index_col=None,
                                    header=None,
                                    names=headers,
                                    dtype=dtypes)

    '''Return a list of all of the available plants'''
    def return_plants(self):
        plants = self.df_plant.name.unique()
        return plants

    '''Return whether a plant is a perennial or not'''
    def get_perennial_status(self, name):
        # drop the extra zone entries for each plant
        df_perennial = self.df_plant[['name', 'is_perennial']].drop_duplicates()
        is_perennial = df_perennial[df_perennial.name == name].is_perennial.values[0]
        return is_perennial

    '''Make a df of count per square for each plant, which can be called when creating a plan'''
    def get_count_per_square(self, plant_name):
        df_count_per_square = self.df_plant[['name', 'count_per_square']].drop_duplicates()
        return df_count_per_square[df_count_per_square.name == plant_name].count_per_square.values[0]