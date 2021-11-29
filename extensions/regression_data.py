# !pip install Faker
from faker import Faker
from random import randrange
from datetime import datetime
import random
import pandas as pd
import numpy as np
from sklearn import datasets
from scipy.stats import skew

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
        
        # number of rows in the dataset
        n_observations = n_rows
        # number of continous variables in the dataset
        n_variables = n_var # 10 continous variables
        # number of important/informative variables to explain "y"
        n_informative_variables = int(n_variables*0.7) # 70% of the variables are important to explain "y"
        # number of correlated variables: random linear combinations of the informative features:
        n_redundant_variables = int(n_variables*0.2)
        # standard deviation of the distribution of the noise added to the target variable
        noise_sd = 0.1
        # seed
        random_seed = 123


        # Create target and continous variables
        X, y = datasets.make_regression(n_samples = n_observations, \
                                    n_features  = n_variables, \
                                    n_informative=n_informative_variables, \
                                    effective_rank = n_redundant_variables, \
                                    noise = noise_sd, \
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
                                        columns=['Transaction_date', \
                                                'Name', 'Gender', \
                                                'City', \
                                                'Product_id', \
                                                'Amount_spent']) 


        # concatenations of the arrays and transformation to DF
        df = pd.concat([y, categorical_df, X], axis=1)

        # We insert randomly missing data into the continuous variables
        percentage_missing = np.arange(0, 0.05, 0.05/(n_variables*0.5))
        columns = df.columns[-(n_variables):]

        for col, val in zip(columns, percentage_missing):
            df.loc[df.sample(frac = val*random.uniform(1,1.5), random_state=1).index, col] = np.nan

        # We reset index
        df.reset_index(drop=True, inplace=True)

        # let's enforce 20 % of the continuous variables to have a non-linear relationship with the target 
        columns = df.columns[-int((n_variables)*0.2):]

        list = []
        for col in columns:
            var = np.exp(df[col] - df['target']*00.1)
            list.append(var)

        list = pd.DataFrame(np.array(list).transpose(), columns=columns)

        df[columns] = list
        
        # Export dataframe as CSV
        
        if i == 0:
            df.to_csv(f'./files_regression/generated_data_regression_{i}.csv', index=False, header=True)
        else:
            df.to_csv(f'./files_regression/generated_data_regression_{i}.csv', index=False, header=False)
            
        ###############################################  
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        ###############################################
    
    
