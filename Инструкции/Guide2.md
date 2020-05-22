## Навигация по папкам
При написание скрипта не забываем про:
```python
import powerfactory as pf
app = pf.GetApplication()
```
Метод `GetProjectFolder()` возвращает папки проекта:
```python
Fold1=app.GetProjectFolder('equip')  # вернет Библиотеку типов оборудования
Fold2=app.GetProjectFolder('netmod') # Модель сети
```
##### Kлючевые папки:
| Атрибуты    | Описание папки               | 
| ------------|:----------------------------:| 
|demand       |Перераспределение нагрузок    |
|oplib        |Динамическая библиотека
|equip        |Библиотека типов оборудования
|cbrat        |Характеристики выключателей
|therm        |Перегрузочная способность
|ra           |Оперативные схемы ПС
|script       |Скрипты
|templ        |Шаблоны
|mvar         |Граничные кривые Реакт. Мощности (Мвар)
|qpc          |QP-Кривые
|ucc          |Кривые контроля напр. V
|netmod       |Модель сети
|netdat       |Данные сети
|outage       |Плановые отключения
|dia          |Схемы
|scen         |Оперативные Сценарии
|study        |Расчеты
|fault        |Повреждения
|ras          |Схемы устранения неисправности (RAS)
|scheme       |Варианты развития сети
|lib          |Библиотека
|blk          |Предопределенные пользователем модели
|report       |Табличные отчеты

Для перехода по уровням проекта используем:
```python
up = Fold1.GetParent()     # на уровень вверх
down = Fold1.GetContents() # на уровень вниз
```

Или получим папки и их содержимое напрямую:
```python
prj=app.GetActiveProject()
# вернем папку с названием Динамическая библиотека:
folder = prj.GetContents('Библиотека\Динамическая библиотека.intPrjfolder')[0]
folderdown = folder.GetContents() # Получим содержимое Динамической библиотеки
```

Мы можем скопировать в эту папку любой объект с помощью метода `addcopy()`:
```python
line = app.GetCalcRelevantObjects('Линия.ElmLne')
folder.AddCopy(line)
```

Для создания объектов воспользуйтесь `CreateObject("Имя класса", "Имя объекта")`:
```python
folder.CreateObject('intPrjfolder','Новая папка') #Создаст новую папку
```
Следующий код создаст папку 'Копия сети' в папке 'Данные сети'
```python
namefolder = 'Копия сети'
folder =  prj.GetContents('Модель сети\Данные сети.intPrjfolder')[0]
newfold = folder.CreateObject('intPrjfolder',namefolder)
```

Чтобы удалить объект вызовите функцию `folder.Delete()`

[Посмотреть пример](https://github.com/Dsmit05/PowerFactory_Python-script_ru/blob/master/Примеры/Example2.py)