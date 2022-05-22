import imp
from sqlalchemy import asc
import streamlit as st
import pandas as pd

import altair as alt
import plotly.express as px

def main() :
    # plotly 라이브러리를 이용한 차트 그리기(스트림릿 제공)
    df4 = pd.read_csv('data2/prog_languages_data.csv', index_col = 0)
    st.dataframe(df4.sort_values('Sum', ascending = False).head(5))

    # plotly의 bar차트
    df4_sorted = df4.sort_values('Sum', ascending = False)
    fig2 = px.bar(df4_sorted, x = 'lang', y = 'Sum')
    st.plotly_chart(fig2)

if __name__ == '__main__' :
    main()