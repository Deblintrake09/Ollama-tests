import ollama

response = ollama.list()
#print(response)


response = ollama.chat(model="llama3.2", 
                       messages=[{"role": "user", "content": "list the top 5 battlemechs used by house Steiner"}],
                    )
print(response["message"]["content"])