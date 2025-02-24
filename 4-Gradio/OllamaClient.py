import requests
import json  # Add this import

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url

    def query(self, prompt, model="llama3.2:latest", temperature=0.1):
        endpoint = f"{self.base_url}/models/{model}/completions"
        headers = {"Content-Type": "application/json"}
        data = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": temperature
        }
        response = requests.post(endpoint, json=data, headers=headers)
        print("Response Status Code:", response.status_code)  # Check the HTTP status code
        print("Raw Response Text:", response.text)  # This will show you the full server response

        try:
            parsed_response = response.json()
            return parsed_response['choices'][0]['text']
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
            return "An error occurred: Unable to decode JSON."
        except KeyError as e:
            print("Key Error:", e)
            return "An error occurred: Key missing in the response."
