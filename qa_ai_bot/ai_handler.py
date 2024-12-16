import openai
from bot_config import OPENAI_API_KEY
from instruction_set import get_instruction_set
from reference_handler import get_all_references
from learning_handler import save_learning, get_recent_learnings

openai.api_key = OPENAI_API_KEY


def get_ai_response(prompt):
    instruction_set = get_instruction_set()
    reference_data = get_all_references()
    recent_learnings = get_recent_learnings()

    learnings_text = "\n".join([f"Q: {l['query']}\nA: {l['response']}" for l in recent_learnings])

    full_prompt = f"{instruction_set}\n\nReference Data:\n{reference_data}\n\nRecent Learnings:\n{learnings_text}\n\nUser query: {prompt}\n\nQueeny's response:"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=full_prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    ai_response = response.choices[0].text.strip()
    save_learning(prompt, ai_response)

    return ai_response