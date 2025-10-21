# : 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
import os
from dotenv import load_dotenv
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
# : 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"

knowledge_augmented_prompt_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)
response = knowledge_augmented_prompt_agent.respond(prompt)

# : 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
print("Knowledge Augumented Prompt Agent Response:\n")
print(f"{response}\n")

# : 5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print("Knowledge source: The agent generated this response using knowledge given by the user")
