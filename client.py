from google import generativeai as genai

genai.configure(api_key="AIzaSyCeAMs6SOBlrrp44vPU4fq5j8IMRbWoG5I")

def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if prompt=="":
        print("Say That Again Please...")

    response = model.generate_content(prompt)

    if response.text:
        return response.text
    else:
        return "Sorry, no response from Gemini."
    
def ask_gemini_with_image(prompt, image_path):
    model = genai.GenerativeModel('models/gemini-1.5-flash')

    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

    response = model.generate_content([
        {"text": prompt},
        {"inline_data": {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }}
        ]
    )
    return response.text
