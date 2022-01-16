from  sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as m

# Carrega o dataSet
data = load_iris()

# Define como X as variaveis preditoras e y variavel predita 
X = data.data
y = data.target

# Separamos a base em treino/teste 
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.3)

# Instaciando o modelo 
model = RandomForestClassifier()

# Treinando modelo na base de treino
model.fit(X_train, y_train)

# Avaliamos o modelo na base de teste 
print(m.classification_report(y_test, model.predict(X_test)))