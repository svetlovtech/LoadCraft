(echo "Y") | sudo apt-get install python3-venv
python3 -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('load', 'loadcraft@testserver.io', 'craft')" | python manage.py shell
nohup python3 manage.py runserver 0.0.0.0:8000 > django-test-server-log.txt &
tail -f django-test-server-log.txt
