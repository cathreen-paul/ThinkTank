""""
File: api.py

Description: The primary API for interacting with the gad dataset.
"""

import pandas as pd

class API:

    data = None  # dataframe

    def load_data(self, filename, columns=None):
     
        if columns:
            self.data = pd.read_csv(filename, usecols=columns)  # Load only the specified columns
        else:
            self.data = pd.read_csv(filename)  # Load all columns if none specified
        print("Load Data:")
        print(self.data)  

    def get_catalog(proficiency_level, learning_style_button, class_list, city):
        local = api.extract_local_network(proficiency_level, learning_style_button, class_list, city)
        table = pn.widgets.Tabulator(local, selectable=False)
        return table

    def get_cities(self):
        city = self.data['city'].unique().tolist()
        return sorted(city)

    def get_classes(self):
        classes = self.data['class'].unique().tolist()
        return sorted(classes)
    
    def get_learning_style(self):
        learning_style = self.data['learning_style'].unique().tolist()
        return sorted(learning_style)
    
    def proficiency_level(self):
        proficiency_level = self.data['proficiency_level'].unique().tolist()
        return sorted(proficiency_level)
 


    def extract_local_network(self, learning_style, class_list, city):
        # Filter based on learning style

        
        if learning_style:
            data = self.data[self.data['learning_style'].isin(learning_style)]
        
        # Filter based on class
        if class_list:
            data = data[data['class'].isin(class_list)]
        
        # Filter based on city
        if city:
            data = data[data['city'].isin(city)]


        return data
     

