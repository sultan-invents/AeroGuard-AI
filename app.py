import streamlit as st

st.set_page_config(
    page_title="AeroGuard AI",
    page_icon="🚁",
    layout="wide"
)

st.title("🚁 AeroGuard AI")
st.subheader("Offline Disaster Intelligence Powered by Google DeepMind's Gemma 4")

st.write("""
Welcome to AeroGuard AI.

This prototype demonstrates how Gemma 4 can assist emergency responders
by analyzing disaster information and generating intelligent recommendations.
""")

uploaded_file = st.file_uploader(
    "Upload a disaster image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.success("Image uploaded successfully.")

st.text_area(
    "Describe the emergency situation",
    placeholder="Example: Flooding has affected several houses and roads..."
)

if st.button("Analyze with Gemma 4"):
    st.info("Gemma 4 integration will be completed during the live hackathon.")
