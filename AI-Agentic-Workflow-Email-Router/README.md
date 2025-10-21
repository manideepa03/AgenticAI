# 🧠 AI-Powered Agentic Workflow for Project Management  
**Pilot Project:** Email Router (InnovateNext Solutions)  

A Python-based, multi-agent workflow system that demonstrates how intelligent agents can collaborate to manage complex product development lifecycles.

---

## 🚀 Overview

This project demonstrates an **AI-powered agentic workflow** for managing product development.

**Highlights:**
- Multi-agent orchestration simulating **TPMs, Product Managers, and Engineers**  
- Converts high-level ideas into **user stories, product features, and engineering tasks**  
- Uses **Prompt Chaining, Routing, and Evaluation Loops**  

---

## 🧩 Project Structure
AI-Agentic-Workflow/
├── Phase1/ # Agent library + tests
├── Phase2/ # Workflow orchestration + product spec + outputs
├── .env # (Optional) OpenAI API key
├── requirements.txt
└── README.md


---

## 🧠 Phase 1: Agentic Toolkit

**Implemented Agents:**

- **DirectPromptAgent** – Handles simple LLM prompts  
- **AugmentedPromptAgent** – Adds context & formatting to prompts  
- **KnowledgeAugmentedPromptAgent** – Uses embedded domain knowledge  
- **RAGKnowledgePromptAgent** – Retrieval-augmented generation  
- **EvaluationAgent** – Validates outputs of other agents  
- **RoutingAgent** – Routes tasks to suitable agent teams  
- **ActionPlanningAgent** – Breaks high-level goals into sub-tasks  

✅ Each agent includes a **standalone test script** with outputs.

---

## ⚙️ Phase 2: Project Management Workflow

**Workflow Input:**
- High-level project prompt  
- Product specification file (`Product-Spec-Email-Router.txt`)

**Workflow Process:**
1. `ActionPlanningAgent` → Extracts actionable steps  
2. `RoutingAgent` → Assigns steps to agent teams:  
   - 🧩 Product Manager → User Stories  
   - ⚙️ Program Manager → Product Features  
   - 🧑‍💻 Development Engineer → Engineering Tasks  
3. Knowledge Agents generate outputs  
4. Evaluation Agents validate results  

**Output:**
- Complete, structured project plan with **validated stories, features, and tasks**  

---

## 🧩 Example Output

- `[Action Plan Step 1]` Generate user stories → 5 validated stories created  
- `[Action Plan Step 2]` Define product features → 3 high-level features generated  
- `[Action Plan Step 3]` Create engineering tasks → 12 tasks with dependencies  
- ✅ Final Output: Complete structured plan generated successfully  

---

## 🧠 Key Concepts Demonstrated

- Prompt Chaining & Routing  
- Multi-Agent Collaboration (TPM, PM, Engineer personas)  
- LLM Evaluation Loops  
- Modular, reusable agent design  
- Scalable project management  

---

## 🧩 Skills Gained

- Python for AI workflow design  
- Agentic system architecture  
- Multi-agent orchestration  
- OpenAI API integration  
- Prompt engineering & evaluation loops  
- Intelligent project planning & automation  

---

## 🏆 Acknowledgments

Part of the **Agentic Workflows Course** — showcasing the design of **dynamic AI systems** capable of reasoning, planning, and acting collaboratively.
