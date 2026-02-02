from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df.drop('PlayTennis', axis=1)
y = df['PlayTennis']

model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)
print("\nEnter new data to predict:")
outlook = int(input("Outlook (Sunny=2, Overcast=0, Rainy=1): "))
temperature = int(input("Temperature (Hot=1, Mild=2, Cool=0): "))
humidity = int(input("Humidity (High=0, Normal=1): "))
wind = int(input("Wind (Weak=1, Strong=0): "))
prediction = model.predict([[outlook, temperature, humidity, wind]])
if prediction[0] == 1:
    print("\nPrediction: Play Tennis = YES")
else:
    print("\nPrediction: Play Tennis = NO")
