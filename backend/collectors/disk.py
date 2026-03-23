import psutil

def get_disk_stats():
    """Returns total, used, and free disk space for the primary partition."""
    try:
        usage = psutil.disk_usage('/')
        
        def bytes_to_gb(bytes_val):
            return round(bytes_val / (1024 ** 3), 2)
    
        return {
            "disk_total": f"{bytes_to_gb(usage.total)} GB",
            "disk_used": f"{bytes_to_gb(usage.used)} GB",
            "disk_free": f"{bytes_to_gb(usage.free)} GB",
            "disk_percent": f"{usage.percent}%"
        }
    except Exception as e:
        return {"error": f"Could not read disk stats: {str(e)}"}
