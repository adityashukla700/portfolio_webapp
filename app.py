from turtle import right
import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Aditya Shukla Portfolio Webpage",page_icon="chart_with_upwards_trend",layout="wide")

#asset
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_z2vighsa.json")


# Header
lottie_react=load_lottieurl("https://assets5.lottiefiles.com/datafiles/fab7172a9302d416bcdb8ac7e1c71123/data.json")
with st.container():
    
    st.subheader("Hi, I am Aditya Shukla :wave:")
    st.title("React JS Developer")
    left_column,right_column=st.columns(2)
    with left_column:
        st.write("React JS developer, working on increasing user engagement through beautiful UI designs.")
        st.subheader("Certifications: ")
        st.markdown('''
        1. ***React Js*** \n
            Certificate from learncodeonline.in on React JS
        2. ***Introduction to JavaScript*** \n
            Certificate from geeks for geeks.
        3. ***Introduction to MySQL*** \n
            Certificate from geeks for geeks
        ''')
    with right_column:
        st_lottie(lottie_react,height=350,key="react")


#Work Description
with st.container():
    st.write("----")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("Passion")
        st.write("I am a student pursuing BTech in Computer Science from JK Lakshmipat University. I am passionate about react js as well as data science and machine learning.")
        st.header("Achievements")
        st.subheader("Research Paper selected for Oral Presentation")
        st.write("Research Paper selected for Oral Presentation in International Conference on “Sustainable Future: Innovations in Education. We were the only students whose paper was selected. Rest were professors or Research Scholar")
        st.subheader("Student Coordinator at National Science Day Event")
        st.write("Student Coordinator of the National Science Day event. Successfully completed the event ensuring maximum participation and organized Poster Presentation as well as Quiz Competition in it")
        st.subheader("Skills")
        st.write('''
        
                ***React JS***,***HTML***,***CSS***,***SQL***,***JAVA*** ,***PYTHON***       
        ''')

        st.subheader("Coding Profiles")
        st.write("[***Leetcode***](https://leetcode.com/aditya7002/)")
        st.write("[***CodeChef***](https://www.codechef.com/users/adityashukla70)")
    with right_column:
        st_lottie(lottie_coding,height=500,key="coding")

 #Contact me

with st.container():
    st.write("----") 
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form='''
    <form action="https://formsubmit.co/adityashuklaatwork@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Name" required>
     <input type="email" name="email" placeholder="Email" required>
     <textarea name="message" placeholder="Enter your message" required></textarea>
     <button type="submit">Send</button>
    </form>
    '''
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()

def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
css("style.css")
