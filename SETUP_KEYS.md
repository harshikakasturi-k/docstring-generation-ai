# 🔑 How to Set Up API Keys for Dokki

To use the AI Docstring Agent ("Dokki"), you need an API Key from OpenAI (or a local LLM setup).

## Option 1: Interactive Setup (Easiest)

1.  Run the agent:
    ```bash
    python run_agent.py
    ```
2.  Dokki will ask you: "Do you want to update your OpenAI API Key?".
3.  Type `y` and press Enter.
4.  Paste your key (it will be hidden) and press Enter.
5.  Done!

## Option 2: Environment Variable (Best for Security)

1.  **Windows (Powershell)**:
    ```powershell
    $env:OPENAI_API_KEY="sk-..."
    python run_agent.py
    ```

2.  **Windows (Command Prompt)**:
    ```cmd
    set OPENAI_API_KEY=sk-...
    python run_agent.py
    ```

## Option 3: Manual Config File

1.  Navigate to `d:\Drive D\nasiko\docstring_agent\utils`.
2.  Create or edit `config.json`.
3.  Add your key like this:

```json
{
    "user_name": "Your Name",
    "api_keys": {
        "openai": "sk-your-actual-key-here"
    }
}
```

## Option 4: Use Groq (Fast & Free Tier)

If OpenAI is giving you "insufficient_quota" errors, use Groq instead. It's much faster!

1.  Get a key from [console.groq.com](https://console.groq.com/keys).
2.  Open `d:/Drive D/nasiko/docstring_agent/utils/config.json`.
3.  Set `"preferred_provider": "groq"`.
4.  Paste your key in `"groq": "gsk_..."`.

## ⚠️ Troubleshooting Errors

If you see errors about `langsmith` or imports:
1.  It usually means a package version mismatch.
2.  Try running this to clean up:
    ```bash
    pip install --upgrade langchain langchain-openai langchain-community
    ```
3.  If it hangs, check if it's waiting for your input!
