import os
from langchain_community.tools import TavilySearchResults
os.environ["TAVILY_API_KEY"] = "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"
tool = TavilySearchResults()
docs = tool.invoke({"query": "What is the approach taken in the Alpha podium paper?"})