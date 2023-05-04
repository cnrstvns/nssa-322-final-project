import subprocess


def get_hostname():
    hostname = subprocess.getoutput("hostname")

    return hostname


def get_interface():
    return "en10"

    interface = subprocess.getoutput(
        "ifconfig | grep \"ens\" | awk -F [:] '{print $1}'")

    return interface


def get_mac_address():
    interface = get_interface()

    command = f"ifconfig {interface} | grep \"ether\" | awk '{{print $2}}'"
    mac_address = subprocess.getoutput(command)

    return mac_address


def get_cpu_cores():
    cores = int(subprocess.check_output(["nproc"]))

    return cores


def get_cpu_speed():
    return '1.0'

    cpu_speed = int(subprocess.check_output(
        "lscpu | grep \"MHz\" | awk '{print $3}'"))

    return cpu_speed


def get_cpu_utilization():
    return .10

    cpu_utilization = int(subprocess.check_output(
        "top -b -n 1 -U $(whoami) | grep \"$(whoami)\" | awk '{total+=$9} END {print total}'"))

    return cpu_utilization / 100


def get_memory_amount():
    return 16384

    memory_amount = int(subprocess.check_output(
        "lsmem | grep \"Total online\" | awk {print $4} | tr -d \"G\" ")) * 1024

    return memory_amount


def get_memory_utilization():
    return .64

    memory_utilization = int(subprocess.check_output(
        "top -b -n 1 -U $(whoami) | grep \"$(whoami)\" | awk '{total+=$10} END {print total}'"))

    return memory_utilization


def get_disk_size():
    disk_size = subprocess.getoutput(
        "df -h |  grep \"boot$\" | awk '{print $5}' | tr -d '%'")

    return disk_size


def get_disk_utilization():
    return '8.5Gi'

    disk_utilization = subprocess.getoutput(
        "df -h |  grep \"boot$\" | awk '{print $2}'")

    return disk_utilization
