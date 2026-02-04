import psutil

def get_process_list(limit=5):
    """Returns top processes by CPU and Memory usage."""
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        try:
            p.info['cpu_percent'] = p.cpu_percent(interval=None) # Non-blocking
            procs.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Sort by CPU usage
    top_cpu = sorted(procs, key=lambda p: p['cpu_percent'], reverse=True)[:limit]
    
    # Sort by Memory usage
    top_mem = sorted(procs, key=lambda p: p['memory_percent'], reverse=True)[:limit]
    
    return {
        "top_cpu_processes": top_cpu,
        "top_memory_processes": top_mem
    }
