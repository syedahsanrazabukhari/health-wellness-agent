from agents.guardrail import input_guardrail, GuardrailFunctionOutput
from agents import Agent, RunContextWrapper
from pydantic import BaseModel
from agents.run import Runner
from config import config, model

class HealthInputValidation(BaseModel):
    is_relevant: bool
    original_text: str
    reasoning: str
    verdict: str

input_validation_agent = Agent(
    name="Health Input Validation Agent",
    instructions=(
        "As a gatekeeper, determine if user input pertains to health, wellness, fitness, diet, exercise, injury, "
        "progress tracking, scheduling, or polite greetings. "
        "Reject inputs unrelated to these topics politely."
    ),
    output_type=HealthInputValidation,
    model=model
)

@input_guardrail
async def health_input_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    input_data: str | list[str]
) -> GuardrailFunctionOutput:
    try:
        result = await Runner.run(input_validation_agent, input_data, context=ctx.context, run_config=config)
        output_data = result.agent_output  # ✅ Extract this properly
        return GuardrailFunctionOutput(
            output_info=output_data,
            tripwire_triggered=not output_data.is_relevant
        )
    except Exception as e:
        print(f"[InputGuardrail] Validation failed: {e}")
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=True)
