import argparse
import pickle
import pandas as pd

from sklearn.preprocessing import LabelEncoder

parser = argparse.ArgumentParser()

parser.add_argument('--input-data', type=str)
parser.add_argument('--output-data', type=str)

args = parser.parse_args()

data = pd.read_csv(args.input_data)
y_label = data.Activity.values.astype(object)

encoder = LabelEncoder()
y = encoder.fit_transform(y_label)

with open(args.output_data, 'wb') as f:
    pickle.dump(y, f)