from utils.llm import call_llm 
def joke_writer_node(state): 
    name = state["name"] 
    traits = state["traits"] 
    roast_level = state.get("roast_level", "medium")
    prompt = f"""
You are a professional Indian stand-up comedy writer.

Task:
Write 5 roast jokes about a person.

Person Name: {name}
Person Traits: {traits}
Roast Level: {roast_level}

STRICT RULES (VERY IMPORTANT):
- Write in ENGLISH only
- Each joke must be ONE complete sentence
- Do NOT break sentences or cut lines
- No stage directions
- No audience reactions
- No narration or explanations
- No broken Hindi or forced Hinglish
- Indian references are okay
- Punchline must naturally land at the END of the sentence
- Meme-worthy, sharp, savage but clean
- No abuse, no slurs

OUTPUT FORMAT:
- Bullet points
- Only jokes, nothing else
"""

    jokes = call_llm(prompt, temperature=0.85)
    return {"jokes": jokes}
