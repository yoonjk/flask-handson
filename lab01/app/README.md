
Setup some environment variables:
```
touch .env
pip freeze > requirements.txt
```
Add this in the .env file:
```
export FLASK_APP=dashapp
export FLASK_ENV=development
export DATABASE_URL=sqlite:///${PWD}/app.db
export SECRET_KEY=secret_key_change_as_you_wish_make_it_long_123
```
Then build and run in detached mode with docker-compose
```
docker-compose up -d --build
```
Check out: http://127.0.0.1:5000/dashboard