import streamlit as st
st.write("""
# Addition of Two Numbers
""")

input1,input2=st.number_input('Enter First number'), st.number_input('Enter the Second number')

if st.button('Show Addition'):
    st.write(input1+input2)
else:
    st.write("")