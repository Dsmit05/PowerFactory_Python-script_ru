## ��������� �� ������
��� ��������� ������� �� �������� ���:
```python
import powerfactory as pf
app = pf.GetApplication()
```
����� `GetProjectFolder()` ���������� ����� �������:
```python
Fold1=app.GetProjectFolder('equip')  # ������ ���������� ����� ������������
Fold2=app.GetProjectFolder('netmod') # ������ ����
```
##### K������� �����:
| ��������    | �������� �����               | 
| ------------|:----------------------------:| 
|demand       |����������������� ��������    |
|oplib        |������������ ����������
|equip        |���������� ����� ������������
|cbrat        |�������������� ������������
|therm        |������������� �����������
|ra           |����������� ����� ��
|script       |�������
|templ        |�������
|mvar         |��������� ������ �����. �������� (����)
|qpc          |QP-������
|ucc          |������ �������� ����. V
|netmod       |������ ����
|netdat       |������ ����
|outage       |�������� ����������
|dia          |�����
|scen         |����������� ��������
|study        |�������
|fault        |�����������
|ras          |����� ���������� ������������� (RAS)
|scheme       |�������� �������� ����
|lib          |����������
|blk          |���������������� ������������� ������
|report       |��������� ������

��� �������� �� ������� ������� ����������:
```python
up = Fold1.GetParent()     # �� ������� �����
down = Fold1.GetContents() # �� ������� ����
```

��� ������� ����� � �� ���������� ��������:
```python
prj=app.GetActiveProject()
# ������ ����� � ��������� ������������ ����������:
folder = prj.GetContents('����������\������������ ����������.intPrjfolder')[0]
folderdown = folder.GetContents() # ������� ���������� ������������ ����������
```

�� ����� ����������� � ��� ����� ����� ������ � ������� ������ `addcopy()`:
```python
line = app.GetCalcRelevantObjects('�����.ElmLne')
folder.AddCopy(line)
```

��� �������� �������� �������������� `CreateObject("��� ������", "��� �������")`:
```python
folder.CreateObject('intPrjfolder','����� �����') #������� ����� �����
```
��������� ��� ������� ����� '����� ����' � ����� '������ ����'
```python
namefolder = '����� ����'
folder =  prj.GetContents('������ ����\������ ����.intPrjfolder')[0]
newfold = folder.CreateObject('intPrjfolder',namefolder)
```

����� ������� ������ �������� ������� `folder.Delete()`

[���������� ������](https://github.com/Dsmit05/PowerFactory_Python-script_ru/blob/master/�������/Example2.py)