import google.generativeai as genai
import os



GOOGLE_API_KEY = "*************************"
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

print("Models that support generateContent:\n")
for m in genai.list_models():
    methods = getattr(m, "supported_generation_methods", [])
    if "generateContent" in methods:
        print(m.name, "->", methods)
