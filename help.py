import streamlit as st

def app():
    st.markdown('''# Commands''')
    st.markdown('''
                ## Scaling
                Image is resized to given size, eg: width can be doubled or heigth can halved.
                ''')
    st.image('./images/resize.jpg')
    
    st.markdown('''
                ## Cropping
                A portion of image is selected.
                ''')
    st.image('./images/crop.jpg')
    
    st.markdown('''
                ## Padding
                the image is padded with given set of values, eg: left, top, right, bottom border value can be given inout as well as color of padding can also be choosen.
                ''')
    st.image('./images/pad.jpg')
    
    st.markdown('''
                ## Flipping
                the image if flipped is horizontally or vertically.
                ''')
    st.image('./images/flip.jpg')
    
    st.markdown('''
                ## Translation
                The image is shifted in either of the four directions.
                ''')
    st.image('./images/transform.jpg')
    
    st.markdown('''
                ## Rotation
                The image is rotated by certain degree.
                ''')
    st.image('./images/rotate.jpg')