from collectors.cpu import get_cpu_stats
from collectors.memory import get_memory_stats
from collectors.process import get_process_list

AVAILABLE_TOOLS = {
    "get_cpu_stats": get_cpu_stats,
    "get_memory_stats": get_memory_stats,
    "get_process_list": get_process_list
}

def router_tool_calls(intent: str):
    """
    Decides which tools to call based on the intent (or tool names provided by LLM).
    For Phase 1, we might just receive a list of tool names strings from the LLM service.
    """
    # For simplicity in Phase 1, we assume the LLM returns a list of tool names to call.
    # In a real agentic loop, this would parse JSON tool calls.
    
    results = {}
    
    # Simple heuristic for keyword matching if LLM isn't doing the selection fully yet
    # Or strict mapping if LLM returns "call_tool: get_cpu_stats"
    
    # Let's assume input is a list of tool_names for now
    tool_names = []
    if "cpu" in intent.lower():
        tool_names.append("get_cpu_stats")
    if "memory" in intent.lower() or "ram" in intent.lower():
        tool_names.append("get_memory_stats")
    if "process" in intent.lower() or "slow" in intent.lower() or "spike" in intent.lower() or "why" in intent.lower() or "suggestion" in intent.lower(): 
        tool_names.append("get_process_list")
        if "cpu" not in intent.lower(): tool_names.append("get_cpu_stats") 
        if "memory" not in intent.lower() and "ram" not in intent.lower(): tool_names.append("get_memory_stats")
        
    # Deduplicate
    tool_names = list(set(tool_names))
    
    for tool_name in tool_names:
        if tool_name in AVAILABLE_TOOLS:
            results[tool_name] = AVAILABLE_TOOLS[tool_name]()
            
    return results
