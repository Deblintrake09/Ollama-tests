import ollama
import os

model = "llama3.2"

inputpath= "./data/groceries.txt"
outputpath = "./data/groceries-organized.txt"
# Check if input file exists
if not os.path.exists(inputpath):
    print(f"Input file {inputpath} does not exist")
    exit(1) 

# Read the input file
with open(inputpath, "r") as f:
    items = f.read().strip()

#prepare the prompt
prompt = f"""
You are an assistant that categorizes and sorts grocery items.

Here's a list of items:
{items}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, Snacks, Household Items, etc.
2. Sort items within each category alphabetically
3. Present the output in a clear format with categories as headings and items listed under each category using bullet points.
"""


#send the prompt to ollama and get the response
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print("generated_text:", generated_text)
    
    # Write the organized list to the output file
    with open(outputpath, "w") as f:
        f.write(generated_text.strip())
    print(f"Organized grocery list written to {outputpath}")
except Exception as e:
    print(f"Error during generation: {e}")
