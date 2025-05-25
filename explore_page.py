import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df1=pd.read_csv("c_undegrad.csv")
df1=df1.drop(['STATUS', 'SYMBOL','TERMINATED'], axis=1)
df1['VALUE'] = df1['VALUE'].fillna(df1.groupby(['GEO', 'Field of study'])['VALUE'].transform("mean"))
df1=df1.dropna()
df1['Level of study']='undergrad'
df1['nationality']='canadian'

df2=pd.read_csv('c_grad.csv')
df2=df2.drop(['STATUS', 'SYMBOL','TERMINATED'], axis=1)
df2['VALUE'] = df2['VALUE'].fillna(df2.groupby(['GEO', 'Field of study'])['VALUE'].transform("mean"))
df2=df2.dropna()
df2['Level of study']='grad'
df2['nationality']='canadian'

df3=pd.read_csv('i_undergrad.csv')
df3=df3.drop(['STATUS', 'SYMBOL','TERMINATED'], axis=1)
df3['VALUE'] = df3['VALUE'].fillna(df3.groupby(['GEO','Field of study'])['VALUE'].transform("mean"))
df3=df3.dropna()
df3['Level of study']='undergrad'
df3['nationality']='international'

df4=pd.read_csv('i_grad.csv')
df4=df4.drop(['STATUS', 'SYMBOL','TERMINATED'], axis=1)
df4['VALUE'] = df4['VALUE'].fillna(df4.groupby(['GEO','Field of study'])['VALUE'].transform("mean"))
df4=df4.dropna()
df4['Level of study']='grad'
df4['nationality']='international'

df=pd.concat([df1, df2, df3, df4])

df=df.drop(['UOM','UOM_ID','SCALAR_FACTOR','SCALAR_ID','DECIMALS'], axis=1)

df=df.drop('VECTOR', axis=1)

df['DGUID']=df['DGUID'].str.replace('2016A000','').astype(int)

