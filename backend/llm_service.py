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
            summary_lines.append(f"- Top CPU consumer: {top_cpu['name']} ({top_cpu['cpu_percent']:.1f}%)")
            
    summary_lines.append("\nBased on this, everything looks " + ("normal." if "8" not in str(system_data) else "a bit high."))

    # Generate suggestions for resource management
    suggestion_lines = []
    if "get_process_list" in system_data and "get_memory_stats" in system_data and "get_cpu_stats" in system_data:
        try:
            cpu_val = float(system_data["get_cpu_stats"].get('total_cpu_usage', '0').replace('%', ''))
            mem_val = float(system_data["get_memory_stats"].get('ram_percent', '0').replace('%', ''))
            
            procs = system_data["get_process_list"]
            top_cpu = procs.get('top_cpu_processes', [])[0] if procs.get('top_cpu_processes') else None
            top_mem = procs.get('top_memory_processes', [])[0] if procs.get('top_memory_processes') else None

            needs_suggestion = False
            if "spike" in user_message.lower() or "why" in user_message.lower() or "suggestion" in user_message.lower():
                needs_suggestion = True
            elif cpu_val > 70 or mem_val > 70:
                needs_suggestion = True
                
            if needs_suggestion:
                suggestion_lines.append("\n💡 **Suggestion on managing your resources:**")
                added_specific_suggestion = False
                
                if cpu_val > 50 and top_cpu:
                    suggestion_lines.append(f"- Your CPU usage is elevated. You should check the '{top_cpu['name']}' process (PID: {top_cpu['pid']}) because it is using {top_cpu['cpu_percent']:.1f}% of your CPU.")
                    added_specific_suggestion = True
                    
                if mem_val > 60 and top_mem:
                    suggestion_lines.append(f"- Your RAM usage is high. The '{top_mem['name']}' process (PID: {top_mem['pid']}) is currently consuming {top_mem['memory_percent']:.1f}% of your memory. Consider closing it if it's not needed.")
                    added_specific_suggestion = True
                
                if not added_specific_suggestion and top_cpu and top_mem:
                    suggestion_lines.append(f"- While your overall metrics aren't critically high, the heaviest applications right now are '{top_cpu['name']}' on CPU and '{top_mem['name']}' on RAM. Keeping fewer background apps open helps manage resources.")

            if suggestion_lines:
                summary_lines.extend(suggestion_lines)
        except Exception as e:
            # Silently fail suggestion logic if parsing fails
            pass
            
    return "\n".join(summary_lines)
