import psutil
import time

def get_process_list(limit=5):
    """Returns top processes by CPU and Memory usage."""
    procs = []
    
    # psutil requires calculating the delta for cpu_percent. 
    # Calling it once returns 0.0 usually. We need a small delay.
    for p in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        try:
            # First call initializes
            p.cpu_percent(interval=None)
            procs.append(p)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Give it a tiny moment to measure (0.1s is enough for a quick read)
    time.sleep(0.1)

    proc_data = []
    for p in procs:
        try:
            info = p.info
            # Second call gets the actual delta
            info['cpu_percent'] = p.cpu_percent(interval=None) 
            proc_data.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Sort by CPU usage
    top_cpu = sorted(proc_data, key=lambda p: p['cpu_percent'], reverse=True)[:limit]
    
    # Sort by Memory usage
    top_mem = sorted(proc_data, key=lambda p: p['memory_percent'], reverse=True)[:limit]
    
    return {
        "top_cpu_processes": top_cpu,
        "top_memory_processes": top_mem
    }
