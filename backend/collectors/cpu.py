import psutil

def get_cpu_stats():
    """Returns CPU usage statistics."""
    # interval=1 blocks for 1 second to get accurate reading. 
    # For a chat app, we might want to make this async or accept 0 if previously polled, 
    # but 1s is acceptable for "checking status"
    total_cpu = psutil.cpu_percent(interval=1)
    
    # Per core could be useful later, but sticking to basics
    # per_core = psutil.cpu_percent(interval=1, percpu=True)
    
    return {
        "total_cpu_usage": f"{total_cpu}%",
        "cpu_count_logical": psutil.cpu_count(logical=True),
        "cpu_count_physical": psutil.cpu_count(logical=False),
        # "cpu_freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else "N/A"
    }
