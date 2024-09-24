#photoreader
pip install exifread
import streamlit as st
from PIL import Image
import exifread
import pandas as pd
import os

def extract_exif_data(image_file):
    tags = exifread.process_file(image_file)
    
    # Extract ISO
    iso = tags.get('EXIF ISOSpeedRatings', 'N/A')
    
    # Extract Shutter Speed
    shutter_speed = tags.get('EXIF ExposureTime', 'N/A')
    
    # Extract Aperture
    aperture = tags.get('EXIF FNumber', 'N/A')
    
    return iso, shutter_speed, aperture

def process_images(uploaded_files):
    data = {'Image': [], 'ISO': [], 'Shutter Speed': [], 'Aperture': []}
    
    for uploaded_file in uploaded_files[:50]:  # Limit to 50 photos
        iso, shutter_speed, aperture = extract_exif_data(uploaded_file)
        data['Image'].append(uploaded_file.name)
        data['ISO'].append(iso)
        data['Shutter Speed'].append(shutter_speed)
        data['Aperture'].append(aperture)
    
    return pd.DataFrame(data)

def main():
    st.title("EXIF Data Extractor")
    st.write("Upload up to 50 images to extract ISO, Shutter Speed, and Aperture data.")
    
    # Allow the user to upload multiple files
    uploaded_files = st.file_uploader("Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    if uploaded_files:
        exif_data_df = process_images(uploaded_files)
        st.write("EXIF Data:")
        st.dataframe(exif_data_df)
    else:
        st.write("No images uploaded yet.")

if __name__ == '__main__':
    main()
