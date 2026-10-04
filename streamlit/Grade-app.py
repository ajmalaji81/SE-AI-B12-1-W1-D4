import streamlit as st  

st.title("Student Grade Calculator")

st.header("Welcome to the Student Grade Calculator")

Name = st.selectbox("Select your Name:", ["Ajmal", "Aishwarya", "Ananya", "Anjali", "Anushka", "Arjun", "Aryan", "Ayaan", "Diya", "Ishaan", "Kavya", "Krishna", "Maya", "Neha", "Riya", "Saanvi", "Siddharth", "Tanvi", "Tanishq", "Vihaan"])
st.write("You selected:", Name)

st.selectbox("Select your Class:", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5"])

with st.form("grade_form"):
    st.write("Enter your mark to get the corresponding grade.")
    mark = st.number_input("Enter your mark (0-100):", min_value=0.0, max_value=100.0, step=1.0)
    submitted = st.form_submit_button("Submit")



    if submitted:
        # Check if the mark is valid
        if mark < 0 or mark > 100:
            Grade = "Invalid mark"
        elif mark >= 90:
            Grade = "A"
        elif mark >= 80:
            Grade = "B"
        elif mark >= 70:
            Grade = "C"
        elif mark >= 60:
            Grade = "D"
        else:
            Grade = "E"

        # Display the mark and corresponding grade
        st.subheader(f"Your mark is: {mark}")
        st.header (f"{Name}'s grade is : {Grade}")
        if mark  >= 90 :
                st.success("Excellent! You have an A grade.")
        elif mark >= 80:
                st.success("Great job! You have a B grade.")
        elif mark >= 70:
                st.success("Good effort! You have a C grade.")
        elif mark >= 60:
                st.warning("You have a D grade. Consider improving.")
        else:
                st.error("You have an E grade. You need to work harder.")

