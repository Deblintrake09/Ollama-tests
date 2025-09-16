import ollama

response = ollama.list()

response = ollama.chat(model="llama3.2", 
                       messages=[{"role": "user", 
                                  "content": "What caused the fall of the Roman Empire? Compare it to the fall of the First Star League (from Battletech)"}
                                 ],
                                 stream=True,
                    )

for chunk in response:
    print(chunk["message"]["content"], end='', flush=True)