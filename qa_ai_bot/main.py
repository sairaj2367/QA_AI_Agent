from speech_handler import speak, listen
from ai_handler import get_ai_response
from bot_config import TEAM_MEMBERS


def main():
    speak("Hello, I'm Queeny, your QA AI agent. How can I help you today?")

    website_url = None

    while True:
        user_input = listen()

        if "exit" in user_input.lower():
            speak("Thank you for using our QA AI service. Goodbye!")
            break

        if website_url is None and ("http://" in user_input or "https://" in user_input):
            website_url = user_input
            speak(
                f"Thank you for providing the website URL: {website_url}. I'll keep this in mind for our discussion. What would you like to know about our QA services for this site?")
            continue

        if website_url:
            prompt = f"Consider the website {website_url}. As a QA AI agent named Queeny, respond to: {user_input}"
        else:
            prompt = f"As a QA AI agent named Queeny, respond to: {user_input}"

        response = get_ai_response(prompt)

        # Check if we need to hand over to a team member
        for member, role in TEAM_MEMBERS.items():
            if member.lower() in response.lower():
                speak(f"I'll hand over to {member}, our {role}, for this question.")
                speak(response, member)
                break
        else:
            speak(response)


if __name__ == "__main__":
    main()