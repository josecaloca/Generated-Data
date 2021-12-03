# !pip install Faker
from faker import Faker
from random import randrange
from datetime import datetime
import random
import pandas as pd
import numpy as np
from sklearn import datasets

#################################
# Classification dataset 
#################################
# We aim to create a dataset for classification problems 
# We create a multiclass umbalanced target variable with a 1:100 class distribution.
# The dataset contains continuous and categorical features 
# The dataset contains important and irrelevant variables to explain the target variable "y"

def generate_data(n_rows, n_var, iter):

    for i in range(iter):
        start_time = datetime.now()
        
        #First we set a seed
        np.random.seed(i)

        # number of classes in the target variable
        n_classes_target_variable = 3
        # number of rows in the dataset
        n_observations = n_rows
        # number of continous variables in the dataset
        n_variables = n_var-7
        # number of important/informative variables to explain "y"
        n_informative_variables = int(n_variables*0.7) # 70% of the variables are important to explain "y"
        # number of correlated variables: random linear combinations of the informative features:
        n_redundant_variables = int(n_variables*0.2)
        # seed
        random_seed = i
        # If we want an imbalanced dataset, set the proportions of samples assigned to each class
        weights = [0.3, 0.69] # classes distributed: 69, 30 and 1 percent in the "y" variable
        flip_y = 0

        # Create target and continous variables
        X, y = datasets.make_classification(n_classes = n_classes_target_variable, \
                                            n_samples = n_observations, \
                                            n_features  = n_variables, \
                                            n_informative=n_informative_variables, \
                                            n_clusters_per_class = 1, \
                                            n_redundant = n_redundant_variables, \
                                            weights = weights, \
                                            flip_y = flip_y, \
                                            random_state=random_seed, \
                                            )

        X = pd.DataFrame(X).add_prefix('continuous_var_')
        y = pd.DataFrame(y).set_axis(['target'], axis=1, inplace=False)

        # Let's now add categorical data to the set of features:

        fake = Faker('en_GB')

        transactional_data = []

        for customers_id in range(n_observations):

            # Create transaction date 
            d1 = datetime.strptime(f'1/1/2011', '%m/%d/%Y')
            d2 = datetime.strptime(f'1/11/2021', '%m/%d/%Y')
            transaction_date = fake.date_between(d1, d2)

            #create customer's name
            name = fake.name()

            # Create gender
            gender = random.choice(["M", "F"])

            #Create city
            city = fake.city()

            #create product ID in 8-digit barcode
            product_ID = fake.ean(length=8)

            #create amount spent
            amount_spent = fake.pyfloat(right_digits=2, positive=True, min_value=1, max_value=100)

            transactional_data.append([transaction_date, name, gender, city, product_ID, amount_spent])

        categorical_df = pd.DataFrame(transactional_data, \
                                        columns=['transaction_date', \
                                                'name', \
                                                'gender', \
                                                'city', \
                                                'product_id', \
                                                'amount_spent']) 


        # concatenation of the arrays and transformation to DF
        df = pd.concat([y, categorical_df, X], axis=1)
        
        # We insert randomly missing data into the continuous variables
        percentage_missing = np.arange(0, 0.05, 0.05/(n_variables*0.5))
        columns = df.columns[-(n_variables):]

        for col, val in zip(columns, percentage_missing):
            df.loc[df.sample(frac = val*random.uniform(1,1.5), random_state=1).index, col] = np.nan

        # We reset index
        df.reset_index(drop=True, inplace=True)
        
        # Export dataframe as CSV
        
        if i == 0:
            df.to_csv(f'./files_classification/generated_data_classification_{i}.csv', \
                        index=False, \
                        header=True, \
                        encoding="utf-8")
        else:
            df.to_csv(f'./files_classification/generated_data_classification_{i}.csv', \
                        index=False, \
                        header=True, \
                        encoding="utf-8")
            
        ###############################################  
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        ###############################################



