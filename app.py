
import streamlit as st
from PIL import Image
from gemma import analyze_disaster
from utils.image_analysis import prepare_image
from utils.report_generator import format_report

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="AeroGuard AI",
    page_icon="🚁",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("🚁 AeroGuard AI")
st.subheader("Offline Disaster Intelligence Powered by Google Gemma")

st.markdown("""
AeroGuard AI is an AI-powered disaster intelligence assistant designed to help
emergency responders quickly analyze disaster reports and images using
Google Gemma.

Supported disasters include:

- 🌊 Floods
- 🔥 Fires
- 🌪️ Storms
- 🏚️ Building Collapse
- ⛰️ Landslides
- 🚧 Road Blockages
""")

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("About AeroGuard AI")

st.sidebar.info("""
Powered by Google Gemma

Supports:

• Disaster Report Analysis
• Image Understanding
• Risk Assessment
• Emergency Recommendations
• Situation Reports

SDGs:
• SDG 11
• SDG 13
""")

# -----------------------------
# USER INPUTS
# -----------------------------
uploaded_image = st.file_uploader(
    "📷 Upload Disaster Image",
    type=["jpg", "jpeg", "png"]
)

report = st.text_area(
    "📝 Describe the Emergency",
    height=180,
    placeholder="""
Example:

Heavy flooding has affected a rural community after
three days of rainfall.

Roads are submerged.
Several houses are underwater.
People require evacuation.
"""
)

if uploaded_image:

    image = Image.open(uploaded_image)

    image = prepare_image(image)

    st.image(
        image,
        caption="Uploaded Disaster Image",
        use_container_width=True
    )

analyze_button = st.button(
    "🚨 Analyze Disaster"
)
# -----------------------------
# GEMMA ANALYSIS
# -----------------------------

if analyze_button:

    if not report.strip() and uploaded_image is None:

        st.warning("Please upload a disaster image or enter an emergency report.")

    else:

        prompt = f"""
You are AeroGuard AI, an expert disaster intelligence assistant.

Analyze the disaster information below.

Return a professional emergency response report using the following sections.

1. Disaster Type
2. Risk Level (Low, Medium, High, Critical)
3. Summary
4. Hazards Detected
5. Estimated Affected Area
6. People Potentially at Risk
7. Resources Required
8. Immediate Emergency Actions
9. Recommended Response Priority
10. Drone Observations
11. Additional Notes

Emergency Report:

{report}
"""

        with st.spinner("🧠 Gemma is analyzing the disaster..."):

            try:

                result = analyze_disaster(
                    prompt=prompt,
                    image=uploaded_image
                )

                final_report = format_report(result)

                st.success("✅ Analysis Complete")

                st.markdown("## 🚨 Emergency Response Report")

                st.markdown(final_report)

            except Exception as e:

                st.error("Analysis failed.")

                st.exception(e)
            
# -----------------------------
# FOOTER
# -----------------------------

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚁 AeroGuard AI")
    st.write(
        """
Offline Disaster Intelligence powered by Google Gemma.

Designed to support emergency responders with AI-assisted
decision making during floods, storms, fires, landslides,
and other disasters.
"""
    )

with col2:
    st.markdown("### 🌍 Supported SDGs")
    st.write("""
✅ SDG 11 — Sustainable Cities and Communities

✅ SDG 13 — Climate Action
""")

st.divider()

st.caption(
    "Built by Sultan Abdulkareem • Powered by Google Gemma • AeroGuard AI © 2026"
)

