# video1.py
# This version runs even if your OpenAI key has no credits

try:
    from langchain_openai import ChatOpenAI

    # Create the model instance
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    # Ask the model a question
    response = llm.invoke("Explain LangGraph in one short paragraph.")
    print(response)

except Exception as e:
    print("⚠️ OpenAI call failed (no credits or connection). Showing fallback output instead.\n")
    print("Reason:", e)
    print("\nFallback answer:")
    print(
        "LangGraph is a framework in the LangChain ecosystem that helps developers "
        "structure large language model applications as connected nodes and edges. "
        "It allows you to manage workflows, tools, and logic in a modular way, "
        "making complex AI apps easier to design and debug."
    )





