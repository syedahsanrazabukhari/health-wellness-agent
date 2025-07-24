import sys
import asyncio

async def stream_response(generator):
    async for chunk in generator:
        print(chunk, end="", flush=True)
        await asyncio.sleep(0.05)
    print()
    print("\n[Streaming] Response complete.")