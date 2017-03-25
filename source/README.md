## Steps to run the project

### 1. create a network to link containers
docker network create -d bridge --subnet 172.25.0.0/16 backendtest_network --attachable

### 2. run mongo (dbname=backendtest_rafal, collection=commits)
docker run --network=backendtest_network --ip=172.25.3.3 -itd --name mongo -p 27017:27018 mongo

### 3. build an image of Dockerfile
docker build -t backendtest/rafal .

### 4. run the image
docker run --network=backendtest_network --ip=172.25.3.4 -itd --name BackEndTest -p 9000:9000 backendtest/rafal

### 5. check
open urls: 
http://172.25.3.4:9000
http://172.25.3.4:9000/commits

#### POST to ADD a new document to the collection
curl -H "Content-Type: application/json" -X POST -d '{ "sha": "cb6c0c14eb58fb0660bc429cc137ef7e519ad06d", "author": "Rafal", "committer": "Rafal", "date":"2017-03-25T14:59:50Z", "message":"first test", "url": "http://test", "reviewed": false }' -i http://172.25.3.4:9000/commits/add

#### PUT to UPDATE a document (replace 58d5b39e42eb91da1e85cfc0 with the proper key)
curl -H "Content-Type: application/json" -X PUT -d '{ "reviewed": true }' -i http://172.25.3.4:9000/commits/58d5b39e42eb91da1e85cfc0

## troubleshooting
docker exec -it BackEndTest bash
### one logged in, ping other container to see if mongo is reachable
ping mongo

#### press ctrl-p ctrl-q to exit


### check if containers are connected to the network
docker network inspect backendtest_network
