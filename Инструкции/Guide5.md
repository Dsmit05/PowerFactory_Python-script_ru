## Работа с виртуальными инструментами

Получим доступ к графической панели:
```python
Desktop=app.GetFromStudyCase('SetDesktop')
```

Создадим новую страницу:
```python
NewPage=Desktop.GetPage('Имя страницы',1)
```
Вставим на нее график векторов:
```python
VectorGraph=NewPage.GetVI('ИмяГрафика','VisVec',1)
```
При работе с командой `GetVI('Имя', 'Имя класса', N)` 'Имя' не должно совпадать с другим существующим 
виртуальными инструментами(графиками), флаг `N` должен быть активирован `=1` для создания графиков

##### Классы для виртуальных инструментов:

| Значение    | Описание                         | 
| ------------|:--------------------------------:| 
|VisPlot      | График кривой|
|VisPlot2     | График кривой c 2 осями|
|VisXyplot    | График кривой c несколькими X-осями |
|VisFft       | Диаграмма БПФ|
|VisOcplot    | Время-токовая диаграмма|
|VisDraw      | Диаграмма R-X|
|VisEigen     | Диаграмма Мод|
|VisModbar    | Столбчатая диаграмма Мод|
|VisModphasor | Векторная диаграмма Мод|
|VisVec       | График векторов|
|VisHrm       | График формы волны|
|VisBdia      | Столбчатая диаграмма|
|VisPath      | Профиль напряжения|
|VisVsag      | Диаграмма просадки напряжения|
|VisPdc       | Диаграмма плотность вероятности|


Получим доступ к графической панеле
```python 
Desktop=app.GetGraphicsBoard()
```
Для получения страницы и графика вызовим функции `GetPage()` и `GetVI()` с флагом `=0`  
```python 
Page=Desktop.GetPage('Имя страницы',0)
Graph=Page.GetVI('ИмяГрафика','VisVec',0)
```

Функция `WriteWMF(имя файла)`
может использоваться для экспорта активной графической страницы в графический файл 
в формате Windows Metafile (WMF). 
```python 
app=powerfactory.GetApplication()
Desktop=app.GetGraphicsBoard()
Desktop.WriteWMF('C:\Users\.....\Desktop\result')
```

[Посмотреть пример](https://github.com/Dsmit05/PowerFactory_Python-script_ru/blob/master/Примеры/Example5.py)