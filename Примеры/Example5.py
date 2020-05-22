"""
���������� ���������� ������ � ����� ����������� ���� �������
��������� ��������� ��������� ����� �� ������� 4
"""
import powerfactory

app = powerfactory.GetApplication()

Desktop = app.GetFromStudyCase('SetDesktop')
NewPage = Desktop.GetPage('�������������', 1)  # �������� ����� ��������
VectorGraph = NewPage.GetVI('��������� ������', 'VisVec', 1)  # ������� �� ��� ������ ��������

# ������� ������ �����:
nameline = '�����'
line = app.GetCalcRelevantObjects(f'{nameline}.ElmLne')

# �������� ������ ��(��������� ������� �������� ��������� ������ � ����������� ����):
# ����� �� ���������� �������������
KZ = app.GetFromStudyCase('ComShc')
KZ.Execute()

VectorGraph.SetAttribute('pObj', line)  # ��������� ���� ����� �� ������ � ������ ���������� �� ��������� ��� �����������
VectorGraph.SetAttribute('Var', ['m:Ikss:bus1 * exp ( j * m:phii:bus1 )'])  # ����������� ����������
""" 
m:Ikss:bus1  ��������� ��� ��
m:phii:bus1  ������ ���� ��
"""
VectorGraph.SetAttribute('vColor', [2])  # ���� �����
VectorGraph.SetAttribute('vStyle', [1])  # ����� �����

app.PrintPlain(VectorGraph)
