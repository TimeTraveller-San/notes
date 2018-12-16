# Web server, WSGI, Frameworks
A simple note to self regarding these which often used to confuse me
WSGI: Web server gateway interface example gunicorn, werkzeug)

## Here are some things to remember:
- Flask is not a webserver
- Flask is just a framework
- During development, flask uses werkzeug WSGI

## Web framework - WSGI - Web server
I've created this image using draw.io it says a thousand words

![](https://i.imgur.com/EjRkZYu.png)

- Note: WSGI is just a set a rules to help unify and standardize how Python applications communicate with web servers.
- Note: Flask is often used with gunicorn because inbuilt flask WSGI (werkzeug) isn't good enough for production use
- WSGI has two sides: 
	1. Server side: To communicate to nginx or apaceh etc
	2. Framework side: A python callable written in some framework like flask or django etc

