from deep_translator import GoogleTranslator
import tkinter as tk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


data = pd.read_csv("dataset.csv")
print("Örnek olarak bu cümleleri deneyebilirsiniz." "\n"
        "வணக்கம் இன்று வெள்ளிக்கிழமை" "\n"
        "Hoy entregamos nuestro proyecto final en nuestra clase de programación avanzada.""\n"
        "Этот проект посвящен определению языка и переводу.""\n"
        "프로젝트가 마음에 드셨나요?")

pencere = tk.Tk()
pencere.title("Dil Algılama ve Çevirme Optimizasyonu")
pencere.geometry('750x350+100+100')


etiket = tk.Label(pencere, text="Dil Algılama ve Çevirme Optimizasyonuna Hoş Geldiniz!" "\n"
                                "Text alanına herhangi dilde kelime/cümle girin." "\n", fg='black')
etiket.pack()

kelimeGir = tk.Entry(pencere)
kelimeGir.pack()

def diliAlgila(data):

    user = kelimeGir.get()

    x = np.array(data["Text"])
    y = np.array(data["language"])
    cv = CountVectorizer()
    X = cv.fit_transform(x)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    model.score(X_test, y_test)
    data = cv.transform([user]).toarray()
    output = model.predict(data)
    sonuc["text"] = output[0]

def dilCevir(data):
    user = kelimeGir.get()
    translated = GoogleTranslator(source='auto', target='tr').translate(text=user)
    sonuc['text']= translated

def cikis():
    pencere.destroy()

Button = tk.Button(pencere, text="Dili Algıla", command=lambda: diliAlgila(data), fg="blue")
Button.pack()
Button1 = tk.Button(pencere, text= "Dili Çevir", command=lambda: dilCevir(data), fg="blue")
Button1.pack()
cikisButonu = tk.Button(pencere, text="Çıkış", command=quit, fg="blue")
cikisButonu.pack()
sonuc = tk.Label(pencere, fg="black")
sonuc.pack()

pencere.mainloop()




