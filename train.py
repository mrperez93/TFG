import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import numpy as np

# Suponiendo que 'training_1600000_processed_noemoticon' es un DataFrame en pandas
# y contiene las columnas 'X]' y 'X6'

# Renombrar columnas
pretrained = training_1600000_processed_noemoticon.rename(columns={"X]": "Sentiment", "X6": "tweet"})

# Crear tokens
# En este caso, usamos CountVectorizer para crear una matriz de documentos-términos (DFM)
vectorizer = CountVectorizer()
dfm_train = vectorizer.fit_transform(pretrained['tweet'])

# Crear un DataFrame de pandas a partir de la matriz esparsa
dfm_train_df = pd.DataFrame(dfm_train.toarray(), columns=vectorizer.get_feature_names_out())

# Añadir columna de ID numérico
dfm_train_df['id_numeric'] = np.arange(len(dfm_train_df))

# Dividir los datos en conjuntos de entrenamiento y prueba
set_seed = 600
np.random.seed(set_seed)

# Muestra de entrenamiento (1440000 ejemplos) y prueba (1600000 - 1440000 ejemplos)
id_train, id_test = train_test_split(dfm_train_df['id_numeric'], test_size=(1600000 - 1440000), random_state=set_seed)

# Dividir el DataFrame en conjuntos de entrenamiento y prueba
dfmat_training = dfm_train_df[dfm_train_df['id_numeric'].isin(id_train)]
dfmat_test = dfm_train_df[~dfm_train_df['id_numeric'].isin(id_train)]

# Si necesitas la columna 'Sentiment' en dfmat_training y dfmat_test
dfmat_training['Sentiment'] = pretrained.loc[dfmat_training.index, 'Sentiment']
dfmat_test['Sentiment'] = pretrained.loc[dfmat_test.index, 'Sentiment']
