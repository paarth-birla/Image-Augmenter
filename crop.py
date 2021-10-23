import streamlit as st
from PIL import Image
from techniques import *
from io import BytesIO
import base64

def download_image(image):
    result = Image.fromarray(image)
    
    buffered = BytesIO()
    result.save(buffered, format='JPEG')
    result_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{result_str}"><input type="button" value="Download"></a>'
    return href
    
    
def app():
    
    x1 = st.sidebar.text_input('x1')
    y1 = st.sidebar.text_input('y1')
    x2 = st.sidebar.text_input('x2')
    y2 = st.sidebar.text_input('y2')
    image_name = ''

    st.title('Upload Image')

    file = st.file_uploader('Choose an image....', type=['png', 'jpg'])

    if file is not None:
        if x1 != '' and y1 != '' and x2 != '' and y2 != '':
            image = Image.open(file)
            image_name = file.name
            st.image(image)
            image = np.array(plt.imread(image_name))
            new_image = crop_image(image, int(x1), int(y1), int(x2), int(y2))
            st.image(new_image)
            
            st.markdown(download_image(new_image), unsafe_allow_html=True)
        
        else:
            st.error('Fill all Values')