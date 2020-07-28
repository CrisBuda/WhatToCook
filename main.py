import json
import pandas as pd
from pprint import pprint

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


patients_df = pd.read_json('det_ingrs.json')
patients_df2 = pd.read_json('recipes_with_nutritional_info.json')
x=patients_df.query("id=='000095fc1d'")
y=patients_df2.query("id=='000095fc1d'")

print(x)


print('asdf')