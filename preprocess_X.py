import argparse
import pandas as pd

from sklearn.preprocessing import StandardScaler

parser = argparse.ArgumentParser()

parser.add_argument('--input-data', type=str)
parser.add_argument('--output-data', type=str)

args = parser.parse_args()

data = pd.read_csv(args.input_data)
X = pd.DataFrame(data.drop(['Activity', 'subject'], axis=1))

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_scaled.to_csv(args.output_data)