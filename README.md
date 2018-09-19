# Docker demo container 
Docker demo container based on flask.
This container runs a flask app that will display the container hostname and time.
2 environment variables can be set :
MY_VAR
USER
These will be showed when set.
The app itself listens on port 5000.
Run the container with :
    docker run --name flask-demo -p8080:5000 -e USER='Mark' -e MY_VAR='Look at me here !' flask-demo:0.1
