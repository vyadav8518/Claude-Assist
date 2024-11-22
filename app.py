from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, jsonify
import anthropic

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Store conversation history
conversation_history = []

def get_claude_response(message):
    try:
        # Create messages for the conversation
        messages = [
            {
                "role": "user",
                "content": message
            }
        ]
        
        # If there's conversation history, include it
        if conversation_history:
            messages = conversation_history + messages
        
        # Get response from Claude
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=messages
        )
        
        # Extract the response content
        assistant_message = response.content[0].text
        
        # Update conversation history
        conversation_history.extend([
            {"role": "user", "content": message},
            {"role": "assistant", "content": assistant_message}
        ])
        
        # Keep only the last 10 messages to manage context length
        if len(conversation_history) > 10:
            conversation_history.pop(0)
            
        return assistant_message
        
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'})
    
    response = get_claude_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)