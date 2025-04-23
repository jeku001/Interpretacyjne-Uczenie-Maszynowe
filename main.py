import pandas as pd
from pygam import LinearGAM, s, f, l
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('data/raw_data/zal_hausing.csv')
data = data.drop(columns=['zainter'])
scaler = StandardScaler()
scaled = scaler.fit_transform(data)
X = scaled[:,:-1]
y = scaled[:,-1]


gam = LinearGAM(s(0) + s(1) + s(2) + s(3) + s(4) + s(5) + s(6) + s(7))
gam.fit(X,y)