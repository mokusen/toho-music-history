# toho-music-history
It is a Django Application.You can see music infomation of toho. 

## Requirements
My environment is as follows.

|  | Version |
| :----: | :---: |
| Python | 3.6.5 |
| Django | 2.0.6 |

## Quick start
init setting:
~~~PowerShell
# Windows
> mkdir (Clone destination directory)
> cd (Clone destination directory)
> python -m (any environment name) venv
> ~\(any environment name)\scripts\activate.ps1
~~~
~~~bash
# Linux
$ mkdir (Clone destination directory)
$ cd (Clone destination directory)
$ python -m (any environment name) venv
$ source (any environment name)/bin/activate
~~~
Clone application:
~~~bash
# if current_directory then
git clone https://github.com/mokusen/toho-music-history.git
# else then
cd (Clone destination directory)
git clone https://github.com/mokusen/toho-music-history.git
~~~
install requirement:
~~~bash
pip install requirement.txt
~~~
application active:
~~~bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
~~~
## Notes
Initial information is not included in DB. 
## Licence
This Application is released under the MIT License, see LICENSE.