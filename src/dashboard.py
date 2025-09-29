import streamlit as st 
import random

choices = (":fist: Rock", ":raised_back_of_hand: Paper", ":v: Scissors")
st.title(":fist: Rock :raised_back_of_hand: Paper :v: Scissors Game")
user_choice = st.radio("Choose!", (":fist: Rock", ":raised_back_of_hand: Paper", ":v: Scissors"))


if st.button("Play!"):
    computer_choice = random.choice(choices)
    st.write("Computer Choice:", computer_choice)

    if user_choice == computer_choice:
        st.title("It's a tie!")
    elif (user_choice == ":fist: Rock" and computer_choice == ":v: Scissors") or \
         (user_choice == ":raised_back_of_hand: Paper" and computer_choice == ":fist: Rock") or \
         (user_choice == ":v: Scissors" and computer_choice == ":raised_back_of_hand: Paper"):
        st.title("🎉 Congratulations! You won.")
    else:
        st.title("😢 You lost...")