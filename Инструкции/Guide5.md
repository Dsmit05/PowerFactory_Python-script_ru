## ������ � ������������ �������������

������� ������ � ����������� ������:
```python
Desktop=app.GetFromStudyCase('SetDesktop')
```

�������� ����� ��������:
```python
NewPage=Desktop.GetPage('��� ��������',1)
```
������� �� ��� ������ ��������:
```python
VectorGraph=NewPage.GetVI('����������','VisVec',1)
```
��� ������ � �������� `GetVI('���', '��� ������', N)` '���' �� ������ ��������� � ������ ������������ 
������������ �������������(���������), ���� `N` ������ ���� ����������� `=1` ��� �������� ��������

##### ������ ��� ����������� ������������:

| ��������    | ��������                         | 
| ------------|:--------------------------------:| 
|VisPlot      | ������ ������|
|VisPlot2     | ������ ������ c 2 �����|
|VisXyplot    | ������ ������ c ����������� X-����� |
|VisFft       | ��������� ���|
|VisOcplot    | �����-������� ���������|
|VisDraw      | ��������� R-X|
|VisEigen     | ��������� ���|
|VisModbar    | ���������� ��������� ���|
|VisModphasor | ��������� ��������� ���|
|VisVec       | ������ ��������|
|VisHrm       | ������ ����� �����|
|VisBdia      | ���������� ���������|
|VisPath      | ������� ����������|
|VisVsag      | ��������� �������� ����������|
|VisPdc       | ��������� ��������� �����������|


������� ������ � ����������� ������
```python 
Desktop=app.GetGraphicsBoard()
```
��� ��������� �������� � ������� ������� ������� `GetPage()` � `GetVI()` � ������ `=0`  
```python 
Page=Desktop.GetPage('��� ��������',0)
Graph=Page.GetVI('����������','VisVec',0)
```

������� `WriteWMF(��� �����)`
����� �������������� ��� �������� �������� ����������� �������� � ����������� ���� 
� ������� Windows Metafile (WMF). 
```python 
app=powerfactory.GetApplication()
Desktop=app.GetGraphicsBoard()
Desktop.WriteWMF('C:\Users\.....\Desktop\result')
```

[���������� ������](https://github.com/Dsmit05/PowerFactory_Python-script_ru/blob/master/�������/Example5.py)