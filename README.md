# Quotes API Assignment

## Background
Our goal is to offer a customer the best policy he is eligable to by utlizing analytics, smart routing, data feedback loops, etc.
This story will focus on the Quoting step which is one part of supporting the product in our application process.
The goal is to develop a server that can fetch the right quote.

## Requirements:

A running server:
    **run server command: python django_server/manage.py runserver**\
   (requirements: django, djangorestframework, pandas)

A Working API: \
url: 'api/v1/quotation/' \
body: valid input, for example: \
        {
            “term”: 10,\
            “coverage”: 250000,\
            “age”: 25,\
            “height: “5 ft 1”,\
            “weight”: 160\
        }

HLD - 
![alt text](https://github.com/4yonatan4/quoting_server/blob/master/HLD.png?raw=true)

Be able to test and demonstrate - \
I used postman during development.\
    In addition, I wrote some tests in django_server/quotation/tests.py\
    **run tests command: python django_server/manage.py test**
