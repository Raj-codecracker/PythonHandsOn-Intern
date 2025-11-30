import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Streamlit app of VGU")
st.text("Welcome to the Dashboard")
st.header("I'm Header")
st.write("You can write", 10+5)
name= st.text_input("Enter your Name: ")
age= st.number_input("Enter your age: ")
st.write("Your name is : ", name, "Your age is: ", age)
st.selectbox("Enter Course: ", ["BCA", "B.Tech", "MCA"])
if st.button("CLICK ME"):
    st.write("Button Clicked successfully")
file = st.file_uploader("Upload Your File")
if file:
    content = file.read()
    st.write("File Uploaded Successfully!!!!")
    
data = {"Name": ["Pataysa", "Natureshe","kumans"], "Marks":[14,23,17,]}
df = pd.DataFrame(data)

st.dataframe(df)

data = pd.DataFrame({
    "Marks": [14,23,17]
})
st.line_chart(data)
st.bar_chart(data)

Subject=["Python", ["C++"],["Java"]]
marks=[14,17,19]

fix, ag = plt.subplot()
ax.pies(marks,labels=Marks)
st.pyplot(fig)