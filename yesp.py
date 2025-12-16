import streamlit as st
import random
st.title("welcome to crush predictor")
your_name=st.text_input("Enter your name: ")
crush_name=st.text_input("Enter your crush name: ")
if st.button("Predict"):
   if your_name and crush_name:
        results = ["Secret Crush", "Best Friend", "Soulmate"]
        prediction = random.choice(results)
        st.write("predicting your relationship....")
        st.write(f"**{your_name.title()} {crush_name.title()}**")
        st.write(f"Result:{prediction}")
   else:
       st.warning("Please enter both names")
