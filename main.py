from misteral import get_response
import streamlit as st



st.title("hello from javna , misteral api llm")
st.write("write down your question here :")


user_input = st.text_area("enter your question : " , "" )


if st.button("ask misteral"):
    if user_input:
        misteral_out = get_response(user_input)
        
        st.success("generated text : ")
        st.write(misteral_out)
        
    else:
        st.error("enter pleeeeese your question")