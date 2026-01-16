from utils.llm import call_llm

def delivery_node(state):
    jokes = state["jokes"]

    prompt = f"""
Clean and polish these roast jokes.
Strict rules:
- Keep each joke ONE complete sentence
- Do NOT split sentences
- Make jokes tighter and funnier if needed
- English only
- Output as bullet points only

JOKES:
{jokes}
"""

    response = call_llm(prompt, temperature=0.8)

    # Remove prompt copy from response (just in case)
    # Agar model repeats the instructions accidentally
    lines = response.split("\n")
    cleaned_jokes = [line for line in lines if line.strip().startswith("*")]
    final_script = "\n".join(cleaned_jokes)

    return {"final_script": final_script}
