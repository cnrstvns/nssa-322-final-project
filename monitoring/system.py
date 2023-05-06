import subprocess

bin_bash = "/bin/bash"


def get_hostname():
    hostname = subprocess.getoutput("hostname")

    return hostname


def get_interface():
    interface = subprocess.getoutput(
        [bin_bash, "ifconfig | grep \"ens\" | awk -F [:] '{print $1}'"])

    return interface


def get_mac_address():
    interface = get_interface()

    command = f"ifconfig {interface} | grep \"ether\" | awk '{{print $2}}'"
    mac_address = subprocess.getoutput([bin_bash, command])

    return mac_address


def get_cpu_cores():
    cores = int(subprocess.check_output([bin_bash, "nproc"]))

    return cores


def get_cpu_utilization():
    cpu_utilization = int(subprocess.check_output(
        [bin_bash, "top -b -n 1 -U $(whoami) | grep \"$(whoami)\" | awk '{total+=$9} END {print total}'"]))

    return cpu_utilization / 100


def get_memory_amount():
    memory_amount = int(subprocess.check_output(
        [bin_bash, "lsmem | grep \"Total online\" | awk {print $4} | tr -d \"G\""])) * 1024

    return memory_amount


def get_memory_utilization():
    memory_utilization = int(subprocess.check_output(
        [bin_bash, "top -b -n 1 -U $(whoami) | grep \"$(whoami)\" | awk '{total+=$10} END {print total}'"]))

    return memory_utilization


def get_disk_size():
    disk_size = subprocess.getoutput(
        [bin_bash, "df -h |  grep \"boot$\" | awk '{print $5}' | tr -d '%'"])

    return disk_size


def get_disk_utilization():
    disk_utilization = subprocess.getoutput(
        [bin_bash, "df -h |  grep \"boot$\" | awk '{print $2}'"])

    return disk_utilization
