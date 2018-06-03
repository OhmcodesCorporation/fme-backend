# fme
FundMeDaddy


###### Setup virtual environments
    virtualenv -p python3 envFMEmaster
    cd envFMEmaster
    source bin/activate
    git clone https://github.com/NewWorldInnovations/fme.git
    cd fme
    pip freeze -r requirements.txt
    python manage.py runserver
    
###### Restful API links
   * http://localhost:8000/api/                 <=== namespace for api but doesn't have view/get
   * http://localhost:8000/api/token/auth/      <=== to obtain user login token
   * http://localhost:8000/api/login/           <=== login (post)
   * http://localhost:8000/api/register/        <=== register (Create)
   * http://localhost:8000/api/members/         <=== members (Retrieve) admin only
   * http://localhost:8000/events/              <=== Create (List if Get/Create if POST)
   * http://localhost:8000/events/<event_id>    <=== RUD (Retrieve/Update/Delete)
   
###### Test Responses
   * Run curl in terminal
        curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser6","password":"testuser69"}' http://localhost:8000/api/token/auth/
        
  * Sample Response     
 *{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo4LCJ1c2VybmFtZSI6InRlc3R1c2VyNiIsImV4cCI6MTUyODA2NzY0NiwiZW1haWwiOiJ0ZXN0NkB0ZXN0LmNvbSJ9.vhGG53DAvpfPTtxp7wmHhd-6E7S5FHsFxIROsTP3Njk"}
  * POST|GET Auth with token
        curl -H "Authorization: JWT <your_token>" http://localhost:8000/api/events/
  ** Paste token to <your_token>
        curl -H "Authorization: JWT 
        curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo4LCJ1c2VybmFtZSI6InRlc3R1c2VyNiIsImV4cCI6MTUyODA2NzY0NiwiZW1haWwiOiJ0ZXN0NkB0ZXN0LmNvbSJ9.vhGG53DAvpfPTtxp7wmHhd-6E7S5FHsFxIROsTP3Njk" http://localhost:8000/api/events/
        
        
    
