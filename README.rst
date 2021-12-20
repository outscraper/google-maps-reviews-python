Outscraper SDK in Python
========================

Python SDK that allows fetching Google Maps reviews from any place.
Fetch reviews from any business on Google Maps without limitations.

`API
Docs <https://app.outscraper.com/api-docs#tag/Google-Maps/paths/~1maps~1reviews-v3/get>`__

Installation
------------

Python 3+

.. code:: bash

   pip install google-maps-reviews

`Link to the python package
page <https://pypi.org/project/google-maps-reviews/>`__

Initialization
--------------

.. code:: python

   from google_maps_reviews import ReviewsClient

   client = ReviewsClient(api_key='SECRET_API_KEY')

Fetch Google Maps Reviews
-------------------------

.. code:: python

   # Get reviews from the place by name and lcoation
   results = client.get_reviews('Trump Tower, NY, USA', reviewsLimit=10, language='en')

   # Get reviews from many places found by search query
   results = client.get_reviews('Memphis Seoul brooklyn usa', reviewsLimit=10, limit=10, language='en')

   # Get reviews from the place by google id
   results = client.get_reviews('0x89c258faf553cfad:0x8e9cfc7444d8f876', reviewsLimit=20, language='en')

   # Get reviews from the place by URL
   results = client.get_reviews('https://www.google.com/maps/place/Trump+Tower/@40.7608106,-73.983412,15z/data=!3m1!5s0x89c259a1e735d943:0xb63f84c661f84258!4m9!1m2!2m1!1sTrump+Tower!3m5!1s0x89c258faf553cfad:0x8e9cfc7444d8f876!8m2!3d40.7624284!4d-73.973794!15sCgtUcnVtcCBUb3dlcloNIgt0cnVtcCB0b3dlcpIBCGxhbmRtYXJr', reviewsLimit=20, language='en')

   # Get only new reviews during last 24 hours
   from datetime import datetime, timedelta
   yesterday_timestamp = int((datetime.now() - timedelta(1)).timestamp())

   results = client.get_reviews(
       '0x89c258faf553cfad:0x8e9cfc7444d8f876', sort='newest', cutoff=yesterday_timestamp, reviewsLimit=100, language='en')

Results Demo
------------

.. code:: json

   {
     "name": "Memphis Seoul",
     "address": "569 Lincoln Pl, Brooklyn, NY 11238, \\u0421\\u043f\\u043e\\u043b\\u0443\\u0447\\u0435\\u043d\\u0456 \\u0428\\u0442\\u0430\\u0442\\u0438",
     "address_street": "569 Lincoln Pl",
     "address_borough": "\\u041a\\u0440\\u0430\\u0443\\u043d-\\u0413\\u0430\\u0439\\u0442\\u0441",
     "address_city": "Brooklyn",
     "time_zone": "America/New_York",
     "type": "\\u0420\\u0435\\u0441\\u0442\\u043e\\u0440\\u0430\\u043d",
     "types": "\\u0420\\u0435\\u0441\\u0442\\u043e\\u0440\\u0430\\u043d",
     "postal_code": "11238",
     "latitude": 40.6717258,
     "longitude": -73.9579098,
     "phone": "+1 347-349-2561",
     "rating": 3.9,
     "reviews": 32,
     "site": "http://www.getmemphisseoul.com/",
     "photos_count": 77,
     "google_id": "0x89c25bb5950fc305:0x330a88bf1482581d",
     "reviews_link": "https://www.google.com/search?q=Memphis+Seoul,+569+Lincoln+Pl,+Brooklyn,+NY+11238,+%D0%A1%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D1%96+%D0%A8%D1%82%D0%B0%D1%82%D0%B8&ludocid=3677902399965648925#lrd=0x89c25bb5950fc305:0x330a88bf1482581d,1",
     "reviews_id": "3677902399965648925",
     "photo": "https://lh5.googleusercontent.com/p/X_6-QqMphC_ctqs3bHSqFg",
     "working_hours": "\\u0432\\u0456\\u0432\\u0442\\u043e\\u0440\\u043e\\u043a: 16:00\\u201322:00 | \\u0441\\u0435\\u0440\\u0435\\u0434\\u0430: 16:00\\u201322:00 | \\u0447\\u0435\\u0442\\u0432\\u0435\\u0440: 16:00\\u201322:00 | \\u043f\\u02bc\\u044f\\u0442\\u043d\\u0438\\u0446\\u044f: 16:00\\u201322:00 | \\u0441\\u0443\\u0431\\u043e\\u0442\\u0430: 16:00\\u201322:00 | \\u043d\\u0435\\u0434\\u0456\\u043b\\u044f: 16:00\\u201322:00 | \\u043f\\u043e\\u043d\\u0435\\u0434\\u0456\\u043b\\u043e\\u043a: 16:00\\u201322:00",
     "reviews_per_score": "1: 6, 2: 0, 3: 4, 4: 3, 5: 19",
     "verified": true,
     "reserving_table_link": null,
     "booking_appointment_link": null,
     "owner_id": "100347822687163365487",
     "owner_link": "https://www.google.com/maps/contrib/100347822687163365487",
     "reviews_data": [
       {
         "google_id": "0x89c25bb5950fc305:0x330a88bf1482581d",
         "autor_link": "https://www.google.com/maps/contrib/112314095435657473333?hl=en-US",
         "autor_name": "Eliott Levy",
         "autor_id": "112314095435657473333",
         "review_text": "Very good local comfort fusion food ! \\nKimchi coleslaw !! Such an amazing idea !",
         "review_link": "https://www.google.com/maps/reviews/data=!4m5!14m4!1m3!1m2!1s112314095435657473333!2s0x0:0x330a88bf1482581d?hl=en-US",
         "review_rating": 5,
         "review_timestamp": 1560692128,
         "review_datetime_utc": "06/16/2019 13:35:28",
         "review_likes": null
       },
       {
         "google_id": "0x89c25bb5950fc305:0x330a88bf1482581d",
         "autor_link": "https://www.google.com/maps/contrib/106144075337788507031?hl=en-US",
         "autor_name": "fenwar1",
         "autor_id": "106144075337788507031",
         "review_text": "Great wings with several kinds of hot sauce. The mac and cheese ramen is excellent.\\nUPDATE:\\nReturned later to try the meatloaf slider, a thick meaty slice  topped with slaw and a fantastic sauce- delicious. \\nConsider me a regular.\\ud83d\\udc4d",
         "review_link": "https://www.google.com/maps/reviews/data=!4m5!14m4!1m3!1m2!1s106144075337788507031!2s0x0:0x330a88bf1482581d?hl=en-US",
         "review_rating": 5,
         "review_timestamp": 1571100055,
         "review_datetime_utc": "10/15/2019 00:40:55",
         "review_likes": null
       },
       ...
     ]
   }
