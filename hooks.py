from agents import RunHooks

class CustomRunHooks(RunHooks):
    async def on_start(self, context, agent):
        print(f"[Start] {agent.name} initiated")

    async def on_end(self, context, agent, final_result):
        print(f"[End] {agent.name} completed with result: {final_result}")

    async def on_agent_start(self, agent, context):
        print(f"[Agent Start] {agent.name}")

    async def on_agent_end(self, agent, context, result):
        print(f"[Agent End] {agent.name}: {result}")

    async def on_tool_start(self, context, agent, tool):
        print(f"[Tool Start] {tool.name}")

    async def on_tool_end(self, context, agent, tool, output):
        print(f"[Tool End] {tool.name}: {output}")

    async def on_handoff(self, context, agent, origin):
        print(f"[Handoff] {origin.name} ➝ {agent.name}")