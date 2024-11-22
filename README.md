# Claude-Assist 🤖

Claude-Assist is an intelligent chatbot web application powered by Anthropic's Claude AI. It provides a seamless conversational interface that leverages Claude's advanced language capabilities to deliver helpful, informative responses.

## Features ✨

- Real-time chat interface with Claude AI
- Conversation history management
- Responsive web design
- Secure API key handling
- Easy-to-use interface
- Support for markdown formatting in responses

## Technology Stack 🛠️

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: Claude 3 Opus (Anthropic)
- **API**: Anthropic Messages API
- **Dependencies**: anthropic, flask, python-dotenv

## Getting Started 🚀

### Prerequisites

- Python 3.8 or higher
- Anthropic API key ([Get one here](https://console.anthropic.com/))
- pip (Python package installer)

### Installation

1. Clone the repository
```bash
git clone https://github.com/vyadav8518/Claude-Assist.git
cd Claude-Assist
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables 
Create a `.env` file in the root directory and add your Claude API key:
```env
ANTHROPIC_API_KEY="your_api_key_here"
```


4. Run the application
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure 📁

```
Claude-Assist/
├── app.py                 # Main application file
├── .env                   # Environment variables (not in repo)
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore file
├── requirements.txt      # Project dependencies
└── templates/
    └── index.html        # Frontend template
```

## Usage 💡

1. Start the application
2. Type your message in the input field
3. Press Enter or click Send
4. Receive AI-generated responses from Claude

## Security 🔒

- API keys are stored securely in environment variables
- .env file is excluded from version control
- Sensitive data is never exposed to the frontend

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments 🙏

- Powered by [Anthropic's Claude AI](https://www.anthropic.com/)
- Built with [Flask](https://flask.palletsprojects.com/)
- Inspired by the need for intelligent conversational interfaces

## Contact 📬

Name - Vicky Kumar

Project Link: https://github.com/yourusername/Claude-Assist