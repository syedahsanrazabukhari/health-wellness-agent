from agents.guardrail import output_guardrail, GuardrailFunctionOutput
from agents import Agent, RunContextWrapper
from pydantic import BaseModel
from agents.run import Runner
from config import config, model

class OutputSafetyCheck(BaseModel):
    is_safe: bool
    original_response: str
    feedback: str

output_validation_agent = Agent(
    name="Health Output Validation Agent",
    instructions=(
        "Analyze the assistant's response for safety, relevance, and appropriateness. "
        "Responses should relate only to health, fitness, nutrition, injury care, scheduling, or wellness. "
        "Reject unsafe, off-topic, or harmful replies. Polite greetings are allowed."
    ),
    output_type=OutputSafetyCheck,
    model=model
)

@output_guardrail
async def health_output_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    output_text: str
) -> GuardrailFunctionOutput:
    try:
        result = await Runner.run(output_validation_agent, output_text, context=ctx.context, run_config=config)
        output_data = result.final_output  # Use final_output for the model output

        return GuardrailFunctionOutput(
            output_info=output_data,
            tripwire_triggered=not output_data.is_safe
        )
    except Exception as e:
        print(f"[OutputGuardrail] Validation failed: {e}")
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=True)
