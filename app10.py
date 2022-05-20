import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() :
    st.title('차트 그리기')

    df = pd.read_csv('data2/iris.csv')

    st.write(df)

    # 차트 그리기
    # sepal_length와 sepal_width의 관계를 차트로 나타내시오

    ## plt와 seaborn 차트를 streamlit에 그리는 방법. ##

    # Scaater 그래프
    fig = plt.figure()
    plt.scatter(data = df, x = 'sepal_length', y = 'sepal_width')
    plt.title('Sepal Length vs width')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal width')
    st.pyplot(fig)

    # seaborn으로 그린 Scatter 그래프
    fig2= plt.figure()
    sns.scatterplot(data = df, x = 'sepal_length', y = 'sepal_width')
    plt.title('Sepal Length vs width')
    st.pyplot(fig2)

    # reglet이 있는 Scatter 그래프
    fig3 = plt.figure()
    sns.regplot(data = df, x = 'sepal_length', y = 'sepal_width')
    st.pyplot(fig3)

    # sepal_length로 히스토그램을 그린다.
    # bin의 갯수는 20개
    fig4 = plt.figure()
    plt.hist(data = df, x = 'sepal_length', bins = 20, rwidth = 0.8)
    st.pyplot(fig4)

    # sepal_length 히스토그램을 그리되,
    # bin의 갯수를 10개와 20개로
    # 두 개의 차트를 수평으로 보여주기\
    fig5 = plt.figure(figsize = (10, 4))
    plt.subplot(1, 2, 1)
    plt.hist(data = df, x = 'sepal_length', bins = 10, rwidth = 0.8)

    plt.subplot(1, 2, 2)
    plt.hist(data = df, x = 'sepal_length', bins = 20, rwidth = 0.8)
    st.pyplot(fig5)

    # species 컬럼의 데이터를 각각 몇개씩 있는지
    # 차트로 나타내시오
    fig6 = plt.figure()
    sns.countplot(data = df, x = 'species')
    st.pyplot(fig6)

    ## 데이터프레임이 제공하는 차트함수, streamlit에 그리기 ##

    # species는 각각 몇개인지 데이터프레임의 차트로 그리는 방법
    fig7 = plt.figure()
    df['species'].value_counts().plot()
    st.pyplot(fig7)

    # sepal_length 컬럼을 히스토그램으로 그리기
    fig8 = plt.figure()
    df['sepal_length'].hist(bins = 40)
    st.pyplot(fig8)

if __name__ == '__main__' :
    main()