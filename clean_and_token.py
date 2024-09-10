import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import download
import emoji

# Descargar recursos necesarios para NLTK
download('punkt')
download('stopwords')

# Función para procesar los tweets
def create_tokens(twts):
    # Eliminar menciones (@) y asteriscos (*), y reemplazar URLs con 'url'
    clean = twts['tweet'].str.replace('@', '', regex=False)
    clean = clean.str.replace('*', '', regex=False)
    clean = clean.apply(lambda x: re.sub(r"http\S+|www\S+|https\S+", 'url', x, flags=re.MULTILINE))
    
    # Reemplazar emojis con texto (usando emoji.demojize)
    clean = clean.apply(lambda x: emoji.demojize(x, delimiters=("", "")))

    twts['tweet'] = clean
    
    # Tokenización
    twts['tokens'] = twts['tweet'].apply(word_tokenize)
    
    # Eliminar puntuaciones, símbolos y stopwords
    stop_words = set(stopwords.words('english'))
    twts['tokens'] = twts['tokens'].apply(lambda x: [word.lower() for word in x if word.isalnum() and word not in stop_words])
    
    # Stemming (radicalización)
    stemmer = PorterStemmer()
    twts['tokens'] = twts['tokens'].apply(lambda x: [stemmer.stem(word) for word in x])
    
    return twts['tokens']

# Ejemplo de uso de la función con un DataFrame
tweets_data = pd.DataFrame({
    'tweet': ["This is a sample tweet 😊 ", "Another tweet ❤️ emoji"]
})

tokens = create_tokens(tweets_data)
print(tokens)

# Convertir tokens a un modelo de frecuencia de documentos (CountVectorizer)
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
dfm_tws = vectorizer.fit_transform([' '.join(token) for token in tokens])

print(dfm_tws.toarray())
