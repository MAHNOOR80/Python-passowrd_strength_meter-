import streamlit as st
import re
import random
import string

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Increase length to at least 8 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔴 Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔴 Add at least one digit (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔴 Add a special character (!@#$%^&*).")

    if score == 4:
        return "✅ Strong Password!", "green", score, []
    elif score == 3:
        return "⚠️ Moderate Password - Improve security.", "orange", score, feedback
    else:
        return "❌ Weak Password - Use suggestions below.", "red", score, feedback

# Function to generate a strong password
def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI setup
st.set_page_config(page_title="Password Strength Meter", layout="centered")
st.title("🔐 Password Strength Meter")
st.subheader("🔑 Check Your Password Strength")
password = st.text_input("", type="password", placeholder="Enter your password here")

# Checking password strength
if password:
    strength, color, score, feedback = check_password_strength(password)
    st.markdown(f"<h5 style='color: {color};'>{strength}</h5>", unsafe_allow_html=True)
    st.progress(score / 4)

    if feedback:
        st.warning("🔹 Suggestions to Improve:")
        for tip in feedback:
            st.write(f"✔ {tip}")

st.markdown("---")
st.subheader("🔄 Generate a Strong Password")

if st.button("🛠 Generate Password"):
    strong_password = generate_strong_password()
    st.code(strong_password, language="plaintext")
