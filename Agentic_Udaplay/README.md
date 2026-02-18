# 🎮 UdaPlay – AI Research Agent for Gaming Analytics

UdaPlay is an AI-powered research assistant designed for gaming executives, analysts, and gamers. It answers natural language questions about video games using a hybrid Retrieval-Augmented Generation (RAG) system combined with intelligent web search fallback.

---

## 💬 Example Questions UdaPlay Can Answer

- Who developed FIFA 21?
- When was God of War Ragnarok released?
- What platform was Pokémon Red launched on?
- What is Rockstar Games working on right now?

---

## 🛠️ Technologies Used

- Python
- OpenAI LLM
- ChromaDB (Vector Database)
- Tavily API (Web Search)
- Pydantic (Validation)
- State Machine Design Pattern

---

## 🚀 Project Overview

UdaPlay is built as a stateful AI research agent that:

- Retrieves information from a local vector database (primary source)
- Evaluates retrieval quality and confidence
- Falls back to web search when internal knowledge is insufficient
- Persists newly discovered information into long-term memory
- Generates structured, well-cited responses

The system is designed to simulate a real-world AI research assistant used in gaming analytics environments.

---

## 🏗️ Architecture

### Two-Tier Retrieval System

### 🧠 Primary: RAG over Local Dataset

- Game data is preloaded from JSON files
- Data is processed and embedded into a persistent vector database (ChromaDB)
- Semantic search retrieves relevant game information

### 🌐 Secondary: Web Search (Tavily API)

- Triggered when internal retrieval confidence is low
- Performs real-time web search
- Extracted information is parsed and optionally persisted

---

## 📂 Project Structure

UdaPlay/
│
├── Udaplay_01_solution_project.ipynb
│ ├── Loads and processes game JSON files
│ ├── Creates embeddings
│ ├── Stores data in persistent ChromaDB
│ └── Demonstrates semantic querying
│
├── Udaplay_02_solution_project.ipynb
│ ├── Implements UdaPlay agent
│ ├── Defines tools (retrieve, evaluate, web search)
│ ├── Implements state machine workflow
│ ├── Runs example queries
│ └── Demonstrates reasoning + final structured answers
│
└── README.md


---

## 🧩 Core Components

### 1️⃣ RAG Pipeline

- Loads local JSON dataset of video games
- Cleans and formats data
- Generates embeddings
- Stores data in ChromaDB
- Supports semantic similarity search

---

### 2️⃣ Agent Tools

UdaPlay includes at least three tools:

#### 🔎 Internal Retrieval Tool

- Queries vector database
- Returns top semantic matches
- Structured output: title, release date, platform, publisher, etc.

#### 📊 Evaluation Tool

- Assesses relevance and completeness
- Determines confidence score
- Decides whether fallback is needed

#### 🌍 Web Search Tool (Tavily API)

- Performs web search when RAG is insufficient
- Extracts relevant information
- Returns structured and cited results