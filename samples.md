# Objects
	* Events
		{
		    "title": "",
		    "desc": "",
		    "edate": "",  (format: YYYY-MM-DDTHH:MM:SSZ)
		    "target_fund": "0,00", (exclude if null)
		    "status": "inc", (ong, pas, inc) (on going/passed/incoming) default: inc
		    "visibleto": "all", (all,fri,fam,acq) (All/Only Friends/Family/Acquaintances)
		    "date_created": "", (auto generated)
		}

	* Wishlist
		{
			"pk": 1, (<primary_key>)
	        "eid": 1, (<event_id>)
	        "name": "", (required)
	        "desc": "", (exclude if null)
	        "alotted": "0.00", (exclude if null)
	        "prod_link": "", (exclude if null)
	        "price": "600.00", (required)
	        "date_created": "", (auto generated)
		}

# RESPONSES
	* Events
		[
		    {
		        "pk": 1,
		        "url": "http://192.168.0.102:8000/api/events/1/",
		        "title": "Test Event 1",
		        "desc": "This is a description of my event",
		        "edate": "2018-06-21T18:00:00Z",
		        "target_fund": "5000.00",
		        "status": "inc",
		        "visibleto": "all",
		        "date_created": "2018-06-03T02:22:43Z",
		        "usrid": {
		            "username": "fme",
		            "email": "fme@fme.com",
		            "first_name": "",
		            "last_name": ""
		        },
		        "wl_count": 4,
		        "wishlist": [
		            {
		                "pk": 1,
		                "eid": 1,
		                "name": "New Cellphone",
		                "desc": "Must be tough even if i throw it to my friend",
		                "alotted": "0.00",
		                "prod_link": null,
		                "price": "600.00",
		                "date_created": "2018-06-03T02:25:51Z"
		            },
		            {
		                "pk": 2,
		                "eid": 1,
		                "name": "Wish2",
		                "desc": "test",
		                "alotted": "0.00",
		                "prod_link": null,
		                "price": "200.00",
		                "date_created": "2018-06-03T11:37:24Z"
		            },
		            {
		                "pk": 4,
		                "eid": 1,
		                "name": "Test wish curl update",
		                "desc": "This is a test for curl update",
		                "alotted": "0.00",
		                "prod_link": null,
		                "price": "50.00",
		                "date_created": "2018-06-11T02:27:38.570700Z"
		            },
		            {
		                "pk": 5,
		                "eid": 1,
		                "name": "Test wish curl 2",
		                "desc": "This is a test for curl 2",
		                "alotted": "0.00",
		                "prod_link": null,
		                "price": "450.00",
		                "date_created": "2018-06-11T02:29:13.416115Z"
		            }
		        ]
		    },
		    ....
		    .......
		]
	* Wishlist
		[
		    {
		        "pk": 1,
		        "eid": 1,
		        "name": "New Cellphone",
		        "desc": "Must be tough even if i throw it to my friend",
		        "alotted": "0.00",
		        "prod_link": null,
		        "price": "600.00",
		        "date_created": "2018-06-03T02:25:51Z"
		    },
		    ...
		    ....
		]

