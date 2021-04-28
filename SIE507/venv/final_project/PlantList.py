import pandas as pd

class PlantList:
    def __init__(self, filename, zone):
        self.filename = filename
        self.zone = zone
        self.import_plant_data()

    def import_plant_data(self):
        self.df_plant = pd.read_csv(self.filename, index_col=None)
