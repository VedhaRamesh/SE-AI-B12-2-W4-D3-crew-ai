# CrewAI Travel Planner

A simple CrewAI agent that recommends exactly three places to visit in a city,
with a short reason or practical tip for each.

## Requirements

- Python 3.10 or newer
- An OpenAI API key

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install crewai python-dotenv
```

Create a `.env` file in the project root with your OpenAI API key:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=openai/gpt-4o-mini
```

`OPENAI_MODEL` is optional; if omitted, the script uses `openai/gpt-4o-mini`.
Keep `.env` private and do not commit it to Git.

## Run

```bash
python travel_planner.py
```

When prompted, enter the city name. The planner prints three numbered
recommendations.
