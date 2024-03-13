import os
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

location = "us-central1"
project_id = ""
vertexai.init(project=project_id, location=location)

model = generative_models.GenerativeModel("gemini-pro")  # Use GenerativeModel class
response = model.generate_content('너 누구야?')

print(response.text)
