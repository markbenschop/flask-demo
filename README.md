# Docker demo container 
Flask based Docker demo container.  
This container runs a flask app that display the container hostname and time.  
The container can be used to demonstrate scaling out of containers or kubernets pods and loadbalancing over them.  
Each request will return a different hostname when loadbalanced properly.

An environment variables can be set :   
NAME   
This name will be displayed when this variable is set.   
This can be used to demonstrate the use variabels or a kubenetes configMap.  
Example service, deployment and configmapfiles can be found in k8s directory.

The app itself listens on port 5000.   
Run the container with e.g. :

    docker run --name flask-demo -p8080:5000 -e NAME='Mark'  flask-demo:0.16
