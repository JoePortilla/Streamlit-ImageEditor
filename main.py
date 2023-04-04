from turtle import width
import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown('# <center> Editor de Imagenes </center>', unsafe_allow_html=True)
st.markdown('---')

img_user = st.file_uploader('Sube tu imagen', type=['jpg', 'png', 'jpeg'])

if img_user:
    img = Image.open(img_user)
    st.markdown('## Info. de la Imagen.')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'Tamaño: {img.size}')
    with col2:
        st.markdown(f'Modo: {img.mode}')
    with col3:
        st.markdown(f'Formato: {img.format}')

    st.markdown('## Cambiar tamaño')
    width = st.number_input('Ancho', value=img.width)
    height = st.number_input('Altura', value=img.height)

    st.markdown('## Rotar')
    degree = st.number_input('Degree')

    st.markdown('## Aplicar Filtros')
    filt = st.selectbox("Filtro", options=(
        'Ninguno', 'BLUR', 'DETAIL', 'SMOOTH', 'EMBOSS'))

    s_btn = st.button('Editar')

    if s_btn:
        img_new = img.resize((width, height)).rotate(degree)

        if filt == 'BLUR':
            img_new = img_new.filter(BLUR)
        elif filt == 'DETAIL':
            img_new = img_new.filter(DETAIL)
        elif filt == 'SMOOTH':
            img_new = img_new.filter(SMOOTH)
        elif filt == 'EMBOSS':
            img_new = img_new.filter(EMBOSS)
        else:
            pass

        st.image(img_new)
