# A Workspace for teams using gRPC
A Team workspace using gRPC as database server with methods. This project also has django app that consumes resouces from the gRPC service.

## Tools
- Uses Postgresql as database backend for the gRPC service
- gRPC server is written in python
- SQLalchemy is used as ORM

`python -m venv env`

Install all the required dependencies

`pip install -r requirements.txt`

## Testing
For testing, 
- Run `workspace_server.py` to launch gRPC service.
- Run python `.\manage.py runserver 0.0.0.0:8000` on `workstation` project folder
