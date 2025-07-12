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

from context import UserSessionContext
from guardrails import validate_goal_input, validate_output
from agent import create_health_agent

# ── bootstrap ────────────────────────────────────────────────────────────────
load_dotenv()
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(PROJECT_ROOT)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY missing – set it in your .env file")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

chat_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

set_default_openai_client(client=client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)

config = RunConfig(model=chat_model, model_provider=client, tracing_disabled=True)

# ── application loop ─────────────────────────────────────────────────────────
async def main() -> None:
    agent = create_health_agent(chat_model)

    # user context is stored in memory for this demo
    user_context = RunContextWrapper(
        UserSessionContext(
            name="User",
            uid=1,
            meal_plan=[],
        )
    )

    print("🟢 Type your question (or 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        if not validate_goal_input(user_input):
            print("🚫 Sorry, that didn't look like a goal – try again.")
            continue

        print("\nAssistant:")
        result = Runner.run_streamed(agent, input=user_input, context=user_context)

        async for event in result.stream_events():
            if event.type == "run_item_stream_event":
                if event.item.type == "tool_call_item":
                    print(f"[Tool ▶] {getattr(event.item, 'tool', 'unknown')}")
                elif event.item.type == "tool_call_output_item":
                    print(f"[Tool ✔] {event.item.output}")
                elif event.item.type == "message_output_item":
                    print(ItemHelpers.text_message_output(event.item))

        validate_output(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
