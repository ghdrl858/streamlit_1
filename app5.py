from email.mime import audio
import streamlit as st
import pandas as pd

# 이미지 처리를 위한 라이브러리
from PIL import Image
def main() :
    # 1. 저장되어있는 이미지 파일을 화면에 표시하기
    img = Image.open('data2/image_03.jpg')

    st.image(img)

    st.image(img, use_column_width = True)

    # 2. 인터넷상에 있는 이미지를 화면에 표시하기
    # URL이 있는 이미지를 말함
    url = 'https://newsimg.hankookilbo.com/cms/articlerelease/2021/10/14/2241ae05-7b8d-414a-ba55-128f479b5688.jpg'
    st.image(url)

    # 3. 비디오 영상 화면에 표시하기
    video_file = open('data2/secret_of_success.mp4', 'rb')
    st.video(video_file)

    # 4. 오디오 파일 화면에 표시하기
    audio_file = open('data2/song.mp3', 'rb')
    st.audio(audio_file.read(), format = 'audio/mp3')

if __name__ == '__main__' :
    main()