import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import sys
import asyncio
from dotenv import load_dotenv

from agents import (
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    ItemHelpers,
    set_default_openai_client,
    set_default_openai_api,
    set_tracing_disabled,
    RunContextWrapper,
)
from agents.run import RunConfig

from context import SessionContext
from guardrails import is_valid_goal_input, ensure_valid_output
from agent import build_health_wellness_agent

sys.path.append(os.path.dirname(__file__))
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise EnvironmentError("GEMINI_API_KEY is missing in .env")

openai_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model_instance = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=openai_client,
)

set_default_openai_client(client=openai_client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(disabled=True)

async def main():
    wellness_agent = build_health_wellness_agent(model_instance)

    user_ctx = RunContextWrapper(SessionContext(
        user_name="User",
        user_id=1,
        target_goal=None,
        diet_choices=None,
        exercise_plan=None,
        meal_suggestions=[],
        injury_details=None,
        handoff_history=[],
        progress_updates=[]
    ))

    print("\n✅ Health & Wellness Agent Ready! Type your goals:\n")

    while True:
        question = input("\nYour Input (or type 'exit'): ")
        if question.lower() == "exit":
            break

        if not is_valid_goal_input(question):
            print("\n⚠️ Invalid format. Try like: 'lose 5kg in 2 months'")
            continue

        print("\n💬 Assistant:")

        runner = Runner.run_streamed(wellness_agent, input=question, context=user_ctx)

        async for event in runner.stream_events():
            if event.type == "run_item_stream_event":
                if event.item.type == "tool_call_item":
                    print(f"[Tool Called] {getattr(event.item, 'tool', 'Unknown')}")
                elif event.item.type == "tool_call_output_item":
                    print(f"[Tool Output] {event.item.output}")
                elif event.item.type == "message_output_item":
                    print(ItemHelpers.text_message_output(event.item))

        output = runner.final_output
        if not ensure_valid_output(output):
            print("⚠️ Output validation failed.")

if __name__ == "__main__":
    asyncio.run(main())