from database import create_connection
import system
from dotenv import load_dotenv
import time

load_dotenv()

conn = create_connection()
print('Successfully connected to the MySQL database!')


def run_statistics():
    device_name = system.get_hostname()
    device_mac = system.get_mac_address()
    device_cpu_cores = system.get_cpu_cores()
    device_cpu_speed = system.get_cpu_speed()
    device_cpu_utilization = system.get_cpu_utilization()
    device_memory_amount = system.get_memory_amount()
    device_memory_utilization = system.get_memory_utilization()
    device_disk_size = system.get_disk_size()
    device_disk_utilization = system.get_disk_utilization()

    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT into device_statistics 
        (
            device_name,
            device_mac,
            cpu_cores,
            cpu_speed,
            cpu_utilization,
            memory_amount,
            memory_utilization,
            disk_size,
            disk_utilization
        ) 
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''',
        (
            device_name,
            device_mac,
            device_cpu_cores,
            device_cpu_speed,
            device_cpu_utilization,
            device_memory_amount,
            device_memory_utilization,
            device_disk_size,
            device_disk_utilization
        )
    )

    conn.commit()
    cursor.close()


if __name__ == '__main__':
    while True:
        run_statistics()
        print('Ran statistics, sleeping...')
        time.sleep(30)
