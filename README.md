# Zarnite Python SDK

Welcome to the official **Zarnite Python SDK**! This library allows you to build, manage, and scale real-time conversational AI tutors and RAG services on the Zarnite platform with minimal effort.

Designed for modern Python backends, CLI tools, and data science workflows, it comes with full typing, easy authentication, and built-in semantic error handling.

---

## 📦 Installation

Install the package via `pip`:

```bash
pip install zarnite
```

---

## 🚀 Quick Start

To talk to the Zarnite Platform, initialize the unified `Zarnite` client with your API key.

```python
import zarnite
from zarnite import ZarniteError

client = zarnite.Zarnite(
    api_key="zar_live_your_api_key_here"
)

def main():
    try:
        # 1. Fetch available tutor agents
        agents_envelope = client.agents.list_agents_v1_agents_get()
        agents = agents_envelope.data.data
        print(f"Found {len(agents)} active agents.")
        
    except ZarniteError as e:
        print(f"Error [{e.code}] (Status {e.status}): {e.message}")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
```

---

## 🛠️ Common Use Cases

### 1. Programmatic Agent Creation
Create a new conversational agent with dedicated language and voice configurations:

```python
new_agent = client.agents.create_agent_v1_agents_post({
    "name": "Spanish Tutor Maria",
    "language": "Spanish",
    "voice": "Aoede",
    "system_prompt": "You are Maria, a friendly Spanish tutor. Help the user practice conversational Spanish."
})

agent_id = new_agent.data.data.id
print(f"Created Agent ID: {agent_id}")
```

### 2. Ingesting Knowledge Documents (RAG)
Upload document guidelines (PDF, TXT, MD, DOCX) to ground your agent in custom knowledge context:

```python
# Upload an instructional document for a specific agent
with open("./rulesOfGrammar.pdf", "rb") as f:
    upload_response = client.knowledge.upload_agent_document_v1_agents_agent_id_documents_post(
        agent_id=agent_id,
        file=f
    )

print("Document indexed successfully!")
```

### 3. Bootstrapping a Real-Time Voice Session
Mint short-lived LiveKit credentials to join an interactive, real-time voice playground session:

```python
session_response = client.playground.bootstrap_session_v1_playground_sessions_post({
    "agent_id": agent_id,
    "learner_id": "learner_user_123",
    "enable_knowledge_base": True
})

data = session_response.data.data
print(f"Room Session Created: {data.session_id}")
print(f"LiveKit Server URL: {data.url}")
print(f"Access Token: {data.token}")

# You can now feed the returned URL & token directly to your LiveKit client
# to render an interactive voice UI stream!
```

---

## 🛡️ Error Handling
The SDK provides a `ZarniteError` class to intercept failures and easily debug validation errors, unauthorized attempts, or connectivity issues:

```python
try:
    client.agents.get_agent_v1_agents_agent_id_get(agent_id="invalid_id")
except ZarniteError as e:
    print("Status Code:", e.status) # e.g., 404
    print("Error Code:", e.code)     # e.g., "API_ERROR"
    print("Payload:", e.data)         # Parsed response payload
```

---

## 📄 License
MIT © Zarnite Platform
