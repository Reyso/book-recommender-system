import pickle
import streamlit as st
import numpy as np

st.header('Smart Books Recommender System')

model = pickle.load(open('models/model.pkl','rb'))
book_names = pickle.load(open('models/book_name.pkl','rb'))
final_rating = pickle.load(open('models/final_rating.pkl','rb'))
book_pivot = pickle.load(open('models/book_pivot.pkl','rb'))

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url= []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['Image-URL-L']
        poster_url.append(url)

    return poster_url

def recomendation_books(book_name):
    book_list = []
    index = np.where(book_pivot.index==book_name)[0][0] #obtendo o nome do livro
    distance , suggestions = model.kneighbors(book_pivot.iloc[index,:].values.reshape(1,-1),n_neighbors=6) #5 vizinhos mais próximos

    poster_url = fetch_poster(suggestions)

    for i in range(len(suggestions)):
        book = book_pivot.index[suggestions[i]]
        for j in book:
            book_list.append(j)
    
    return book_list,poster_url


selected_books = st.selectbox(
    'Digite ou selecione o livro',
    book_names
    #'Type or select a book'
)

if st.button('Show me more like this'):
    recomendation_books , poster_url =  recomendation_books(selected_books)
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(recomendation_books[1])
        st.image(poster_url[1])

    with col2:
        st.text(recomendation_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recomendation_books[3])
        st.image(poster_url[3])

    with col4:
        st.text(recomendation_books[4])
        st.image(poster_url[4])

    with col5:
        st.text(recomendation_books[5])
        st.image(poster_url[5])

