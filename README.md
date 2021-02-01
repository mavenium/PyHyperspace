# PyHyperspace
A free, open-source Blog CMS based on the "Django" and "Hyperspace" HTML5 theme.

![](https://img.shields.io/github/stars/mavenium/PyHyperspace) ![](https://img.shields.io/github/forks/mavenium/PyHyperspace) ![](https://img.shields.io/github/issues/mavenium/PyHyperspace) ![](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fmavenium%2FPyHyperspace)

------------
### Features

- "Blog" section to create and edit a blog
- "Skill" section to create and edit a skill
- "ContactUs" section
- "CONSTANCE" Section to manage dynamic Django settings (Blog title, Social Networks links and ...)
- Used "Django Admin" to manage all models
- Used "Hyperspace" theme by HTML5 UP
- Used "Sqlite" to create DB
- Used "CKEditor"
- Translation ready
------------
[![](https://s16.picofile.com/file/8419124942/buy_me_a_coffee.png)](https://www.blockchain.com/btc/payment_request?address=1ChqZPGhxpn6HB1WuQh55S3Mf8RydxMiFk&amount=0.00018711 "Buy me a coffee")
- You can buy me a coffee so I can turn it into more open source projects :)
------------
### Special Thanks

| Python | Django | Pycharm |
| ------------- | ------------- | ------------- |
| [![](https://s17.picofile.com/file/8418101118/python.png)](https://www.python.org "Python")  | [![](https://s17.picofile.com/file/8418100976/django.png)](https://www.djangoproject.com "Django")  | [![](https://s17.picofile.com/file/8418101034/pycharm.png)](https://www.jetbrains.com/pycharm/ "Pycharm")  |

------------
### How to install and run (GNU/Linux and Mac)
                
1. Install `git`,`python3`, `pip3`, `virtualenv` in your operating system
2. Create a development environment ready by using these commands
```
git clone https://github.com/mavenium/PyHyperspace		# clone the project
cd PyHyperspace		                                        # go to the project DIR
virtualenv -p python3 .venv		                        # Create virtualenv named .venv
source .venv/bin/activate		                        # Active virtualenv named .venv
pip install -r requirements.txt		                        # Install project requirements in .venv
python manage.py makemigrations		                        # Create migrations files
python manage.py migrate		                        # Create database tables
python manage.py collectstatic		                        # Create statics files
python manage.py runserver		                        # Run the project
```
3. Go to  `http://127.0.0.1:8000/` to use project
------------
### Notes
The Hyperspace template is released under "Creative Commons Attribution 3.0 Unported" license.