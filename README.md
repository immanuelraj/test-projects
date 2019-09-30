### install postgres
$ brew install postgres
$ brew install postgresql
### start postgres
$ brew service start postgres
### create db 
$ createdb employeegb
### clone project
$ git clone https://github.com/immanuelraj/test-projects.git
$ cd test-projects/employee
### create virtualenv
$ brew install mkvirtualenv
$ mkvirtualenv --python=python3 venv
$ workon venv
### install required package
$ pip install -r ../../base.txt
