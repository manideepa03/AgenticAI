# agentic_workflow.py
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#1 - Import the following agents: ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent from the workflow_agents.base_agents module
from phase_1.workflow_agents.base_agents import ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent

# 2 - Load the OpenAI key into a variable called openai_api_key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
# load the product spec
# 3 - Load the product spec document Product-Spec-Email-Router.txt into a variable called product_spec
with open("Product-Spec-Email-Router.txt", "r", encoding = "utf-8") as f:
    product_spec = f.read()
# Instantiate all the agents
#  = ActionPlanningAgent(openai_api_key)
# knowledge_augmented_agent = KnowledgeAugmentedPromptAgent(openai_api_key)
# evaluation_agent = EvaluationAgent(openai_api_key)
# routing_agent = RoutingAgent(openai_api_key)

# Action Planning Agent
# knowledge_action_planning = (
#     "Stories are defined from a product spec by identifying a "
#     "persona, an action, and a desired outcome for each story. "
#     "Each story represents a specific functionality of the product "
#     "described in the specification. \n"
#     "Features are defined by grouping related user stories. \n"
#     "Tasks are defined for each story and represent the engineering "
#     "work required to develop the product. \n"
#     "A development Plan for a product contains all these components"
#     "The action steps should any or all the three steps based on the user prompt: generate user stories (no features and no development), generate features (no user stories or no development tasks) and generate development tasks(no user stories or no features)"
#     "Do not consider other steps"
# )

knowledge_action_planning = (
    "Analyze the user prompt and include any of the below actions its asking"
    "1. USER STORIES: Generate user stories only for the specified product.",
    "2. PRODUCT FEATURES: Generate product features derived from grouping user stories of product. Do not include user stories",
    "3. ENGINEERING TASKS: Generate development engineering tasks derived for product. Do not include user stories or features, do not route to product manager"
    "Do not include random details, only include details all perterining to product specified"
    "Follow the evaluation criteria"
)
# 4 - Instantiate an action_planning_agent using the 'knowledge_action_planning'
action_planning_agent = ActionPlanningAgent(openai_api_key, knowledge_action_planning)
# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    f"Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    f"The sentences always start with: As a "
    f"Write several stories for the product spec below, where the personas are the different users of the product. "
    # 5 - Complete this knowledge string by appending the product_spec loaded in 3
    f"---BEGIN PRODUCT SPEC---\n"
    f"Here is the Product-Spec-Email-Router.txt: {product_spec}\n"
    f"Do not use outside knowledge"
    # f"Use the Product-Spec-Email-Router.txt content to generate relevant user stories \n"
    # f"Create features specific to the users stories of product \n"
    # f"Generate engineering tasks for based on the features \n"
    f"---END PRODUCT SPEC---"
)
# 6 - Instantiate a product_manager_knowledge_agent using 'persona_product_manager' and the completed 'knowledge_product_manager'
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_product_manager, knowledge_product_manager)
# Product Manager - Evaluation Agent
# 7 - Define the persona and evaluation criteria for a Product Manager evaluation agent and instantiate it as product_manager_evaluation_agent. This agent will evaluate the product_manager_knowledge_agent.
# The evaluation_criteria should specify the expected structure for user stories (e.g., "As a [type of user], I want [an action or feature] so that [benefit/value].").
persona_product_manager_evaluation = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria = "The answer should be stories that follow the following structure: As a [type of user], I want [an action or feature] so that [benefit/value]."
product_manager_evaluation_agent = EvaluationAgent(openai_api_key, persona_product_manager_evaluation,evaluation_criteria, product_manager_knowledge_agent, 10)

# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the all features for a product."
knowledge_program_manager = """Features of a product are defined by organizing similar user stories into cohesive groups. Do not consider outside knowledge: Only see knowledge from {product_spec}. Each features should contain 
    Feature name, Description, Key Functionality, User Benefit"""
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
# (This is a necessary step before. Students should add the instantiation code here.)
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_program_manager, knowledge_program_manager)

# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."

# 8 - Instantiate a program_manager_evaluation_agent using 'persona_program_manager_eval' and the evaluation criteria below.
#                      "The answer should be product features that follow the following structure: " \
#                      "Feature Name: A clear, concise title that identifies the capability\n" \
#                      "Description: A brief explanation of what the feature does and its purpose\n" \
#                      "Key Functionality: The specific capabilities or actions the feature provides\n" \
#                      "User Benefit: How this feature creates value for the user"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
program_manager_evaluation_criteria = """
"The answer should be product features that follow the following structure: " \
"Feature Name: A clear, concise title that identifies the capability\n" \
"Description: A brief explanation of what the feature does and its purpose\n" \
"Key Functionality: The specific capabilities or actions the feature provides\n" \
"User Benefit: How this feature creates value for the user"
"""
program_manager_evaluation_agent = EvaluationAgent(openai_api_key, persona_program_manager_eval, program_manager_evaluation_criteria, program_manager_knowledge_agent, 10)

# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = (
    "Development tasks are defined by identifying what needs to be built to implement each user story." 
    # "The tasks must be directly related to the product described below:\n\n"
    f"Consider knowledge from only this: {product_spec}\n\n"
    "Ensure engineering tasks include all required fields (ID, Title, Related User Story, Description, Acceptance Criteria, Estimated Effort, Dependencies)."
)
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before  9. Students should add the instantiation code here.)
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_dev_engineer, knowledge_dev_engineer)
# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = f"You are an evaluation agent that checks the answers from dev engineer agent and  make sure the response meets the exact evaluation criteria"
# 9 - Instantiate a development_engineer_evaluation_agent using 'persona_dev_engineer_eval' and the evaluation criteria below.
#                      "The answer should be tasks following this exact structure: " \
#                      "Task ID: A unique identifier for tracking purposes\n" \
#                      "Task Title: Brief description of the specific development work\n" \
#                      "Related User Story: Reference to the parent user story\n" \
#                      "Description: Detailed explanation of the technical work required\n" \
#                      "Acceptance Criteria: Specific requirements that must be met for completion\n" \
#                      "Estimated Effort: Time or complexity estimation\n" \
#                      "Dependencies: Any tasks that must be completed first"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.

dev_engineer_evaluation_criteria = """"The answer should be tasks following this exact structure: " \
"Task ID: A unique identifier  for tracking purposes\n" \
"Task Title: Brief description of the specific development work\n" \
"Related User Story: Reference to the parent user story\n" \
"Description: Detailed explanation of the technical work required\n" \
"Acceptance Criteria: Specific requirements that must be met for completion\n" \
"Estimated Effort: Time or complexity estimation\n" \
"Dependencies: Any tasks that must be completed first"
"""
development_engineer_evaluation_agent = EvaluationAgent(openai_api_key, persona_dev_engineer_eval, dev_engineer_evaluation_criteria, development_engineer_knowledge_agent, 10)


# Routing Agent
#10 - Instantiate a routing_agent. You will need to define a list of agent dictionaries (routes) for Product Manager, Program Manager, and Development Engineer. Each dictionary should contain 'name', 'description', and 'func' (linking to a support function). Assign this list to the routing_agent's 'agents' attribute.
routing_agent = RoutingAgent(openai_api_key, {})
agents = [
    {
        "name": "Product Manager",
        "description": (
            "Creates user personas and user stories describing user goals. "
            "Focuses on user needs and outcomes. Does NOT define product features or technical tasks."
         ),        
         "func": lambda x: product_manager_support_function(x)
    },
    {
        "name": "Program Manager",
        "description": (
            "Defines and organizes product features — the high-level capabilities of the product. "
            "Focuses on what the product should do, not who uses it or how it's built. "
            "Does NOT create user stories or technical tasks."
        ),        
        "func": lambda x: program_manager_support_function(x)
    },
    {
        "name": "Development Engineer",
        "description": "Responsible for defining the development tasks.  Does not create personas or do not define features.",
        "func": lambda x: development_engineer_support_function(x)
    }
]
routing_agent.agents = agents
# Job function persona support functions
#11 - Define the support functions for the routes of the routing agent (e.g., product_manager_support_function, program_manager_support_function, development_engineer_support_function).
# Each support function should:
#   1. Take the input query (e.g., a step from the action plan).
#   2. Get a response from the respective Knowledge Augmented Prompt Agent.
#   3. Have the response evaluated by the corresponding Evaluation Agent.
#   4. Return the final validated response.
def product_manager_support_function(query):
    product_response = product_manager_knowledge_agent.respond(query)
    evaluation_product = product_manager_evaluation_agent.evaluate(product_response)
    return evaluation_product['final_response']

