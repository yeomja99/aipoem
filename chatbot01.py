import openai
import streamlit as st


OPENAI_API_KEY = '8c91c5c7058847f3820f9d7c12bbb1fb'
OPENAI_API_ENDPOINT='https://sktfly-ai.openai.azure.com/' 
OPENAI_API_TYPE = 'azure'
OPEN_API_VERSION = '2023-05-15'


openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPEN_API_VERSION

st.header('인공지능 시인 서비스', divider='rainbow')

name = st.text_input('이름을 입력하세요')
if name: 
    st.write(name+'님 반감습니다.')

subject = st.text_input('주제를 입력하세요.')
content = st.text_area('시의 내용을 입력하세요')

button_result = st.button('RUN')
if button_result:
    with st.spinner('please wait....'):
        result = openai.chat.completions.create(
                        model = 'dev-gpt-35-turbo',
                        temperature=1,
                        messages=[
                            {'role':'system','content':'You are a helpful assistant.'},
                            {'role':'user','content':'작가의 이름은 '+name},
                            {'role':'user','content':'시의 주제는 '+subject},
                            {'role':'user','content':'시의 내용은 '+content},
                            {'role':'user','content':'이 내용으로 시를 지어줘'}
                        ]
                    )

    st.write(result.choices[0].message.content)
    st.success('done')