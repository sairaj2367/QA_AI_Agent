from flask import Flask, render_template, request, jsonify
from qa_bot import get_ai_response, team_members

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['question']
    prompt = f"As a QA AI assistant named Queeny, respond to: {user_input}"
    response = get_ai_response(prompt)

    # Check if we need to hand over to a team member
    for member, role in team_members.items():
        if member.lower() in response.lower():
            return jsonify({
                'response': f"{member} ({role}): {response}",
                'member': member
            })

    return jsonify({
        'response': f"Queeny: {response}",
        'member': 'Queeny'
    })


if __name__ == '__main__':
    app.run(debug=True)