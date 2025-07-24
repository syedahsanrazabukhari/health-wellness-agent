from agents import RunHooks

class CustomRunHooks(RunHooks):

    async def on_start(self, context_wrapper, agent):
        print(f"[Hook] Starting agent: {agent.name}")

    async def on_end(self, context_wrapper, agent, final_output):
        print(f"[Hook] Agent {agent.name} finished with output: {final_output}")

    async def on_agent_start(self, agent, context_wrapper):
        print(f"[Hook] Agent {agent.name} initiated.")

    async def on_agent_end(self, agent, context_wrapper, output):
        print(f"[Hook] Agent {agent.name} ended, output: {output}")

    async def on_tool_start(self, context_wrapper, agent, tool):
        print(f"[Hook] Tool {tool.name} started by {agent.name}")

    async def on_tool_end(self, context_wrapper, agent, tool, output):
        print(f"[Hook] Tool {tool.name} finished with output: {output}")

    async def on_handoff(self, context_wrapper, agent, source):
        print(f"[Hook] Handoff from {source.name} to {agent.name}")