def show_explore_page():
    st.title("University students Tuition analysis")

    st.header('Data')

    st.write(df)

    st.header('Analysis')

    years=(['2017/2018',
           '2018/2019',
           '2019/2020',
           '2020/2021',
           '2021/2022',
           '2022/2023',
           '2023/2024',
           '2024/2025'])
    
    years=st.selectbox("Years", years)
    if years:
       year=df[df['REF_DATE']==years]

       st.subheader('What is the average price nbased on their nationality?')

       avg_price_nat=year.groupby('nationality')['VALUE'].mean()
    
       avg_price_nat=avg_price_nat.reset_index()
       fig1, ax1=plt.subplots()
       avg_price_nat_plot= sns.barplot(data=avg_price_nat,
                                x=avg_price_nat.nationality,
                                y=avg_price_nat.VALUE, 
                                hue='nationality'
                               )
       for num in avg_price_nat_plot.containers:
        avg_price_nat_plot.bar_label(num,)

       plt.title('Average price based on their nationality')
            
       st.pyplot(fig1.figure)

       st.write('We can see that international students tend to pay more than canadian students, with it being more than double')

       st.subheader('What is the average price based on their nationality and level of study?')
       
       avg_price_level_nat=year.groupby(['nationality', 'Level of study'])['VALUE'].mean()
       
       avg_price_level_nat=avg_price_level_nat.reset_index()


       fig2, ax2=plt.subplots(figsize=(15,15))
       
       avg_price_nat_level_nat_plot= sns.barplot(data=avg_price_level_nat,
                                x='nationality',
                                y='VALUE', 
                                hue='Level of study'
                               )
       for num in avg_price_nat_level_nat_plot.containers:
        avg_price_nat_level_nat_plot.bar_label(num,)

       plt.title('average price based on their level of study and nationality',fontsize=20)

       st.pyplot(fig2.figure)

       st.write('In this graph, we see that canadian undergrads pay a bit less than canadian grads. However, there is a huge difference  between international undergrads and grads')


       st.subheader('What is the least to most expensive field based on level of study and nationality?')

       field=year.groupby(['Field of study','Level of study','nationality'])['VALUE'].mean()
       field=field.reset_index()
       cad_under=field[field['Level of study']=='undergrad']
       cad_under=cad_under[cad_under['nationality']=='canadian']
       cad_under=cad_under.sort_values(by='VALUE', ascending=True)

       fig3, ax3=plt.subplots(figsize=(15,10))
       fields=sns.barplot(cad_under, 
                   x='Field of study', 
                   y='VALUE', 
                   hue='Field of study', 
                   palette='colorblind'
                  )
       plt.xticks(rotation=90,fontsize=15)
       for num in fields.containers:
         fields.bar_label(num,)
         
       plt.title('The least to most expensive field of study in for canadians undergrads', fontsize=20)

       st.pyplot(fig3.figure)

       st.write(' We can see that the programs requiring a lot of science are the most expensive ones for the canadian undergrads')

       cad_grad=field[field['Level of study']=='grad']
       cad_grad=cad_grad[cad_grad['nationality']=='canadian']
       cad_grad=cad_grad.sort_values(by='VALUE', ascending=True)

       fig4,ax4=plt.subplots(figsize=(15,10))
       fields=sns.barplot(cad_grad, 
                   x='Field of study', 
                   y='VALUE', 
                   hue='Field of study', 
                   palette='husl'
                  )
       plt.xticks(rotation=90,fontsize=15)
       for num in fields.containers:
         fields.bar_label(num,)
       plt.title('The least to most expensive field of study in for canadians grads',fontsize=20)

       st.pyplot(fig4.figure)
       
       st.write('Here we see that business programs are actually the most expensive for canadian grad students, with it being more than double')
       

       int_under=field[field['Level of study']=='undergrad']
       int_under=int_under[int_under['nationality']=='international']
       int_under=int_under.sort_values(by='VALUE', ascending=True)
       

       fig5,ax5=plt.subplots(figsize=(15,10))
       fields=sns.barplot(int_under, 
                   x='Field of study', 
                   y='VALUE', 
                   hue='Field of study', 
                   palette='Paired'
                  )
       plt.xticks(rotation=90,fontsize=15)
       for num in fields.containers:
         fields.bar_label(num,)
       plt.title('The least to most expensive field of study in for international undergrads',fontsize=20)
       st.pyplot(fig5.figure)

       st.write('For international students, we can see that they are over 17k of tuition, dentistry being more than 70k, being the most expensive program out of all of them')

       int_grad=field[field['Level of study']=='grad']
       int_grad=int_grad[int_grad['nationality']=='international']
       int_grad=int_grad.sort_values(by='VALUE', ascending=True)

       fig6,ax6=plt.subplots(figsize=(15,10))
       fields=sns.barplot(int_grad, 
                   x='Field of study', 
                   y='VALUE', 
                   hue='Field of study', 
                   palette='crest'
                  )
       plt.xticks(rotation=90,fontsize=15)
       for num in fields.containers:
         fields.bar_label(num,)
         
       plt.title('The least to most expensive field of study in for international grads',fontsize=20)
       st.pyplot(fig6.figure)

       provinces=year.groupby(['GEO', 'nationality'])['VALUE'].mean()
       provinces=provinces.reset_index().sort_values(by='VALUE', ascending=False)

       st.write('Same thing for international grads, their most expensive program is business, but them being over 15k compared to canadians who starts under 10k')

       st.subheader('What is the most expensive to least expensive province based on their nationality?')

       fig7, ax7=plt.subplots(figsize=(15,10))
       prov=sns.barplot(provinces,
                 x='GEO',
                 y='VALUE',
                 hue='nationality',
                 palette='Accent'
                )
       plt.xticks(rotation=50,fontsize=15)
       for num in prov.containers:
         prov.bar_label(num,)

       plt.title('The most to least expensive province to study based on nationality',fontsize=20)
       st.pyplot(fig7.figure)

       st.write('Here we can see that Ontario is the most expensive for both nationality, and yukon having no internation info as we removed it earlier, since we had no data')

    st.header('How did the prices over the years change?')

    change=df.groupby(['Field of study','REF_DATE', 'nationality','Level of study',])['VALUE'].mean()
    change=change.reset_index()

    c_und=change[change['nationality']=='canadian']
    c_und=c_und[c_und['Level of study']=='undergrad']

    fig8, ax8=plt.subplots(figsize=(15,15))
    sns.lineplot(c_und, x='REF_DATE', y='VALUE', hue= 'Field of study', palette='Paired')
    plt.legend(loc='upper right', fontsize='medium')
    plt.xticks(fontsize=15)
    plt.title('Rate change for canadian undergrads in the last 7 years', fontsize=30)

    st.pyplot(fig8.figure)

    st.write('We can see here that most of the programs have a solid price range. We do see a more visible increase in Dentisty and Veterinary medicine as well as pharmacy. we can also see a slight decrease in optometry.')

    c_grad=change[change['nationality']=='canadian']
    c_grad=c_grad[c_grad['Level of study']=='grad']

    fig9, ax9=plt.subplots(figsize=(15,15))
    sns.lineplot(c_grad, x='REF_DATE', y='VALUE', hue= 'Field of study', palette='Paired')
    plt.legend(loc='upper right', fontsize='medium')
    plt.title('Rate change for canadian grads in the last 7 years',fontsize=30)
    st.pyplot(fig9.figure)

    st.write('Here, we can see that most of the programs also decided to remain stable throughout the years. However, we so see that the executive MBA program has been unstable, deciding to increase in 2018 and decrease till 2022, and reincrease')

    i_und=change[change['nationality']=='international']
    i_und=i_und[i_und['Level of study']=='undergrad']

    fig10,ax10=plt.subplots(figsize=(15,15))
    sns.lineplot(c_und, x='REF_DATE', y='VALUE', hue= 'Field of study')
    plt.legend(loc='upper right', fontsize='medium')
    plt.xticks(fontsize=15)
    plt.title('Rate change for canadian undergrads in the last 7 years', fontsize=30)

    st.pyplot(fig10.figure)

    st.write('For international undergraduates students, we see that every year, we see a pretty significant increase in all of the programs, with veterinary medicine and dentistry have have a higher slope in 2022')

    i_grad=change[change['nationality']=='international']
    i_grad=i_grad[i_grad['Level of study']=='grad']

    fig11,ax11=plt.subplots(figsize=(15,15))

    sns.lineplot(i_grad, x='REF_DATE', y='VALUE', hue= 'Field of study', palette='tab20c')
    plt.legend(loc='upper right', fontsize='medium')
    plt.title('Rate change for international grads in the last 7 years',fontsize=30)
    st.pyplot(fig11.figure)

    st.write('Here, we see that there was a small by visible increase in most programs, with some being more visible than others.')
              



       






