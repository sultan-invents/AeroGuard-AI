
import streamlit as st
from PIL import Image
from gemma import analyze_disaster


st.set_page_config(
    page_title="AeroGuard AI",
    page_icon="🚁",
    layout="wide"
)


st.title("🚁 AeroGuard AI")
st.subheader("Offline Disaster Intelligence Powered by Gemma")

st.write(
"""
AI emergency response assistant that analyzes disaster images
and reports to generate rapid response intelligence.
"""
)

st.divider()


image_file = st.file_uploader(
    "📷 Upload Disaster Image",
    type=["png", "jpg", "jpeg"]
)


report = st.text_area(
    "📝 Emergency Report",
    placeholder="Example: Heavy flooding affected a rural community after 3 days of rain..."
)


if image_file:

    image = Image.open(image_file)

    st.image(
        image,
        caption="Uploaded Disaster Image",
        use_container_width=True
    )


if st.button("🚨 Analyze with Gemma"):

    if not report and not image_file:
        st.warning(
            "Please upload an image or enter a disaster report."
        )

    else:

        prompt = f"""
You are AeroGuard AI, a disaster intelligence system.

Analyze this emergency situation.

Return a structured report:

1. Disaster Type
2. Risk Level (Low/Medium/High/Critical)
3. Visible Hazards
4. Estimated Affected Area
5. People at Risk
6. Emergency Resources Needed
7. Immediate Actions
8. Drone Observations

Emergency Report:

{report}
"""


        with st.spinner("Gemma is analyzing..."):

            result = analyze_disaster(
                prompt,
                image_file
            )

        st.success("Analysis Complete")

        st.header("🚨 Emergency Response Report")

        st.write(result)


st.divider()

st.caption(
"AeroGuard AI | Gemma-powered disaster intelligence for SDG 11 and SDG 13"
)
