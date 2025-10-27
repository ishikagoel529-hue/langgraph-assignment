# LangGraph Assignment – Module 2  
### Course: [Introduction to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph)  
**Student:** Ishika Goel  
**Repository:** [https://github.com/ishikagoel529-hue/langgraph-assignment](https://github.com/ishikagoel529-hue/langgraph-assignment)

---

## 🎥 Video 1 – State Schema
**What I learned:** How to use LangChain’s `ChatOpenAI` class and test it with LangGraph.  
**What I changed:** Added a fallback system so the code still runs without an active API key.

---

## 🎥 Video 2 – State Reducers
**What I learned:** How to modify prompts and run multiple calls in LangGraph.  
**What I changed:** Adjusted the prompt to request bullet points instead of a paragraph.

---

## 🎥 Video 3 – Multiple Schemas
**What I learned:** How to define and work with multiple state schemas within LangGraph.  
**What I changed:** Created a new script (`video3.py`) that summarizes the idea of multiple schemas in two lines.

---

## 🎥 Video 4 – Trim and Filter Messages
**What I learned:** How LangGraph trims and filters message history to improve memory efficiency.  
**What I changed:** Added an example (`video4.py`) demonstrating trimming and filtering messages in a chatbot.

---

## 🎥 Video 5 – Chatbot with Summarizing Messages and Memory
**What I learned:** How summarizing messages helps a chatbot maintain context across long conversations.  
**What I changed:** Modified the code in `video5.py` to show how summarization works in LangGraph chat memory.

---

## 🎥 Video 6 – Chatbot with Summarizing Messages and External Memory
**What I learned:** How to integrate external memory systems into LangGraph chatbots for persistent context.  
**What I changed:** Added a final script (`video6.py`) demonstrating external memory management and summarization.

---

✅ Each video corresponds to one commit.  
✅ All lessons are summarized with small code changes and explanations.  
✅ Repository follows the video-by-video structure required for Module 2.

---

# LangGraph Assignment — Module 3

**Course:** [Intro to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph)  
**Student:** Ishika Goel  
**Repository:** [https://github.com/ishikagoel529-hue/langgraph-assignment](https://github.com/ishikagoel529-hue/langgraph-assignment)

---

### Lesson 1: Streaming
**What I learned:** How to stream LLM outputs from a LangGraph node and observe events as they arrive.  
**My tweak:** Changed the prompt to generate a short motivational study tip; added `.env` loading so the key isn’t hard-coded.  
**How I ran it:**  
`python module3/lesson1_streaming.py` (from repo root)  
**Files:**  
- `module3/lesson1_streaming.py`
### Lesson 2: Breakpoints
**What I learned:** How to pause the graph for human review and then resume to finalize the answer (human-in-the-loop).  
**My tweak:** If the draft isn’t approved, I auto-revise it once with the LLM before finalizing.  
**How I ran it:** `python module3/lesson2_breakpoints.py`  
**Files:** `module3/lesson2_breakpoints.py`

### Lesson 3: Editing State & Human Feedback
**What I learned:** How to capture human feedback and modify the graph **state** mid-run (draft → human edits → apply edits → final).  
**My tweak:** If the user gives no edits, I short-circuit and accept the draft; otherwise I re-prompt the LLM to apply the exact edits into a concise final.  
**How I ran it:** `python module3/lesson3_edit_state.py`  
**Files:** `module3/lesson3_edit_state.py`
### Lesson 4: Dynamic Breakpoints
**What I learned:** How to pause only when the output fails a quality check by routing with `add_conditional_edges` (dynamic breakpoint pattern).  
**My tweak:** I trigger review if the answer is >25 words or contains “error”, then let the user choose Approve/Shorten/Rewrite; after review I re-check before finalizing.  
**How I ran it:** `python module3/lesson4_dynamic_breakpoints.py`  
**Files:** `module3/lesson4_dynamic_breakpoints.py`
