# Docker demo container 
Flask based Docker demo container.  
This container runs a flask app that display the container hostname and time. 
The container can be used to demonstrate scaling out of containers or kubernets pods and loadbalancing over them.  
Each request will return a different hostname when loadbalanced properly.

2 environment variables can be set :   
MY_VAR   
USER   
These will be showed when set.   
This can be used to demonstrate the use of a kubenetes configMap.

The app itself listens on port 5000.   
Run the container with :

    docker run --name flask-demo -p8080:5000 -e USER='Mark' -e MY_VAR='Look at me here !' flask-demo:0.1
