import psutil
import speedtest

def get_network_stats():
    """Returns internet speeds by running an actual speed test, plus cumulative usage."""
    
    # Initialize basic cumulative and packet stats that rarely fail
    try:
        net_io = psutil.net_io_counters()

        def bytes_to_gb(bytes_val):
            return f"{round(bytes_val / (1024 ** 3), 2)} GB"
            
        stats = {
            "total_uploaded": bytes_to_gb(net_io.bytes_sent),
            "total_downloaded": bytes_to_gb(net_io.bytes_recv),
            "packets_sent": net_io.packets_sent,
            "packets_recv": net_io.packets_recv
        }
    except Exception as e:
        return {"error": f"Could not read local network counters: {str(e)}"}

    # Run actual internet speed test in a separate error boundary
    try:
        st = speedtest.Speedtest()
        
        # Find best server to minimize latency
        st.get_best_server()
        
        # Calculate speeds in bits per second
        download_bps = st.download()
        upload_bps = st.upload()
        ping_ms = st.results.ping
        
        # Convert bits per second to Megabits per second
        stats["download_speed"] = f"{round(download_bps / 1_000_000, 2)} Mbps"
        stats["upload_speed"] = f"{round(upload_bps / 1_000_000, 2)} Mbps"
        stats["ping"] = f"{round(ping_ms)} ms"
        
    except Exception as e:
        stats["download_speed"] = "N/A"
        stats["upload_speed"] = "N/A"
        stats["ping"] = "N/A"
        stats["speedtest_error"] = str(e)
        
    return stats

