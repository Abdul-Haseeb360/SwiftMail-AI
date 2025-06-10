# 📧 AI Email Generator

A professional email generation tool built with Streamlit and powered by Google's Gemini AI. This application helps busy professionals quickly create polished, well-written emails from simple instructions.

## ✨ Features

- **Quick Email Generation**: Transform brief instructions into professional emails
- **Customizable Tone**: Choose from multiple email tones:
  - Formal
  - Friendly
  - Apologetic
  - Persuasive
  - Grateful
- **Personalization**: Add recipient and sender names
- **User-Friendly Interface**: Clean and intuitive Streamlit-based UI

## 🚀 Coming Soon

- Email enhancement features
- More tone options
- Template management
- Email history
- Custom templates

## 🛠️ Setup

1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   streamlit run generator.py
   ```

## 📋 Requirements

- Python 3.7+
- Streamlit
- OpenAI (for the agents package)
- python-dotenv

## 🔧 Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details. 