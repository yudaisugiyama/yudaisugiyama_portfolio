```
(mysite) YudaiSugiyama@Pro % python3 manage.py shell    
Python 3.9.16 (main, Mar  8 2023, 04:29:44) 
[Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(username='admin')
>>> user.delete()
(1, {'auth.User': 1})
>>>
```# yudaisugiyama_portfolio
