from phi.agent import Agent

from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
##setx OPENAI_API_KEY with key in command prompt

openai.api_key=os.getenv("OPENAI_API_KEY")

##web agent
web_search_agent = Agent(
    name="Web Agent",
    #model=OpenAIChat(id="gpt-4o"),
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
#web_search_agent.print_response("Whats happening in France?", stream=True)

##finance agent
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
#finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)

### multi ai agent

multi_ai_agent_team = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent_team.print_response("Summarize analyst recommendations for NVDA", stream=True)
