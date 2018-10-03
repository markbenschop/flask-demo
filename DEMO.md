# Demo steps

# Setup a Debian 9 vm and install k8s

## Install vm
Install a debian 9 vm with an administrative user, e.g. username

## Configure the vm and install k8s
Log in to the vm with your user account.
Su to root
To configure the vm clone this git repository

   git clone https://github.com/markbenschop/debian-kubeadm.git

Run the following scripts.

To install some software and setup your user for passwordless sudo

    00-debian_setup.sh ${username}

To install docker (in a slightly older version is supported with k8s)

    01-debian_install_docker.sh

To setup k8s using kubeadm

    02-debian_setup_k8s.sh

To install prometheus into the k8s cluster run 

    03-prometheus.sh

You now have a running k8s cluster with monitoring.

# Run demo with flask-demo container

## Clone git repository
Clone this git repository
   git clone https://github.com/markbenschop/flask-demo.git

## Run


# Install prometheus
Run the 
