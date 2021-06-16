# blog-app
Source code django blog app

**setting up environment**
```
<!-- for windows -->
python -m venv .
# activate
.\Scripts\activate
# deactivate
deactivate
```
 ``` 
<!-- for linux or mac -->
python3 -m venv .
# activte
source bin/activate
# deactivate 
deactivate
```

**Install Dependencies**
```
pip install django
# to check the installed packages 
pip freeze
 ```

**Create DataBase**
```
python manage.py makemigrations
python manage.py migrate
```
 
**Create Super User**
```
python manage.py createsuperuser
```
