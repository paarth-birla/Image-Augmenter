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
    
    direction = st.sidebar.text_input('Direction')
    shift = st.sidebar.text_input('Shift')
    image_name = ''

    st.title('Upload Image')

    file = st.file_uploader('Choose an image....', type=['png', 'jpg'])

    if file is not None:
        if direction == '' and shift == '':
            st.error('Enter direction and shift value')
        
        elif direction == '' and shift != '':
            st.error('Enter direction value')
        
        elif direction != '' and shift == '':
            st.error('Enter shift value')
            
        else:
            image = Image.open(file)
            image_name = file.name
            
            st.image(image, caption='Image')
            st.write(file.name)

            image = np.array(plt.imread(image_name))

            new_image = translate(image, direction=direction, shift=int(shift))
            st.image(new_image)
            st.write('New Image')
            
            st.markdown(download_image(new_image), unsafe_allow_html=True)
