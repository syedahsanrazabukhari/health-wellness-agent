from agents import RunHooks


class CustomRunHooks(RunHooks):
    async def on_start(self, context_wrapper, agent):
        print(f"[Hooks] → run started for {agent.name}")

    async def on_end(self, context_wrapper, agent, final_output):
        print(f"[Hooks] → run ended for {agent.name} ➜ {final_output}")

    async def on_agent_start(self, agent, context_wrapper):
        print(f"[Hooks] agent {agent.name} entered")

    async def on_agent_end(self, agent, context_wrapper, output):
        print(f"[Hooks] agent {agent.name} finished: {output}")

    async def on_tool_start(self, context_wrapper, agent, tool):
        print(f"[Hooks] tool {tool.name} called")

    async def on_tool_end(self, context_wrapper, agent, tool, output):
        print(f"[Hooks] tool {tool.name} returned: {output}")

    async def on_handoff(self, context_wrapper, agent, source):
        print(f"[Hooks] hand‑off → {source.name} ⇢ {agent.name}")
    async def on_error(self, context_wrapper, agent, error):
        print(f"[Hooks] error in {agent.name}: {error}")
        # Optionally, you could re-raise the error if you want it to propagate
        # raise error