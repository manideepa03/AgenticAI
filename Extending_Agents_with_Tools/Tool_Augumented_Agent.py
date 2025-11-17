#!/usr/bin/env python
# coding: utf-8

# #  Exercise - Building an AI Agent with Tools
# 
# In this exercise, you'll build an AI agent that can use tools to enhance its capabilities. You'll learn how to create an agent that can understand when to use tools, process their results, and maintain a coherent conversation.

# ## Challenge
# 
# Imagine you're building a smart coding assistant that needs to:
# - Answer programming questions
# - Execute code snippets
# - Look up documentation
# - Perform calculations
# - Search through codebases
# 
# Instead of hard-coding when to use each capability, your agent should intelligently decide when and how to use its available tools.

# ## Setup
# First, let's import the necessary libraries:

# In[1]:


from typing import List, Dict, Any
from dotenv import load_dotenv
from copy import deepcopy
import json

from lib.messages import UserMessage, SystemMessage, ToolMessage
from lib.tooling import tool
from lib.llm import LLM


# ## Understanding the Components
# 
# Before we build our agent, let's understand the key components we'll be working with:
# 
# - `LLM`: The language model wrapper that handles tool execution
# - `SystemMessage`: Defines the agent's role and behavior
# - `UserMessage`: Represents user inputs
# - `ToolMessage`: Contains tool execution results
# - `tool`: Decorator for creating tools

# ## Building the Agent Class
# 
# Your task is to create an Agent class that can:
# 1. Initialize with a specific role and set of tools
# 2. Process user messages
# 3. Decide when to use tools
# 4. Handle tool responses

# In[ ]:


class Agent:
    """An AI Agent that can use tools to help answer questions"""

    def __init__(
        self,
        role: str = "Personal Assistant",
        instructions: str = "Help users with any question",
        model: str = "gpt-4o-mini",
        temperature: float = 0.0,
        tools: List[Any] = None
    ):
        """Initialize the agent with its configuration and tools"""
        # 1: Initialize the agent
        # Hint: 
        # - Load environment variables with load_dotenv()
        # - Store agent settings (role, instructions, etc.)
        # - Create an LLM instance with the provided tools
        load_dotenv()
        #self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.role = role
        self.instructions = instructions
        self.model = model
        self.tools = tools
        self.llm = LLM ( 
            model = model,
            temperature = temperature,
            tools = tools,
        )

    def invoke(self, user_message: str) -> str:
        """Process a user message and return a response"""
        # 2: Set up the conversation
        # Hint:
        # - Create messages list with SystemMessage (role + instructions)
        # - Add UserMessage with user_message
        # - Get initial AI response using self.llm.invoke()
        messages = [
            SystemMessage(
                content = (
                    f" You are AI agent and your role is {self.role}"
                    f" Your instructions: {self.instructions}"
                )
            )
        ]
        messages.append(UserMessage(content=user_message))
        ai_message = self.llm.invoke(messages)
        messages.append(ai_message)

        # 3: Handle tool calls if needed
        # Hint:
        # - Check if ai_message.tool_calls exists
        # - For each tool call:
        #   * Get function name and arguments
        #   * Execute tool and get result
        #   * Add result as ToolMessage
        # - Get final AI response

        while ai_message.tool_calls:
            for call in ai_message.tool_calls:
                function_name = call.function.name
                function_args = json.loads(call.function.arguments)
                tool_call_id = call.id
                tool = next ((t for t in self.tools if t.name == function_name), None)
                if tool:
                    result = tool(**function_args)
                    messages.append(
                        ToolMessage(
                            content=json.dumps(result),
                            tool_call_id = tool_call_id,
                            name = function_name,
                        )
                    )

            ai_message = self.llm.invoke(messages)
            messages.append(ai_message)

        for m in messages:
            print(m)
        return ai_message.content


# ## Testing Your Agent
# 
# Once you've implemented the Agent class, test it with different scenarios:

# 1. Basic conversation without tools

# In[20]:


agent = Agent(role="Coding Assistant")
response = agent.invoke("What is Python? Be concise")
print(response)


# 2. Create a calculator tool

# In[5]:


@tool
def calculate(expression: str) -> float:
    """Evaluate a mathematical expression"""
    return eval(expression)


# In[6]:


# Create an agent with the calculator tool
math_agent = Agent(
    role="Math Assistant",
    tools=[calculate]
)


# In[7]:


response = math_agent.invoke("What is 23 * 45?")
print(response)


# In[8]:


# Test multiple tool usage
response = math_agent.invoke("If I multiply 3 by 5, what do I get? Then later add 7")
print(response)


# 3. Create a data analyst

# In[9]:


@tool
def get_games(num_games:int=1, top:bool=True) -> str:
    """
    Returns the top or bottom N games with highest or lowest scores.    
    args:
        num_games (int): Number of games to return (default is 1)
        top (bool): If True, return top games, otherwise return bottom (default is True)
    """
    data = [
        {"Game": "The Legend of Zelda: Breath of the Wild", "Platform": "Switch", "Score": 98},
        {"Game": "Super Mario Odyssey", "Platform": "Switch", "Score": 97},
        {"Game": "Metroid Prime", "Platform": "GameCube", "Score": 97},
        {"Game": "Super Smash Bros. Brawl", "Platform": "Wii", "Score": 93},
        {"Game": "Mario Kart 8 Deluxe", "Platform": "Switch", "Score": 92},
        {"Game": "Fire Emblem: Awakening", "Platform": "3DS", "Score": 92},
        {"Game": "Donkey Kong Country Returns", "Platform": "Wii", "Score": 87},
        {"Game": "Luigi's Mansion 3", "Platform": "Switch", "Score": 86},
        {"Game": "Pikmin 3", "Platform": "Wii U", "Score": 85},
        {"Game": "Animal Crossing: New Leaf", "Platform": "3DS", "Score": 88}
    ]
    # Sort the games list by Score
    # If top is True, descending order
    sorted_games = sorted(data, key=lambda x: x['Score'], reverse=top)

    # Return the N games
    return sorted_games[:num_games]


# In[10]:


# Create an agent with the multiple tools
data_analyst_agent = Agent(
    role="Game Stats Assistant",
    instructions="You can bring insights about a game dataset based on users questions",
    tools=[get_games]
)


# In[11]:


response = data_analyst_agent.invoke("What's the best game in the dataset?")
print(response)


# In[16]:


response = data_analyst_agent.invoke("What's the worst game in the dataset?")
print(response)


# In[17]:


response = data_analyst_agent.invoke("What is the average score?")
print(response)


# In[18]:


response = data_analyst_agent.invoke("What is the distribution of platforms?")
print(response)

