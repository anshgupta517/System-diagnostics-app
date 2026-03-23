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
        "You are SystemMind, an expert AI system diagnostic assistant running locally on the user's machine. "
        "Your purpose is to help users understand their computer's current health based on real-time metrics which you will be provided: CPU, RAM, Disk, and Network bandwidth.(one or more at a time) "
        "A beautiful visual dashboard is already displaying these exact numbers and charts to the user in their UI. "
        "Therefore, DO NOT just robotically repeat the raw numbers. Instead, provide a concise, expert text analysis of WHAT those numbers mean. "
        "For example, if memory is high, identify the specific culprit processes (by name and PID) causing the bottleneck. "
        "Rules: "
        "1. Keep your answer conversational, brief, and formatted cleanly with markdown. "
        "2. Do not invent data; rely strictly on the provided JSON payload. "
        "3. Usernames and sensitive paths have been REDACTED for privacy. "
        "4. Always conclude with an actionable, helpful tip genuinely related to their actual current metrics or their specific query."
        "5. If data is unavailable, say so and do not make up data and just explain the situation."
    )
    
    prompt = f"System Data:\n```json\n{json.dumps(scrubbed_data, indent=2)}\n```\n\nUser Query: {user_message}"
    print(prompt)
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
