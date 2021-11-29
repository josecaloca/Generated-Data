# Instructions:

1. Git pull this repository to your local machine.

2. Depending on the type of data to generate (classification/regression) open generate_classification_data.py or generate_regression_data.py and run the code accordingly.

3. CSV files with the desired synthetic data will be available in the corresponding "files_regression"/"files_classification" folder.

4. To concatenate these CSV files into a combined.csv file you should open your command line and write the folling:

### Linux:
'''
cat *csv > combined.csv
'''

### Windows:

'''
copy *.csv combined.csv
'''
