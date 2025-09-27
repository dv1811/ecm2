import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    st.title ('This is a ecomm application for data science')
    st.sidebar.title ('Upload your file')
    st.checkbox('Python Developer')
    st.checkbox('I have also developed LEA')
    st.checkbox('PowerApps Developer')
    st.multiselect('Select your role', options= ['Data Scientist','Data Analyst', 'Data Engineer'],max_selections= 2)
    uploaded_file = st.sidebar.file_uploader('Upload your file here', type = ['.csv', '.xlsx'],accept_multiple_files= False)

    if uploaded_file is not None:
        try: 
            if uploaded_file.name.endswith('.csv'):
               df = pd.read_csv(uploaded_file)
            else:
               df = pd.read_excel(uploaded_file)
            
            st.sidebar.success ('File uploaded successfully')
            st.subheader ('Data Overview')
            st.data_frame = df.head(5)

            st.subheader('Basic information of the data')
            st.write ( 'The Shape of data is', df.shape)
            st.write ('Columns in the data are', df.columns)
            st.write ('Missing value chart is', df.isnull().sum())

            st.subheader ('Data Analytics')
            st.write(df.describe())

            st.subheader ('Correlation Chart')
            st.write(df.corr(numeric_only=True))

        except Exception as e:
            'Try again'

    else: pass

if __name__ == '__main__':
    main()

