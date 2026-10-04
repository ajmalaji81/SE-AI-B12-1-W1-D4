import streamlit as st
st.title("BMI Calculator")
st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")

#2 Input fields for weight and height
weight = st.number_input("Enter your weight (in kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (in meters):", min_value=0.1, step=0.01)

#3 Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")

        #4 Determine BMI category
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than zero.")
