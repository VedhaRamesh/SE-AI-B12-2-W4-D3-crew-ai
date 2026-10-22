import os

from crewai import Agent, Crew, Task
from dotenv import load_dotenv


def main():
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY in the .env file before running.")

    city = input("Which city? ").strip()
    if not city:
        raise ValueError("City cannot be empty.")

    planner = Agent(
        role="Travel Planner",
        goal="Recommend memorable, practical places to visit in the requested city.",
        backstory=(
            "You are an experienced local tour guide and travel curator who knows "
            "how to turn a short trip into a memorable experience."
        ),
        verbose=True,
        llm=os.getenv("OPENAI_MODEL", "openai/gpt-4o-mini"),
    )

    recommendations = Task(
        description=(
            "Recommend exactly 3 places to visit in {city}. Choose notable, "
            "distinct attractions and include a concise reason or practical tip "
            "for each. Do not include an introduction or conclusion."
        ),
        expected_output=(
            "Exactly three concise, punchy numbered bullet points, one place per "
            "line, formatted as '1. Place - brief reason or tip'. No other text."
        ),
        agent=planner,
    )

    crew = Crew(
        agents=[planner],
        tasks=[recommendations],
        verbose=True,
    )
    result = crew.kickoff(inputs={"city": city})
    print(result)


if __name__ == "__main__":
    main()
