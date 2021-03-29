from tpot import TPOT
from sklearn.cross_validation import train_test_split
import pandas as pdas 
import numpy as npy 

#load the data using panda's read_csv method
cherenkov_telescope = pdas.read_csv('MAGIC Gamma Telescope Data.csv')
#i'm using data from a "Cherenkov telescope" which measures radiation in the atmosphere

#clean the data
telescope_randomize = cherenkov_telescope.iloc[npy.random.permutation(len(telescope))]
chrnkv_tele_data = telescope_randomize.reset_index(drop=True)

#Store 2 classes: Gamma or Hadron?
chrnkv_tele_data['Class']= chrnkv_tele_data['Class'].map({'g':0, 'h':1})
chrnkv_tele_class = chrnkv_tele_data['Class'].values

#Split training, testing, and valididation data
#Here we're figutring out how much data should be our training data and how much should be testing
training_indices, valididation_indices = training_indices, testing_indices = train_test_split(chrnkv_tele_data.index, stratify=chrnkv_tele_class, train_size=0.75, test_size=0.25)

#Here we initialize the tpot variable using the TPOT class and train our model
tpot = TPOT(generations=5, verbosity=2)
tpot.fit(chrnkv_tele_data.drop('Class', axis=1).loc[training_indices].values, chrnkv_tele_data.loc[training_indices, 'Class'].values)

#compute testing error for validation
tpot.score(chrnkv_tele_data.drop('Class', axis=1).loc[valididation_indices].values,chrnkv_tele_data.loc[valididation_indices, 'Class'].values)

#export the code the pipeline.py class
tpot.export('pipeline.py')













