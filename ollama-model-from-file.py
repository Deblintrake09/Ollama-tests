import ollama

modelfile = """

SYSTEM you are a very knowledgeable but creative assistant on the scify and fantasy universes.
PARAMETER temperature=0.5
"""

ollama.create(model="knowitall",
              from_="llama3.2",
              system="you are a very knowledgeable but creative assistant on the scify and fantasy universes",
              parameters={"temperature": 0.5})

res = ollama.generate(model="knowitall", prompt="generate a short story where Battletech and Stargate universes collide")
print(res["response"])

#delete the model after use
ollama.delete("knowitall")