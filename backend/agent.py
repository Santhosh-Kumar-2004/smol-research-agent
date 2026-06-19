from dotenv import load_dotenv

from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    InferenceClientModel
)

load_dotenv()

model = InferenceClientModel()

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model
)


def research(query: str):
    return agent.run(query)