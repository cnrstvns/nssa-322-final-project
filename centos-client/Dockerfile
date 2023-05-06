#Get latest centos os
FROM centos:latest

# Set up ENV for database
ENV DB_HOST="sql-server"
ENV DB_USER="root"
ENV DB_PASSWORD="root"
ENV DB_NAME="final_project"
ENV DB_PORT="3306"

RUN cd /etc/yum.repos.d/

# Fix mirrorlist bug
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

# Update VM
RUN yum update -y

# Install dependencies
RUN yum install -y wget make gcc openssl-devel bzip2-devel libffi-devel zlib-devel xz-devel 

# Download python tarball to /usr/src
RUN cd /usr/src && wget https://www.python.org/ftp/python/3.7.11/Python-3.7.11.tgz  

# Extract python tarball and run make
RUN cd /usr/src && tar xzf Python-3.7.11.tgz
RUN cd /usr/src/Python-3.7.11 && ./configure --enable-optimizations && make altinstall

# Install python on VM
RUN yum install -y python3-pip

# Install python packages
RUN python3.7 -m pip install mysql-connector-python python-dotenv

# Install git
RUN yum install -y git

# Get the scripts from GitHub
RUN cd home && git clone https://github.com/cnrstvns/nssa-322-final-project 

# Run the monitoring script
CMD cd /home/nssa-322-final-project/monitoring && python3.7 main.py