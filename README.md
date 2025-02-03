### About the App

App is live at this link: 

This is a Python based app which leverages Flask for web serving. It gives the user details about any given IP address. The web app leverages [IPQuery Docs API](https://ipquery.gitbook.io/ipquery-docs) to fetch the IP details. 

Following are a few snapshots:

Landing page:

<img width="982" alt="image" src="https://github.com/user-attachments/assets/29fdb97c-d4a2-4123-b46c-8db9d380a022" />

IP query result page:

<img width="1466" alt="image" src="https://github.com/user-attachments/assets/7fd75572-24fa-4d11-b8c6-cd33c91a2319" />


***

#### Resources Used 
1. Documentation of the API used to fetch IP details: https://ipquery.gitbook.io/ipquery-docs
2. Sample JSON load retuned by the API for successful query: https://api.ipquery.io/1.1.1.1?format=json
3. Web service used to host: https://dashboard.render.com/

 
*** 

#### Decription of the file tree

* templates - contains `index.html` (landing page), `ip.html` (ip details page), and `invalid.html` (query failed page). 
* static/styles - contains styles.css
* requirements.txt - conatins the requirements for deplying the application
* ip.py - contains the `get_ip_details()` and `get_default_ip_details()` functions which perform the API call and return the resultant JSON object
* server.py - contains the flask app routing and serving logic, along with a few edge cases. It performs the end-to-end logic of the app, from fetching the ip address from the input to rendering the corresponding html file based on the query result.
* init.sh - first steps used to setup the project during local development

*** 
