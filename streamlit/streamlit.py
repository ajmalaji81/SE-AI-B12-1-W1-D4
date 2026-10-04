import streamlit as st

st.title("My Streamlit App")
st.header("Welcome to the Streamlit App")
st.subheader("This is a simple Streamlit application.")
st.text("You can add more Streamlit components here.")
st.markdown("Streamlit allows you to create interactive web applications easily.")

name = st.text_input("Enter your name:")
st.write("Hello", name)

age = st.number_input("Enter your age:", min_value=0, max_value=120)
st.write("Your age is:", age)

if st.button("Submit"):
    st.success(f"Thank you, {name}! Your age is {age}.")

number = st.slider("Select a value:", 0, 100)
st.write("You selected:", number)

city = st.selectbox("Select your city:", ["Puducherry", "Delhi", "Chicago", "Houston", "Phoenix"])
st.write("You selected:", city)

agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("You can proceed with the application.")
    

st.success("This is a success message.")
st.warning("This is a warning message.")
st.error("This is an error message.")
st.info("This is an informational message.")
