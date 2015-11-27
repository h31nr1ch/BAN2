#http://initd.org/psycopg/docs/install.html
sudo apt-get install python-psycopg2
sudo apt-get install python-dev libpq-dev
export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH
pip install psycopg2
sudo apt-get install postgresql postgresql-contrib
#http://initd.org/psycopg/tarballs/
wget http://initd.org/psycopg/tarballs/psycopg2-latest.tar.gz
python setup.py build
sudo python setup.py install
make
make check
sudo pip install virtualenv
export WORKON_HOME=$HOME/.virtualenvs
