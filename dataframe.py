# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data #매번 로드시 과부하 발생으로 캐시 데이터를 사용하게 하는것
def load_data():
    df = pd.read_csv("gapminder.tsv", sep="\t") # 외부 텍스트 데이터 ,tsv는 텍스트 파일(csv,tsv= 콤마나 콜론 사용시 이것),구분자를 해야지만 판다스에서 인식 가능.
    # -> 데이터프레임 반환
    return df

def plot_matplotlib():
    st.title(" Bar Plot")
    df = load_data() #데이터 준비.
    # 그래프 그리기
    fig, ax = plt.subplots() 
    
    # 막대 그래프
    sns.barplot(x=df['year'], y=df['lifeExp'], data=df, ax=ax)
    # x축 들어갈 열 데이터. y는 두번째 열을 이용해 추출
    # Labeling axes and title
    ax.set_xlabel("year")
    ax.set_ylabel("lifeExp")
    ax.set_title("Year vs. lifeExp")
    # 웹 앱 시각화
    st.pyplot(fig)

def main():
    st.title("데이터 시각화 : 표 & 그래프") #write 쓰는것보다 폰트가 좋아서 사용
   
    df = load_data() # 데이터 불러오기.
    st.dataframe(df, use_container_width=True) # 첫번째 표

    #pandas style
    st.title("컬럼별 최대값 표") 
    st.dataframe(df.iloc[:5,2:].style.highlight_max(axis=0)) #두번째 표.
    # 처음 행부터 5번째까지,열은 3번째부터 끝까지.월래는 이렇게 하면 오류가 발생.
    plot_matplotlib() #그래프
    
    
if __name__ == "__main__":
    main()