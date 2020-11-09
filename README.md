# 1. Установить сервер Redis
```bash
apt install redis-server
```
# 2. Протестировать Redis
```bash
redis-cli # ping
```
# 3. Скачать репозиторий 
```bash
git clone git@github.com:mebius01/django_server_HaloLab.git
```
# 4. Установить виртуальное окружение 
```bash
cd django_server_HaloLab/
virtualenv -p python3 virtualenv
```
# 5. Запустить виртуальное окружение 
```bash
. virtualenv/bin/activate
```
# 6. Установить необходимые зависимости
```bash
pip install -r requirements.txt
```
# 7 Запустить API сервер 
```bash
./manage.py runserver
```