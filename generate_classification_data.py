# !pip install Faker
from faker import Faker
from random import randrange
from datetime import datetime
import random
import pandas as pd
import numpy as np
from sklearn import datasets
#
from extensions.classification_data import generate_data
#

generate_data(n_rows=100, n_var=1000, iter=3)