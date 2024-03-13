# generative_model.py
import base64
import os
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def load_image_from_local(file_path):
    with open(file_path, "rb") as image_file:
        encoded_image_data = base64.b64encode(image_file.read()).decode("utf-8")

    mime_type = 'image/jpeg'
    return Part.from_data(data=base64.b64decode(encoded_image_data), mime_type=mime_type)

def generate_summary(image_data):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
    vertexai.init(project="", location="us-central1")

    image = Part.from_data(data=base64.b64decode(image_data), mime_type='image/jpeg')

    model = GenerativeModel("gemini-1.0-pro-vision-001")

    responses_content = ""
    responses = model.generate_content(
        [image, """Please look at the image above and write the information in Korean in the format below. In the incident summary section, please write based on factual information. (Please accurately describe the color and type of clothing in the clothing section. Please indicate only the top and bottom.)
gender:
clothes:
Incident summary:
Countermeasures: (1-2 of the following: 112, 119)
             
ex)
성별: 남자
인상 착의: 파란색 상의, 청바지
사건 개요: 편의점 과자진열대 옆쪽에서 한 남자가 심장쪽을 잡고 바닥에 쓰러져 있습니다.
대응 조치: 119
         """],
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.4,
            "top_p": 0.95,
            "top_k": 28
        },
        stream=True,
    )

    for response in responses:
        responses_content += response.text

    return responses_content
