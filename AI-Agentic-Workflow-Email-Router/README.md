# Starter Code

This folder contains the starter code for the project. The project has been divided into two parts - phase 1 and phase 2. The same has been done with the starter code. Remember to move the files from phase 1 to phase 2 as required. 

🧠 AI-Powered Agentic Workflow for Project Management

Pilot Project: Email Router (InnovateNext Solutions)

A Python-based, multi-agent workflow system that demonstrates how intelligent agents can collaborate to manage complex product development lifecycles.

🚀 Overview

This project showcases the design and implementation of an AI-powered agentic workflow for product and project management.

Built in two phases, the system combines Prompt Chaining, Routing, and Agent Collaboration patterns to simulate a team of AI agents working together—just like real-world technical project managers, product managers, and engineers.

The pilot workflow uses the "Email Router" product specification to demonstrate how the system converts a high-level idea into structured user stories, product features, and engineering tasks.

🧩 Project Structure
AI-Agentic-Workflow/
│
├── Phase1/
│   ├── workflow_agents/
│   │   └── base_agents.py          # Core reusable agent library
│   ├── tests/
│   │   ├── test_direct_prompt_agent.py
│   │   ├── test_augmented_prompt_agent.py
│   │   ├── test_knowledge_agent.py
│   │   ├── test_evaluation_agent.py
│   │   ├── test_routing_agent.py
│   │   ├── test_action_planning_agent.py
│   │   └── ...
│   └── outputs/
│       └── agent_test_results.txt  # Logs or screenshots of successful test runs
│
├── Phase2/
│   ├── agentic_workflow.py         # Main workflow orchestration script
│   ├── Product-Spec-Email-Router.txt
│   └── outputs/
│       └── workflow_output.txt     # Final structured output for Email Router project
│
├── .env                            # (Optional) OpenAI API key file
├── requirements.txt
└── README.md

🧠 Phase 1: Agentic Toolkit

In this phase, a modular AI agent library was developed under workflow_agents/.

Implemented Agents
Agent Class	Description
DirectPromptAgent	Handles simple LLM prompts with minimal augmentation.
AugmentedPromptAgent	Enriches prompts with contextual data or formatting.
KnowledgeAugmentedPromptAgent	Uses embedded domain knowledge to reason over product specs.
RAGKnowledgePromptAgent	(Provided) Demonstrates retrieval-augmented generation.
EvaluationAgent	Validates the output of other agents against structured criteria.
RoutingAgent	Dynamically routes tasks to the most suitable agent team.
ActionPlanningAgent	Breaks high-level goals into executable sub-tasks.

Each agent includes a standalone test script verifying its functionality.

⚙️ Phase 2: Project Management Workflow

The agentic_workflow.py script demonstrates how these agents collaborate to complete a real-world project management process.

Workflow Overview

Input:

A high-level project prompt

Product specification file (Product-Spec-Email-Router.txt)

Process:

ActionPlanningAgent extracts actionable steps.

RoutingAgent assigns each step to specialized agent teams:

🧩 Product Manager Team → User Stories

⚙️ Program Manager Team → Product Features

🧑‍💻 Development Engineer Team → Engineering Tasks

Each team’s KnowledgeAugmentedPromptAgent generates responses.

EvaluationAgents validate and refine those outputs.

Output:

A complete structured plan containing validated stories, features, and tasks.

🧰 Setup & Usage
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI-Agentic-Workflow.git
cd AI-Agentic-Workflow

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

4️⃣ Run Tests for Agents (Phase 1)
python Phase1/tests/test_direct_prompt_agent.py


(repeat for each test script)

5️⃣ Run the Agentic Workflow (Phase 2)
python Phase2/agentic_workflow.py

6️⃣ View Output

Check the Phase2/outputs/workflow_output.txt file or terminal for results.

🧩 Example Output (Excerpt)
[Action Plan Step 1] Generate user stories
[Product Manager] Created 5 user stories following required structure.
[EvaluationAgent] Validation successful.

[Action Plan Step 2] Define product features
[Program Manager] Generated 3 high-level features.

[Action Plan Step 3] Create engineering tasks
[Development Engineer] Created 12 detailed engineering tasks with dependencies.

✅ Final Output: Complete structured plan generated successfully!

🧠 Key AI & Agentic Concepts Demonstrated

Prompt Chaining & Routing – connecting and orchestrating agent outputs dynamically.

Agent Collaboration – agents acting as distinct personas (TPM, PM, Engineer).

LLM Evaluation Loops – using EvaluationAgents for quality assurance.

Reusability – modular agent design for future workflows.

Scalable Project Management – transforming product ideas into actionable development plans.

🧩 Skills Demonstrated

Python for AI workflow design

Agentic system architecture

Multi-agent orchestration

OpenAI API integration

Prompt engineering and evaluation loops

Project automation & intelligent planning

🏆 Acknowledgments

Developed as part of the Agentic Workflows Course — demonstrating the design and implementation of dynamic, intelligent AI systems capable of reasoning, planning, and acting collaboratively.