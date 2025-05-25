import streamlit as st
import numpy as np
import pandas as pd
import pickle

with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)


main_model = data["main_model"]
coor_model=data["coor_model"]
model_encoder = data["rfr_encoder"]
scaler=data['rfr_scaler']

def show_predict_page():
    st.title('Tuition Prediction in Canada')

    st.write("""### Student information""")

    years=(['2017/2018',
           '2018/2019',
           '2019/2020',
           '2020/2021',
           '2021/2022',
           '2022/2023',
           '2023/2024',
           '2024/2025'])
    
    geo=(['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia',
       'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan',
       'Alberta', 'British Columbia', 'Yukon'])
    
    Field=(['Education',
       'Visual and performing arts, and communications technologies',
       'Humanities', 'Social and behavioural sciences, and legal studies',
       'Business, management and public administration',
       'Physical and life sciences and technologies',
       'Mathematics, computer and information sciences', 'Engineering',
       'Agriculture, natural resources and conservation', 'Medicine',
       'Nursing', 'Pharmacy',
       'Other health, parks, recreation and fitness',
       'Personal, protective and transportation services',
       'Veterinary medicine', 'Law', 'Architecture', 'Dentistry',
       'Optometry', 'Regular MBA', 'Executive MBA'])
    levels=(['undergrad','grad'])

    nationality=(['canadian','international'])

    year=st.selectbox('year', years)          
    province=st.selectbox('Geo',geo)
    field=st.selectbox('field', Field)
    level=st.selectbox('level',levels)
    nationality=st.selectbox('nationality', nationality)

    predict=st.button('Predict tuition')
    if predict:
        inputs={'REF_DATE':[year],
                'GEO':[province],
                'Field of study':[field],
                'Level of study':[level],
                'nationality':[nationality]}
        
        to_enc_data=pd.DataFrame.from_dict(inputs)

        encode=model_encoder.transform(to_enc_data)
        encoded_input=pd.DataFrame(encode,columns=model_encoder.get_feature_names_out())
        
        coor_features=encoded_input[['GEO','Field of study','Level of study','nationality']]
        encoded_input['COORDINATE']=coor_model.predict(coor_features)


        col=encoded_input.pop('COORDINATE')
        encoded_input.insert(0, 'COORDINATE', col)

        scaled_input=scaler.transform(encoded_input)

        tuition=main_model.predict(scaled_input)

        st.subheader(f'The estimated tuition is {tuition[0]:.2f}$')



                







