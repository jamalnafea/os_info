import platform

def get_os_info():
    os_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return os_info

if __name__ == "__main__":
    info = get_os_info()
    for key, value in info.items():
        print(f"{key}: {value}")
