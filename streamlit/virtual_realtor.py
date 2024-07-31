import openai
import streamlit as st
import config


openai.api_key = config.OPENAI_API_KEY

st.header("Virtual Realtor 👩🏽‍⚕️")

st.subheader("``Have a Question? ASK Me!`` (Max. 500 characters)")

user_input = st.text_area("", placeholder="Ask away...",
                          height=200, key="key")

sys_prompt = """
You are a extremely knowledgeable realtor who also knows
  everything one needs to know about buying and selling homes in the USA.
  You also specialize in new, first-time homebuyers. 
  Your name is Layala and you are 38 years old. 
  You understand how to help homebuyers to get the best homes on their budget. 
  Your job is to assist users with questions related to buying homes and getting steps for 
  them to get approved on loans available so they can buy a home.
  When answering questions related to your expertise, you'll answer with confidence,
  but make sure to give answers that are true, correct and legal.  
  If you don't have the answer for the questions you might be asked, simply say "I don't know
  the answer to that" and then proceed to giving them advice on where to get that answer.
"""


if st.button("Send Questions ➡", type="primary"):
    my_input = """ {input_var}, Generate a response with less
    than 1000 characters."""
    
    prompt_template = my_input.format(
        input_var=user_input
    )
    
    st.markdown("----")
    
    box = st.empty()
    
    response = []
    messages = []
    
    call = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt_template}
        ],
        temperature=0.5,
        max_tokens=1000,
        n=1)
    result = call.choices[0].message.content
    box.markdown(f"**{result}**")
        
    st.markdown("----")
        
        
    
