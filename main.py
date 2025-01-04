import google.generativeai as genai
import streamlit as st

st.logo('logo.jpeg', size="large", link=None, icon_image=None)
st.title("BB Chatbot",anchor="the-title")
st.subheader("Interact with the study companion")
title_alignment="""
<style>
#the-title {
  text-align: center;
  font-size:5rem;
  background: linear-gradient(
        to right,
        #7953cd 20%,
        #00affa 30%,
        #0190cd 70%,
        #764ada 80%
    );
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    text-fill-color: transparent;
    background-size: 500% auto;
    animation: textShine 5s ease-in-out infinite alternate;

}
@keyframes textShine {
    0% {
        background-position: 0% 50%;
    }
    100% {
        background-position: 100% 50%;
    }
}

</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)
title_alignment="""
<style>
.stLogo {
  margin-top:-15px;
  height:100px;
  width:100px;
}
#interact-with-the-study-companion {
  text-align:center;
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="tunedModels/qnadatasetfinal-6qdw6nwwgtfu",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)
text_input=st.text_area("Message BB Chatbot:")
if text_input!="" or st.button("Generate Response"):
    response = chat_session.send_message(text_input)
    st.write(response.text)
