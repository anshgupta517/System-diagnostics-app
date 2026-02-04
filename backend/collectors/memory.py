import psutil

def get_memory_stats():
    """Returns Memory (RAM) and Swap usage statistics."""
    vm = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    def bytes_to_gb(bytes_val):
        return round(bytes_val / (1024 ** 3), 2)

    return {
        "ram_total": f"{bytes_to_gb(vm.total)} GB",
        "ram_available": f"{bytes_to_gb(vm.available)} GB",
        "ram_used": f"{bytes_to_gb(vm.used)} GB",
        "ram_percent": f"{vm.percent}%",
        "swap_total": f"{bytes_to_gb(swap.total)} GB",
        "swap_used": f"{bytes_to_gb(swap.used)} GB",
        "swap_percent": f"{swap.percent}%",
    }
