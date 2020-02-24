# Django RESTful chat room
This is a Django application for public chat room with unauthorized access
via REST API.

####API methods:
* GET method for getting all messages with pagination by 10 messages per request.
e.g.
/api/messages/list/0 will return first 10 messages
/api/messages/list/1 will return second 10 messages
etc
* GET method for getting single message by unique identifier
e.g.
/api/messages/single/123
* POST method for creating a new message
Body accepts email and text values.
