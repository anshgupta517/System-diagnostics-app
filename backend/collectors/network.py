import psutil
import speedtest

def get_network_stats():
    """Returns internet speeds by running an actual speed test, plus cumulative usage."""
    try:
        # Run actual internet speed test
        st = speedtest.Speedtest()
        
        # Find best server to minimize latency
        st.get_best_server()
        
        # Calculate speeds in bits per second
        download_bps = st.download()
        upload_bps = st.upload()
        ping_ms = st.results.ping
        
        # Convert bits per second to Megabits per second
        download_mbps = round(download_bps / 1_000_000, 2)
        upload_mbps = round(upload_bps / 1_000_000, 2)

        # Get cumulative usage stats for context
        net_io = psutil.net_io_counters()

        def bytes_to_gb(bytes_val):
            return f"{round(bytes_val / (1024 ** 3), 2)} GB"
            
        return {
            "upload_speed": f"{upload_mbps} Mbps",
            "download_speed": f"{download_mbps} Mbps",
            "ping": f"{round(ping_ms)} ms",
            "total_uploaded": bytes_to_gb(net_io.bytes_sent),
            "total_downloaded": bytes_to_gb(net_io.bytes_recv),
            "packets_sent": net_io.packets_sent,
            "packets_recv": net_io.packets_recv
        }
    except Exception as e:
        return {"error": f"Could not complete speed test: {str(e)}"}
