# Instructions:

1. Git pull this repository to the virtual machine.

2. Depending on the type of data to generate (classification/regression) open [generate_classification_data.py](https://github.com/josecaloca/Generated-Data/blob/master/generate_classification_data.py) or [generate_regression_data.py](https://github.com/josecaloca/Generated-Data/blob/master/generate_regression_data.py) and run the code accordingly.

3. CSV files with the desired synthetic data will be available in the corresponding [files_regression](https://github.com/josecaloca/Generated-Data/tree/master/files_regression) or [files_classification](https://github.com/josecaloca/Generated-Data/tree/master/files_classification) folder.

4. To concatenate these CSV files into a combined.csv file you should open your command line and write the folling:

**Linux:**

cat *csv > combined.csv

5. To push the combined.csv file to Google Storage you must write the following commands in the console


**Create a bucket on Google Storage:**

gsutil mb gs://synthetic-datasets/

**Upload csv file to your bucket in Google Storage:**

gsutil cp combined.csv gs://synthetic-datasets/

Delete all CSV files from the folder:
rm *csv 
