# Where_to_go

Этот проект показывает интересные места по миру с помощью яндекс афиши, основан на этом [js коде](https://github.com/devmanorg/where-to-go-frontend).     
      
[Ссылка на сайт](https://herypank.pythonanywhere.com/).  Места добавляются через [django-admin](https://herypank.pythonanywhere.com/admin).     
      
![](https://i.imgur.com/x3nt2d6.jpg)      
      
## Подготовка к запуску    
Уставновить [Python 3+](https://www.python.org/downloads/)    

Установить, создать и активировать виртуальное окружение.
```
pip3 install virtualenv
python3 -m venv env
source env/bin/activate
```
Установить библиотеки командой.  
```
pip3 install -r requirements.txt  
``` 
    
## Запуск кода  
```
python3 manage.py runserver
```
## Добавление мест с помощью кода
```
python3 manage.py load_place http://адрес/файла.json
```
[Данные, которые можете загрузить](https://github.com/devmanorg/where-to-go-places).    
     
Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
