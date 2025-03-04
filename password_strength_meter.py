import streamlit as st
import re
import random
import string
import pyperclip

# Function to check password strength and provide suggestions
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Increase length to at least 8 characters.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔴 Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔴 Add at least one digit (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔴 Add a special character (!@#$%^&*).")

    # Strength Rating
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

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", layout="centered")

# Title
st.title("🔐 Password Strength Meter")

# Password Strength Checker
st.subheader("🔑 Check Your Password Strength")
password = st.text_input("", type="password", placeholder="Enter your password here")

if password:
    strength, color, score, feedback = check_password_strength(password)

    # Strength Message with Color
    st.markdown(f"<h5 style='color: {color};'>{strength}</h5>", unsafe_allow_html=True)

    # Progress Bar
    st.progress(score / 4)

    # Show Feedback for Weak Passwords
    if feedback:
        st.warning("🔹 Suggestions to Improve:")
        for tip in feedback:
            st.write(f"✔ {tip}")

# Divider for better layout
st.markdown("---")

# Password Generator Section
st.subheader("🔄 Generate a Strong Password")

if st.button("🛠 Generate Password"):
    strong_password = generate_strong_password()
    st.code(strong_password, language="plaintext")

    if st.button("📋 Copy to Clipboard"):
        pyperclip.copy(strong_password)
        st.success("✅ Copied Successfully!")

# Footer
st.markdown("---")
st.caption("🔒 Always use strong passwords to keep your accounts secure!")
