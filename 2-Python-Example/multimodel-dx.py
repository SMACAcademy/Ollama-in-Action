from ollama import chat

# from pathlib import Path

# Pass in the path to the image
# conda env list
# conda activate langchain_py311
# python .\2-Python-Example\multimodel-dx.py
# .\2-Python-Example\doc_dx.jpg
# .\2-Python-Example\dx_1.jpg
path = input('Please enter the path to the image: ')

# You can also pass in base64 encoded image data
# img = base64.b64encode(Path(path).read_bytes()).decode()
# or the raw bytes
# img = Path(path).read_bytes()

response = chat(
  model='llama3.2-vision',
  messages=[
    {
      'role': 'user',
      #'content': 'What is your inference from this prescription? Provide the patient name, age, gender and the list of tablets and dosages. What could be the possible diagnostics?',
      'content': 'Extract and summarize all information from the medical prescription image. Details should include: - Patient Details: Name, age, gender, and address. - Medications: List all drugs prescribed, including names, dosages, forms (e.g., tablet, syrup), and quantities. - Prescriber Information: Doctor\'s name, qualifications, registration number, and contact details. - Dosage Instructions: Provide dosage instructions for each medication, including frequency, timing relative to meals, and any other specific directions. - Treatment Duration: Duration for each prescribed medication and any relevant dates. - Refill Information: Details on refills, including the number of refills allowed and related conditions. - Special Instructions: Any special handling or warnings associated with the medications, such as storage conditions or precautions. - Insurance Details: Information related to insurance coverage, including provider name, policy number, and billing instructions.',
      'images': [path],
    }
  ],
)

print(response.message.content)