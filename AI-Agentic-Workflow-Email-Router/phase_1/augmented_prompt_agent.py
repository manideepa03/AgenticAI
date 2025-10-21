# : 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# : 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
augmented_prompt_agent = AugmentedPromptAgent(openai_api_key, persona)

# : 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = augmented_prompt_agent.respond(prompt)
# Print the agent's response
print("Augmented Prompt Agent Response:\n")
print(f"{augmented_agent_response}\n")

# : 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt.
# - How the system prompt specifying the persona affected the agent's response.
print(f"""Knowledge source: The agent generated this response using general world knowledge and reasoning abilities from the LLM, using the 
defined persona. As a result, the response started with "Dear student," and then gave the answer""")
