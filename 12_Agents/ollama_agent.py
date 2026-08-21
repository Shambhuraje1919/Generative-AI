import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

model = OpenAIChatCompletionClient(
    model="tinyllama:latest",
    base_url="http://localhost:11434/v1",
    api_key="placeholder",
    model_info={
        "vision": False,
        "function_calling": False,
        "json_output": False,
        "family": "unknown",
        "structured_output": False,
    },
)

agent = AssistantAgent(
    name="Assistant",
    model_client=model,
)


async def main():
    res = await agent.run(
        task="Who is Narendra Modi?"
    )

    print(res)


if __name__ == "__main__":
    asyncio.run(main())