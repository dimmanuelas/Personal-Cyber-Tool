import socket

def scan_ports(target, mode="common"):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        return {
            "success": False,
            "error": "Invalid Domain or IP address."
        }

    if mode == "common":
        ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
    elif mode == "all":
        ports = range(1, 1025)
    else:
        return {
            "success": False,
            "error": "Invalid scan mode."
        }
    
    port_results = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        
        status = "OPEN" if result == 0 else "CLOSED"
        port_results.append({"port": port, "status": status})
        s.close()
        
    return {
        "success": True,
        "target": target,
        "target_ip": target_ip,
        "mode": mode,
        "results": port_results
    }
