#Get latest centos os
FROM centos:latest

RUN cd /etc/yum.repos.d/

# Fix mirrorlist bug
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

# Update VM
RUN yum update -y

# Install dependencies
RUN yum install -y wget make gcc openssl-devel bzip2-devel libffi-devel zlib-devel xz-devel 

# Install python cd /usr/src
RUN cd /usr/src && wget https://www.python.org/ftp/python/3.7.11/Python-3.7.11.tgz  

RUN cd /usr/src && tar xzf Python-3.7.11.tgz
RUN cd /usr/src/Python-3.7.11 && ./configure --enable-optimizations && make altinstall

# Install python on VM
RUN yum install -y python3-pip
RUN python3.7 -m pip install mysql-connector-python python-dotenv
RUN yum install -y git

# Get the scripts from GitHub
RUN cd home && git clone https://github.com/cnrstvns/nssa-322-final-project 

# Run the monitoring script
RUN cd /home/nssa-322-final-project/monitoring && python3.7 main.py
