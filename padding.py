import streamlit as st
from PIL import Image, ImageColor
from techniques import *
from io import BytesIO
import base64
from matplotlib import colors

def download_image(image):
    result = Image.fromarray(image)
    
    buffered = BytesIO()
    result.save(buffered, format='JPEG')
    result_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{result_str}"><input type="button" value="Download"></a>'
    return href
    
    
def app():
    
    leftBorder = st.sidebar.text_input('Left Border')
    topBorder = st.sidebar.text_input('Top Border')
    rightBorder = st.sidebar.text_input('Right Border')
    bottomBorder = st.sidebar.text_input('Bottom Border')
    color = st.sidebar.color_picker('Color')
    image_name = ''

    st.title('Upload Image')

    file = st.file_uploader('Choose an image....', type=['png', 'jpg'])

    if file is not None:
        if topBorder != '' and leftBorder != '' and rightBorder != '' and bottomBorder != '':
            image = Image.open(file)
            image_name = file.name
            st.image(image)
            image = np.array(plt.imread(image_name))
            if color != '':
                color_list = ImageColor.getcolor(color, 'RGB')
                new_image = padding_image(image, int(topBorder), int(bottomBorder), int(leftBorder), int(rightBorder), color_list)
            
            else:
                new_image = padding_image(image, int(topBorder), int(bottomBorder), int(leftBorder), int(rightBorder))
            st.image(new_image)
            
            st.markdown(download_image(new_image), unsafe_allow_html=True)
        
        else:
            st.error('Fill All Values')