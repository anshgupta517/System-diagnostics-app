import json

async def query_llm(user_message: str, system_data: dict = None):
    """
    Simulates an LLM response. 
    In the future, this will call OpenAI/Anthropic/Local LLM.
    """
    
    if not system_data:
        # Phase 1: Simple keyword matching to simulate "thinking" or "checking"
        return "I need to check your system stats to answer that. (This is a mock response, data not collected yet)"

    # If we have data, we summarize it (Mocking the summary)
    summary_lines = ["Here is what I found on your system:"]
    
    if "get_cpu_stats" in system_data:
        cpu = system_data["get_cpu_stats"]
        summary_lines.append(f"- CPU Usage is at {cpu.get('total_cpu_usage')}.")
        
    if "get_memory_stats" in system_data:
        mem = system_data["get_memory_stats"]
        summary_lines.append(f"- RAM Usage: {mem.get('ram_percent')} ({mem.get('ram_used')} used of {mem.get('ram_total')}).")
        
    if "get_process_list" in system_data:
        procs = system_data["get_process_list"]
        print(procs)
        top_cpu = procs.get('top_cpu_processes', [])[0]
        print("==========================================")
        print(top_cpu)
        if top_cpu:
            summary_lines.append(f"- Top CPU consumer: {top_cpu['name']} ({top_cpu['cpu_percent']}%)")
            
    summary_lines.append("\nBased on this, everything looks " + ("normal." if "8" not in str(system_data) else "a bit high."))
    
    return "\n".join(summary_lines)
