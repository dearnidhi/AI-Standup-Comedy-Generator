from utils.llm import call_llm

def roast_controller_node(state):
    jokes = state["jokes"]
    level = state["level"]

    prompt = f"""
Adjust these jokes to roast level: {level}

Levels:
light = friendly
medium = standup
savage = harsh but clean

Jokes:
{jokes}
"""

    controlled = call_llm(prompt, temperature=0.8)
    return {"controlled_jokes": controlled}
