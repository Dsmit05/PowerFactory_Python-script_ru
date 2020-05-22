## ������� ��������� � ���������� ������� ComPython

������� Python �  DPL ����� ����� ������� � ����� '�������'.
� �������� ���� ��� ������ �� ��������� ����� �������� ������� ��������� � ������� �������.
� ��� �� �������� ���������� ������ ���������.

��� ��������� ������� ���������� `GetCurrentScript()`
```python
Script = app.GetCurrentScript()
```
� ������� ���� ������� - �������� ����� - ������� ���������:

| ���         | ���          |  ��������  | �������  | �������� | 
| ------------|--------------|------------|----------| ---------| 
|string       |nameline      |������-�����|          |          |
|int          |MestoKZ       |35          |          |������������ �� � ���������|     

���������� nameline ����� �������� � ����� ������� �� ������� `Script.nameline`

��� ���������� ����������� � ���� ��������� ����������� ��������� ���������:
```python
Script.IntResUnit  # ������
Script.IntResType  # ���
Script.IntResDesc  # ��������
Script.IntResName  # ���
```

������� ������ ����� �� ������� ���������� ������ �������:
```python
KZ = app.GetFromStudyCase('ComShc')
line = app.GetCalcRelevantObjects(f'{Script.nameline}.ElmLne')
```

��������� ������� ����� ��������� ������ �� ��� ����� ����� � ������� ������������� ��:
```python
def resultKZ(Obj, line, MestoKZ):
    Obj.iopt_net = 0  # ������ �� ����������, ������������, ������ ������������������
    Obj.iopt_allbus = 0 # ����� �� ���������� �������������
    Obj.shcobj = line[0] # �������� �����
    Obj.ppro = MestoKZ  # ���������� �� �� � %
    Obj.Execute()
```

����� ������� �� ����� �������� ����� �� ��������� ������:
```python
resultKZ(KZ, line, Script.MestoKZ)
Ikss = line[0].GetAttribute('m:Ikss:busshc')
app.PrintPlain(Ikss)  # ������� �������� ���������� ���� ��
```

[���������� ���](https://github.com/Dsmit05/PowerFactory_Python-script_ru/blob/master/�������/Example4.py)