"""
Построение векторного график в новом графическом окне проекта
Параметры короткого замыкания взяты из примера 4
"""
import powerfactory

app = powerfactory.GetApplication()

Desktop = app.GetFromStudyCase('SetDesktop')
NewPage = Desktop.GetPage('НоваяСтраница', 1)  # Создадим новую страницу
VectorGraph = NewPage.GetVI('Векторный график', 'VisVec', 1)  # Вставим на нее график векторов

# Получим объект линии:
nameline = 'Линия'
line = app.GetCalcRelevantObjects(f'{nameline}.ElmLne')

# Запустим расчет КЗ(настройки расчета коротких замыканий задаем в графическом окне):
# Место КЗ определено пользователем
KZ = app.GetFromStudyCase('ComShc')
KZ.Execute()

VectorGraph.SetAttribute('pObj', line)  # Добавляем нашу линию на график и дальше орпеделяем ее параметры для отображения
VectorGraph.SetAttribute('Var', ['m:Ikss:bus1 * exp ( j * m:phii:bus1 )'])  # Комплексная переменная
""" 
m:Ikss:bus1  Начальный ток Кз
m:phii:bus1  Фазный угол КЗ
"""
VectorGraph.SetAttribute('vColor', [2])  # Цвет Линии
VectorGraph.SetAttribute('vStyle', [1])  # Стиль Линии

app.PrintPlain(VectorGraph)
