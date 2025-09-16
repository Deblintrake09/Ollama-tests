import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "Write a short story about a mech pilot stranded in an alien planet"
    }

response = requests.post(url, json=data, stream=True)


#check response status
if response.status_code == 200:
    print("Generated text:", end='', flush=True)
    #Iterate over the response lines
    for line in response.iter_lines():
        if line:
            #parse json data
            decoded_line = line.decode('utf-8')
            try:
                json_data = json.loads(decoded_line)
            #generate text
                generated_text = json_data.get("response", "")
                print(generated_text, end='', flush=True)
            except json.JSONDecodeError:
                print(f"Failed to decode JSON: {decoded_line}")
else:
    print(f"Request failed with status code: {response.status_code}")
