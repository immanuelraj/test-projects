### Project Setup for Mac
* Install python
    ```sh
    brew install python3
    ```
* Install postgres
    ```sh
    brew install postgres
    brew install postgresql
    ```
* Start postgres
    ```sh
    brew service start postgres
    ```
* Create db
    ```sh
    createdb testdb
    ```
* Clone project
    ```sh
    git clone https://github.com/immanuelraj/test-project.git
    cd django-project/
    ```
* Create virtualenv
    ```sh
    brew install mkvirtualenv
    mkvirtualenv --python=/usr/local/bin/python3 test-project
    workon test-project
    ```
* Install packages
    ```sh
    pip install -r requirements.txt
    ```
* To run the project
    ```sh
    cd project
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py runserver
    ```
    
### Project Setup for Ubuntu
* Install Python
 ```sh
 Sudo apt install python3.7
 ```

* Install postgres
```sh
sudo apt install postgresql postgresql-contrib
sudo su postgres
createdb testdb
 ```
* Clone project
```sh
git clone https://github.com/immanuelraj/test-project.git
cd test-project/
 ```
* Create virtualenv
```sh
sudo apt-get install python-pip
sudo pip install virtualenv
mkdir ~/.virtualenvs
sudo pip install virtualenvwrapper
export WORKON_HOME=~/.virtualenvs
. /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv test-project
workon test-project
pip install -r requirements.txt
 ```
* To run the project
```sh
cd project
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
 ```

 ### Features

* Create Cycle automatically
    ```sh
    python manage.py purchase_cycle_auto_mode 1000
    ```

* Create Cycle with commandline input
    ```sh
    python manage.py purchase_cycle
    ```

* Create Cycle component with commandline input
    ```sh
    python manage.py create_chain
    python manage.py create_frame
    python manage.py create_handle_bar
    python manage.py create_seat
    python manage.py create_wheel
    ```



* Admin page
    ```sh
    http://127.0.0.1:8000/admin/
    ```

### Heroku Setup

* Install Heroku
    ```sh
    brew install heroku/brew/heroku
    ```
* To Login to Heroku
    ```sh
    heroku login
    ```
* Create heroku App
    ```sh
    heroku create django-test-project-app
    ```
* Install django-heroku package and add it in settings
* Add Procfile under root directory
* Add domain to allowed_host
* To push to Heroku
    ```sh
    git push heroku master
    ```
* Basic Setup
    ```sh
    heroku run python manage.py migrate
    heroku run python manage.py createsuperuser
    ```
* Add config
    ```sh
    heroku config:set SECRET_KEY='key'
    ```