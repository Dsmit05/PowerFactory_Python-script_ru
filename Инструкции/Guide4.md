## Вводные параметры и результаты объекта ComPython

Объекты Python и  DPL лучше всего хранить в папке 'Скрипты'.
В активном окне при работе со скриптами можно задавать вводные параметры и внешние объекты.
И там же выводить результаты работы программы.

Для получения объекта используем `GetCurrentScript()`
```python
Script = app.GetCurrentScript()
```
В рабочем окне скрипта - основные опции - вводные параметры:

| Тип         | Имя          |  Значение  | Единица  | Описание | 
| ------------|--------------|------------|----------| ---------| 
|string       |nameline      |Москва-Питер|          |          |
|int          |MestoKZ       |35          |          |Расположение КЗ в процентах|     

Переменная nameline будет доступна в нашем скрипте по команде `Script.nameline`

Для добавления результатов в окно программы используйте следующие параметры:
```python
Script.IntResUnit  # Модуль
Script.IntResType  # Тип
Script.IntResDesc  # Описание
Script.IntResName  # Имя
```

Получим объект линии из вводных параметров нашего скрипта:
```python
KZ = app.GetFromStudyCase('ComShc')
line = app.GetCalcRelevantObjects(f'{Script.nameline}.ElmLne')
```

Следующая функция будет запускать расчет КЗ для нашей линии с заданым расположением КЗ:
```python
def resultKZ(Obj, line, MestoKZ):
    Obj.iopt_net = 0  # Расчет УР нелинейный, симметричный, прямая последовательность
    Obj.iopt_allbus = 0 # Место КЗ определено пользователем
    Obj.shcobj = line[0] # Выбираем линию
    Obj.ppro = MestoKZ  # Расстояние до КЗ в %
    Obj.Execute()
```

После расчета КЗ можно получить ранее не доступные данные:
```python
resultKZ(KZ, line, Script.MestoKZ)
Ikss = line[0].GetAttribute('m:Ikss:busshc')
app.PrintPlain(Ikss)  # Выведет значение начального тока КЗ
```

[Посмотреть код](https://github.com/Dsmit05/PowerFactory_Python-script_ru/blob/master/Примеры/Example4.py)