import asyncio
from dotenv import load_dotenv
from agents import Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from agents.run import RunConfig
from context import UserSessionContext
from agent import create_health_agent
import os

load_dotenv()
set_tracing_disabled(True)

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY missing from environment.")

client = AsyncOpenAI(api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)
config = RunConfig(model=model, model_provider=client)

async def main_loop():
    user_context = UserSessionContext(name="user", uid=1234)
    print("🌿 Health & Wellness AI Agent — Type 'exit' to quit.\n")

    while True:
        user_input = input("👤 You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        user_context.messages.append({"role": "user", "content": user_input})
        health_agent = create_health_agent(model)

        try:
            run_result = await Runner.run(
                health_agent,                # ✅ Agent passed as positional argument
                input=user_input,
                context=user_context,
                run_config=config,
            )

            print(f"🧠 AI: {run_result.final_output}")
            user_context.messages.append({"role": "assistant", "content": run_result.final_output})

        except Exception as ex:
            if "InputGuardrailTripwireTriggered" in str(ex):
                warning_msg = (
                    "⚠️ Your input doesn't seem related to health, fitness, nutrition, or wellness topics. "
                    "Please ask relevant questions, e.g., 'I want to lose 5kg in 2 months'."
                )
                print(warning_msg)
            else:
                print(f"❌ Unexpected error: {ex}")

if __name__ == "__main__":
    asyncio.run(main_loop())
