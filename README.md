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
   * http://localhost:8000/api/
   * http://localhost:8000/events/ <=== Create (List if Get/Create if POST)
   * http://localhost:8000/events/<event_id> <=== RUD (Retrieve/Update/Delete)
    
