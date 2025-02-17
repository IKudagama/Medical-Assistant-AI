import streamlit as st
from pathlib import Path
import google.generativeai as genai

from api_key import api_key

#configure genai with api key

genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

#apply safty settings
safety_settings = [
{
"category": "HARM_CATEGORY_HARASSMENT",
"threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
{
"category": "HARM_CATEGORY_HATE_SPEECH",
"threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
{
"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
"threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
{
"category": "HARM_CATEGORY_DANGEROUS_CONTENT",
"threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
]

system_prompt="""

As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your
expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.

Your Responsibilities include:

1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.

Important Notes:

1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the
provided image.'
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions."

4. Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above

"""

model = genai.GenerativeModel(
  model_name="gemini-1.5-Flash",
  generation_config=generation_config,
)


st.set_page_config(page_title="Vital Image Analytics", page_icon="logo.jpg")

st.image("logo.jpg", width=200)

st.title("Vital Image Analytics")

st.subheader("An Application that can help users to identify medical images")

uploaded_file = st.file_uploader("Upload the medical image for analysis",type=["png","jpg","jpeg"])


submit_button = st.button("Generate the Analysis")

if submit_button:
    image_data = uploaded_file.getvalue()

    