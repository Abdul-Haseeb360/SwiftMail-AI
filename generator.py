#  imports
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner
import streamlit as st
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError(
        "DEEPSEEK_API_KEY is not set. Please ensure it is defined in your .env file")

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


EmailAgent = Agent(
    name="Email Generator",
    instructions="You help write polished, professional emails from short instructions. Make sure the tone matches user input."
)


async def generate_email(prompt):
    try:
        response = await Runner.run(
            EmailAgent,
            input=prompt,
            run_config=config
        )
        return response.final_output
    except Exception as e:
        return f"❌ Error: {e}"

# Streamlit UI
st.set_page_config(page_title="AI Email Generator", page_icon="📧")
st.title("📧 SwiftMail AI – Professional Emails in Seconds")

user_prompt = st.text_area(
    "✏️ What's your message? (e.g. reschedule meeting to Friday 3pm)", height=100)

tone = st.selectbox(
    "🎯 Choose the tone of your email:",
    ["Formal", "Friendly", "Apologetic", "Persuasive", "Grateful"]
)

to_name = st.text_input("👤 Recipient Name (To)")
from_name = st.text_input("🧑‍💼 Your Name (From)")

if st.button("Generate Email"):
    if not user_prompt.strip():
        st.warning("Please write a message first.")
    else:
        with st.spinner("Generating your email..."):
            full_prompt = f"Write an email in a {tone.lower()} tone based on this instruction:\n\n{user_prompt}"
            output = asyncio.run(generate_email(full_prompt))

            output = output.replace(
                "[Recipient Name]", to_name if to_name else "Recipient")
            output = output.replace(
                "[Name]", to_name if to_name else "Recipient")
            output = output.replace(
                "[Your Name]", from_name if from_name else "Your Name")
            output = output.replace("[Your Title]", "")

            st.subheader("✅ Your Email:")
            st.success(output)
