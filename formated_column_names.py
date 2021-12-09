from typing import Any, Dict, List
import pandas as pd

df = pd.read_csv('./files_classification/generated_data_classification_0.csv')

def generate_auto_transformation(column_names: List[str]) -> List[Dict[str, Any]]:
    transformations = []
    
    for column_name in column_names:
        transformations.append({"auto": {"column_name": column_name}})
    
    return transformations


list = generate_auto_transformation(df.columns)

with open("file.txt", "w") as output:
    output.write(str(list))