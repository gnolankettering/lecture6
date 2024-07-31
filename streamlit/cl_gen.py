import openai
import streamlit as st
import config


openai.api_key = config.OPENAI_API_KEY


st.header("CL Generator")

contact_person = st.text_input('Contact Person')
your_name = st.text_input('Your name')
role = st.text_input('Role')
company_name = st.text_input('Company Name')
personal_exp = st.text_area('Personal Experience')
job_desc = st.text_area('Job Description')
hobbies = st.text_area('Hobbies')

def app():
    
    if st.button('Generate Cover Letter'):
        cover_letter = generate_cover_letter(
            contact_person=contact_person,
            your_name=your_name,
            role=role,
            company_name=company_name,
            personal_experience=personal_exp,
            job_description=job_desc,
            hobbies=hobbies
        )
        #print(cover_letter)
        with st.expander("Cover Letter"):
            st.text_area("Generated Cover Letter", 
                         cover_letter, height=500)


def generate_cover_letter(contact_person,
                          your_name,
                          role,
                          company_name,
                          personal_experience,
                          job_description,
                          hobbies):
    prompt_template = """ 
     Write a cover letter to {contact_person}
    from {your_name} for a {role} job at {company_name}.
    I have experience in {personal_experience}.
    I am excited about the job because {job_description}.
    I am passionate about {hobbies}.
    Make sure to incorporate the following points in the cover letter:
     - highlight the skills and experiences
     - show case achievements
     - use keywords fromt the job description
     - teamwork
     - attention to detail
    Also, make sure that the cover letter is typo free.
    """
    prompt = prompt_template.format(
         contact_person=contact_person,
         your_name=your_name,
         role=role,
         company_name=company_name,
         personal_experience=personal_experience,
         job_description=job_description,
         hobbies=hobbies)
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}

           ])
    return response.choices[0].message.content

def main():
    app()
 
    
if __name__ == "__main__":
    main()
    


