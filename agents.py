"""
THIS FILE: Definition of all 4 Agents
"""

from crewai import Agent
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# === GROQ CONFIGURATION ===
# IMPORTANT: .env file mein variable name GROQ_API_KEY hai (all caps)
groq_api_key = os.getenv("GROQ_API_KEY")  # ← .env se value read karega

if not groq_api_key:
    print("❌ ERROR: GROQ_API_KEY not found in .env file!")
    print("Please check your .env file has: GROQ_API_KEY=your_key_here")
    exit(1)

# Set environment variables for CrewAI (it uses OpenAI-compatible API)
os.environ["OPENAI_API_KEY"] = groq_api_key  # ← variable use kar rahe hain, direct string nahi
os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama-3.3-70b-versatile"

print("✅ GROQ_API_KEY loaded successfully!")

# Search tool (needs SERPER_API_KEY from .env)
search_tool = SerperDevTool()

# AGENT 1: LIBRARIAN
librarian_agent = Agent(
    role='Senior Research Librarian',
    goal='Find the most relevant {topic} research papers from academic sources',
    backstory="""You are an expert librarian who has been finding research papers for 10 years.
    You know how to find the best papers from Google Scholar, ArXiv, and academic databases.
    You only find relevant and high-quality papers.""",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

# AGENT 2: READER
reader_agent = Agent(
    role='Analytical Literature Reviewer',
    goal='Extract key insights from research papers and create structured summaries',
    backstory="""You are a meticulous researcher who reads every paper line by line.
    You identify methodology, findings, and limitations and organize them in table form.
    Your job is to make complex research simple.""",
    verbose=True,
    allow_delegation=False
)

# AGENT 3: STRATEGIST (Gap Finder)
strategist_agent = Agent(
    role='Research Gap Strategist',
    goal='Identify research gaps and unexplored areas in the literature',
    backstory="""You are a strategic thinker who sees patterns.
    You compare different papers and identify what is missing.
    Your job is to find opportunities where new research can happen.""",
    verbose=True,
    allow_delegation=False
)

# AGENT 4: WRITER
writer_agent = Agent(
    role='Academic Thesis Writer',
    goal='Write comprehensive literature review and thesis drafts',
    backstory="""You are a professional academic writer.
    You take data from all three agents and create a structured report.
    Your writing style is clear, professional, and publication-ready.""",
    verbose=True,
    allow_delegation=False
)

print("✅ All agents initialized successfully!")