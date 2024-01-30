import streamlit as st

def generate_cv(name, email, phone, education, experience, skills):
    cv = f"""
    # Curriculum Vitae

    ## Personal Information
    - **Name:** {name}
    - **Email:** {email}
    - **Phone:** {phone}

    ## Education
    - {education}

    ## Experience
    - {experience}

    ## Skills
    - {skills}
    """

    return cv

# Streamlit App
st.title("CV Generator")

# User input
name = st.text_input("Full Name:")
email = st.text_input("Email:")
phone = st.text_input("Phone:")

education = st.text_area("Education:")
experience = st.text_area("Experience:")
skills = st.text_area("Skills:")

if st.button("Generate CV"):
    cv = generate_cv(name, email, phone, education, experience, skills)
    st.markdown(cv, unsafe_allow_html=True)
