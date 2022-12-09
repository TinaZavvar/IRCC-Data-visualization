# ircc-data-visualization-system  
GNG 5300 project backend  

dependency install before runserver:  
pip install django djangorestframework djangorestframework-simplejwt mysqlclient django-cors-headers django-rest-auth  
pip install -U drf-yasg  

# Rest APIs of backend  
PROD Depolyment: [swagger UI](https://irccdjangowebappprod.azurewebsites.net/swagger/)<br/>
QA Deployment: [swagger UI](https://irccdjangowebapp.azurewebsites.net/swagger/)

**login**: /login/ or /login/register/ to login/register using username + password, get all the information of the current user and a token, all the other api request the token to be send inside the request header  

**datasource**: get(GET)/update(PUT)/delete(DELETE) 1 piece of data by data_id, get all data by setting data_id = *, create(POST) a new piece of data  
TODO: create a set of data by receiving csv file from request  

**plan**: get(GET)/update(PUT)/delete(DELETE) 1 piece of plan by plan_id, get all plan by setting data_id = *, create(POST) a new piece of plan  

**subscription**: get(GET) 1 piece of subscription time by user_id, update(PUT) 1 piece of subscription time by sub_id  
# System Architecture
<img src="./resources/systemarchitecture.PNG"> 

# Authentication
<img src="./resources/authentication.PNG">

# Workflow
<img src="./resources/workflow.PNG">