## Простые команды

Для работы в среде PowerFactory импортируем модуль:
```python
import powerfactory
```
Чтобы получить доступ к окружению powerfactory необходимо добавить команду `GetApplication()`:
```python
app=powerfactory.GetApplication()
```
Выводим информацию в окно результатов PF:
```python
app.PrintPlain('Вкладка Остальное')
app.PrintError('Вкладка Ошибки')
app.PrintWarn('Вкладка Предупреждения')
app.PrintInfo('Вкладка Информация')
```
Возвращает текущего пользователя:
```python
user=app.GetCurrentUser()
```
Получение активного проекта:
```python
prj=app.GetActiveProject()
prj.GetContents() # содержимое проекта
```

Получение списка объектов:
```python
allobj = app.GetCalcRelevantObjects() #Возвращает список всех объектов проекта
lines = app.GetCalcRelevantObjects('*.ElmLne') # Возвращает список всех линий проекта
line = app.GetCalcRelevantObjects('Линия.ElmLne')[0] # конкретной линии
```

Получение и изменение атрибутов объектов:
```python
line.GetAttribute('dline') #Получаем длину линии
line.SetAttribute('dline') = 20 #Изменяем длину линии
#или так:
line.loc_name = 'Новое название' #Изменит локальное имя
```

[Посмотреть пример](https://github.com/Dsmit05/PowerFactory_Python-script_ru/blob/master/Примеры/Example1.py)