import subprocess


def get_hostname():
    hostname = subprocess.check_output("hostname", shell=True)

    return hostname


def get_mac_address():
    command = f"ip link show | grep \"eth\" | awk '{{print $2}}' | sed -n 2p"
    mac_address = subprocess.check_output(command, shell=True)

    return mac_address


def get_cpu_cores():
    cores = int(subprocess.check_output("nproc", shell=True).strip())

    return cores


def get_cpu_utilization():
    cpu_utilization = float(subprocess.check_output(
        "top -b -n 1 -U $(whoami) | grep \"$(whoami)\" | awk '{total+=$9} END {print total}'", shell=True).strip())

    return cpu_utilization / 100


def get_memory_amount():
    memory_kb = int(subprocess.check_output(
        "cat /proc/meminfo | grep \"MemTotal\" | awk '{print $2}'", shell=True).strip())
    memory_mb = memory_kb / 1000

    return memory_mb


def get_memory_utilization():
    memory_utilization = float(subprocess.check_output(
        "top -b -n 1 -U $(whoami) | grep \"$(whoami)\" | awk '{total += $10} END {print total}'", shell=True).strip())

    return memory_utilization


def get_disk_size():
    disk_size = subprocess.check_output(
        "df -h |  grep \"boot$\" | awk '{print $5}' | tr -d '%'", shell=True)

    return disk_size


def get_disk_utilization():
    disk_utilization_gb = float(subprocess.check_output(
        "df -h | grep \"/dev/vda1\" | awk '{print $2}' | tr -d G", shell=True).strip())

    disk_utilization_mb = disk_utilization_gb * 1000

    return disk_utilization_mb
