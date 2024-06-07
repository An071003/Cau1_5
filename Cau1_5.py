import streamlit as st
import pandas as pd
import numpy as np

st.title('My first deployed DL model')
st.header('Header đây chứ đâu')
st.write('Đây là text')
st.markdown('Markdown đây __anh em ơi__')
st.text('Còn dưới đây là latex')
st.latex(r'''a + b = 3''')
st.write(12345)
st.code('''
def hello:
    print("hello world!")
''', language='python')

st.text('Hiển thị luôn cả char')

char = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

st.line_chart(char)