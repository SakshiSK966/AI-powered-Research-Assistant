import os
import streamlit as st
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional, Any
from transformers import pipeline


os.environ["TAVILY_API_KEY"] = "Paste your TAVILY API KEY here"  
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "Paste your HUGGINGFACEHUB API TOKEN HERE"  

search_tool = TavilySearchResults(k=5)  
generator = pipeline("text-generation", model="t5-small") 


class ResearchState(TypedDict, total=False):
    query: str
    research_results: Optional[Any]
    final_answer: Optional[str]

# Agent 1: Perform research
def run_research_agent(state: ResearchState) -> ResearchState:
    query = state.get("query")
    if not query:
        raise ValueError("No query provided in the initial state.")
    
    try:
        print(f"\n[Research Agent] Searching for: {query}")
        results = search_tool.run(query)
        print(f"[Research Agent] Results:\n{results[:500]}...\n")
    except Exception as e:
        # Catch any exception and handle it
        print(f"[ERROR] Failed to retrieve results: {e}")
        results = ["Sorry, no results could be fetched. Please try again later."]
    
    return {"query": query, "research_results": results}

# Agent 2: Generate an answer from the research results
def run_answer_agent(state: ResearchState) -> ResearchState:
    results = state.get("research_results")
    query = state.get("query")
    
    if not results:
        raise ValueError("No research results to draft from.")
    
    
    research_content = ""
    for result in results:
        title = result.get("title", "No title")
        url = result.get("url", "No URL")
        content = result.get("content", "No content available.")
        
       
        research_content += f"Title: {title}\nURL: {url}\nContent: {content}\n\n"
    
    prompt = f"Based on the query: '{query}', draft a detailed informative answer using this information:\n\n{research_content}"
    print("[Answer Agent] Drafting answer...")
    
    
    response = generator(prompt, max_length=500)[0]["generated_text"]
    
    return {"query": query, "final_answer": response}

#  Build the LangGraph
graph = StateGraph(ResearchState)
graph.add_node("research", run_research_agent)
graph.add_node("draft", run_answer_agent)
graph.set_entry_point("research")
graph.add_edge("research", "draft")
graph.add_edge("draft", END)
app = graph.compile()

# Streamlit Frontend
def main():
   
    st.set_page_config(page_title="AI Research Assistant", page_icon="🧠", layout="wide")

    
    st.title("AI-Powered Research Assistant")
    st.markdown("""
    Welcome to the **AI Research Assistant**, an intelligent system that helps you gather research and generate informative answers based on your query.
    Just type in your question and click **Get Answer** to see the magic!
    """)
    
    st.subheader("Enter your research query:")
    query = st.text_input("Your Query", placeholder="E.g. 'Scope of AI in education'", key="query_input", label_visibility="collapsed")

    col1, col2 = st.columns([2, 1])
    
    with col1:
      
        if st.button("Get Answer", key="generate_button"):
            if query:
                with st.spinner("Fetching results and generating answer..."):
                    
                    result = app.invoke({"query": query})
                    st.subheader("✅ Final Answer:")
                    st.write(result["final_answer"])
            else:
                st.error("Please enter a valid query.")
    
    with col2:
        
        st.markdown("### About the Research")
        st.markdown("""
        This tool is powered by AI technologies such as **LangChain**, **Tavily**, and **Hugging Face** models.
        It's designed to assist you in quickly gathering research content and generating structured answers for any research topic.
        """)

    st.markdown("---")
    st.markdown("Powered by [LangChain](https://www.langchain.com) & [Hugging Face](https://huggingface.co)")

if __name__ == "__main__":
    main()
