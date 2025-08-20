docker build -t mongo-app .
docker tag mongo-app username/mongo-app:v1
 docker push username/mongo-app:v1

 oc delete all --all -n  <namespace>

 oc new-app mongodb/mongodb-community-server:latest --name mongodb
 oc new-app --name mongo-app --docker-image=docker.io/<username>/mongo-app:v1 -e HOST=mongodb

 oc expose service/mongo-app
 oc get route -l app=mongo-app