def program_manager_support_function(query):
    program_response = program_manager_knowledge_agent.respond(query)
    evaluation_program = program_manager_evaluation_agent.evaluate(program_response)
    return evaluation_program['final_response']

def development_engineer_support_function(query):
    development_response = development_engineer_knowledge_agent.respond(query)
    evaluation_dev = development_engineer_evaluation_agent.evaluate(development_response)
    return evaluation_dev['final_response']





# Run the workflow

print("\n*** Workflow execution started ***\n")
# Workflow Prompt
# ****
#workflow_prompt = "What would the development tasks for this product be?"
workflow_prompt = "Create a comprehensive project plan for the Email Router system including user s ries, product features, and detailed engineering tasks based on the product specification"
# ****
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
# 12 - Implement the workflow.
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
#   2. Initialize an empty list to store 'completed_steps'.
#   3. Loop through the extracted workflow steps:
#      a. For each step, use the 'routing_agent' to route the step to the appropriate support function.
#      b. Append the result to 'completed_steps'.
#      c. Print information about the step being executed and its result.
#   4. After the loop, print the final output of the workflow (the last completed step).
response_steps = action_planning_agent.extract_steps_from_prompt(
     f"Given this workflow prompt: {workflow_prompt}, "
    "generate actionable steps"
    "Do not repeat broad project planning steps."
)
completed_steps = []

print(response_steps)

for step in response_steps:
    print(f"\n Next step is: {step}")
    result = routing_agent.router(step)
    # if result.lower().startswith("yes"):
    #     completed_steps.append(result)
    if isinstance(result, str):
        completed_steps.append(result.strip())
    else:
        completed_steps.append(str(result))
    # print("\n Result:")
    # print(result)

print(f"\nThe final output of the workflow:")
user_stories = []
product_features = []
engineering_tasks = []

for step in completed_steps:
    clean_step = step.strip()
    lower_step = clean_step.lower()

    # --- Detect ENGINEERING TASKS ---
    if (
        "task id:" in lower_step
        or "acceptance criteria:" in lower_step
        or "estimated effort:" in lower_step
        or "dependencies:" in lower_step
    ):
        engineering_tasks.append(clean_step)

    # --- Detect USER STORIES ---
    elif lower_step.startswith("as a ") and "task id:" not in lower_step:
        user_stories.append(clean_step)

    # --- Detect PRODUCT FEATURES ---
    elif (
        "feature name:" in lower_step
        or "feature:" in lower_step
        or "features:" in lower_step
        or "key functionality:" in lower_step
        or "user benefit:" in lower_step
    ):
        product_features.append(clean_step)

    # --- Catch unclassified (for debugging) ---
    else:
        print(f"⚠️ Unclassified step detected:\n{clean_step}\n")

# Build final formatted output
final_output = "=== USER STORIES ===\n"
final_output += "\n".join(user_stories) + "\n\n"

final_output += "=== PRODUCT FEATURES ===\n"
final_output += "\n".join(product_features) + "\n\n"

final_output += "=== ENGINEERING TASKS ===\n"
final_output += "\n".join(engineering_tasks)

# Display or save final result
print("\n=== FINAL PROJECT PLAN ===\n")
print(final_output)