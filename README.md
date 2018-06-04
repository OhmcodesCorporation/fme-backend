# fme
FundMeDaddy


###### Setup virtual environments
    virtualenv -p python3 envFMEmaster
    cd envFMEmaster
    source bin/activate
    git clone https://github.com/NewWorldInnovations/fme.git
    cd fme
    pip install -r requirements.txt
    python manage.py runserver
    
###### Restful API links
   * /api/                     <=== namespace for api but doesn't have view/get
   * /api/token/auth/          <=== to obtain user login token
   * /api/login/               <=== login (post)
   * /api/register/            <=== register (Create)
   * /api/members/             <=== members (Retrieve) admin only
   * /events/                  <=== Create (List if Get/Create if POST)
   * /events/**<event_id>**    <=== RUD (Retrieve/Update/Delete)

###### View API
    Normal link will show you BrowsableAPI
    adding `?format=json` will give you a json raw result
   
###### Test Responses
   * Run curl in terminal
        *curl -X POST -H "Content-Type: application/json" -d '{"username":"**testuser6**","password":"**testuser69**"}' http://localhost:8000/api/token/auth/*
        
  * Sample Response
  *{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo4LCJ1c2VybmFtZSI6InRlc3R1c2VyNiIsImV4cCI6MTUyODA2NzY0NiwiZW1haWwiOiJ0ZXN0NkB0ZXN0LmNvbSJ9.vhGG53DAvpfPTtxp7wmHhd-6E7S5FHsFxIROsTP3Njk"}*
  * POST|GET Auth with token
        *curl -H "Authorization: JWT **<your_token>**" http://localhost:8000/api/events/*
  * Paste token
        *curl -H "Authorization: JWT **eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo4LCJ1c2VybmFtZSI6InRlc3R1c2VyNiIsImV4cCI6MTUyODA2NzY0NiwiZW1haWwiOiJ0ZXN0NkB0ZXN0LmNvbSJ9.vhGG53DAvpfPTtxp7wmHhd-6E7S5FHsFxIROsTP3Njk**" http://localhost:8000/api/events/*
        
        
    
