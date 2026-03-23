import os
import json
from google import genai
from google.genai import types

def scrub_sensitive_data(system_data: dict) -> dict:
    """Removes sensitive information like usernames from the system stats payload."""
    if not system_data:
        return system_data
    
    # Deep copy using JSON to avoid modifying the original data referencing mutable dicts
    scrubbed = json.loads(json.dumps(system_data))
    
    if "get_process_list" in scrubbed:
        for key in ["top_cpu_processes", "top_memory_processes"]:
            if key in scrubbed["get_process_list"]:
                for proc in scrubbed["get_process_list"][key]:
                    if "username" in proc:
                        # Scrub the username to ensure privacy
                        proc["username"] = "REDACTED"
                        
    return scrubbed

async def query_llm(user_message: str, system_data: dict = None):
    """
    Calls the Google Gemini API to analyze the system data and answer the user's query.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        return "Error: Gemini API key is not configured. Please set GEMINI_API_KEY in your .env file."
        
    if not system_data:
        return "I need to check your system stats to answer that. Let me get that data first."

    # 1. Scrub sensitive data
    scrubbed_data = scrub_sensitive_data(system_data)
    
    # 2. Prepare prompt
    system_instruction = (
        "You are an expert AI system diagnostic assistant. "
        "You help users understand their computer's performance using real-time metrics. "
        "Analyze the provided JSON system data and answer the user's query. "
        "Keep your answer concise, helpful, and formatted with markdown. "
        "If a process is consuming too much CPU or RAM, point it out including its PID. "
        "Do not invent data; only rely on the JSON provided. "
        "Do not mention usernames or sensitive paths, as they have been redacted."
        "Always include a helpful tip as well related to the stats."
    )
    
    prompt = f"System Data:\n```json\n{json.dumps(scrubbed_data, indent=2)}\n```\n\nUser Query: {user_message}"
    
    # 3. Call Gemini API
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.3
            )
        )
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error while calling the AI model: {str(e)}"
