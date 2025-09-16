import ollama

## Gemerata a response with Generate Function

response = ollama.generate(model="llama3.2",
                            prompt="list what is the armamament of an Atlas-II battlemech",)

# show what it info is available on the model used to generate the response
print(ollama.show("llama3.2"))

# print the actual generated response
print(response["response"])
