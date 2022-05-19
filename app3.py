import streamlit as st
import pandas as pd

def main() :
    df = pd.read_csv('data2/iris.csv')
    st.dataframe(df)

    species = df['species'].unique()

    st.text('아이리스 꽃은 ' + species + '으로 되어있다.')

    # 헤더를 사용해 웹페이지에 표시하는 방법(두가지)
    st.dataframe(df.head())
    st.write(df.head())

if __name__ == '__main__' :
    main()