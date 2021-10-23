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
    href = f'<a href="data:file/png;base64,{result_str}"><input type="button" value="Download"></a>'
    return href
    
    
def app():
    
    width = st.sidebar.text_input('Width')
    height = st.sidebar.text_input('Height')
    image_name = ''

    st.title('Upload Image')

    file = st.file_uploader('Choose an image....', type=['png', 'jpg'])

    if file is not None:
        if width == '' and height == '':
            st.error('Enter Width and Height value')
        
        elif width == '' and height != '':
            st.error('Enter Width value')
        
        elif width != '' and height == '':
            st.error('Enter Height value')
        
        else:
            image = Image.open(file)
            image_name = file.name
            st.image(image)
            image = np.array(plt.imread(image_name))
            new_image = resize_image(image, int(width), int(height))
            st.image(new_image)
            
            st.markdown(download_image(new_image), unsafe_allow_html=True)
