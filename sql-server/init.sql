CREATE DATABASE final_project;

USE final_project;

CREATE TABLE device_statistics (
  id INT AUTO_INCREMENT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  device_name VARCHAR(100) NOT NULL,
  device_mac VARCHAR(100) NOT NULL,
  cpu_cores INT NOT NULL,
  cpu_speed INT NOT NULL,
  cpu_utilization INT NOT NULL,
  memory_amount INT NOT NULL,
  memory_utilization INT NOT NULL,
  disk_size VARCHAR(25) NOT NULL,
  disk_utilization INT NOT NULL
  
  PRIMARY KEY (id)
)