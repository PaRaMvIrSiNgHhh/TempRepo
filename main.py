import streamlit as st

st.title("My First Streamlit App")
st.subheader("K hal h ladle")
st.text("jan koni  da kisi na bhi")

var1 = st.selectbox("Your select: ", ["study 6 hours ","study more than 8 hours", "study more than 10 hours"])
st. write(f"i am studying {var1}") 

st.write("Hello, Streamlit!")

st.checkbox("efforts")

st.radio("pick your efforts type: ",["hard","harder","hardest","insane"])
st.selectbox("choose your success time:",["2 months", "3 months","1 year"])