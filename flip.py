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
    
    angle = st.sidebar.text_input('Flip Direction')
    st.sidebar.text('''
                    0: horizontal flip
                    1: vertical flip
                    -1: for both
                    ''')
    image_name = ''

    st.title('Upload Image')

    file = st.file_uploader('Choose an image....', type=['png', 'jpg'])

    if file is not None:
        if angle == '':
            st.error('Enter Flip Direction value')
            
        else:
            image = Image.open(file)
            image_name = file.name
            
            st.image(image, caption='Image')
            st.write(file.name)

            image = np.array(plt.imread(image_name))

            new_image = flip_image(image, int(angle))
            st.image(new_image)
            st.write('New Image')
            
            st.markdown(download_image(new_image), unsafe_allow_html=True)
