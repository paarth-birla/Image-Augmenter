import streamlit as st
import translate
import help
import crop
import resize
import padding
import flip
import rotate
from multipage import MultiPage

st.set_page_config(
    page_title = 'Image Augmentor',
    layout='wide',
    initial_sidebar_state='collapsed'
)

app = MultiPage()


app.add_page('Help', help.app)
app.add_page('Scale Image', resize.app)
app.add_page('Crop Image', crop.app)
app.add_page('Pad Image', padding.app)
app.add_page('Flip Image', flip.app)
app.add_page('Translate Image', translate.app)
app.add_page('Rotate Image', rotate.app)

app.run()