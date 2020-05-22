import powerfactory

'''
Скрипт выводит перегруженые линии в проекте
'''
app = powerfactory.GetApplication()

UR = app.GetFromStudyCase('ComLdf')
UR.iopt_net = 0  # Расчет УР нелинейный, симметричный, прямая последовательность
UR.Execute()  # Запуск расчета

lines = app.GetCalcRelevantObjects('*.ElmLne')

for line in lines:
    load = line.GetAttribute('m:loading')
    if load < 100:
        continue
    else:
        app.PrintPlain(f'Линия {line.loc_name} загружена на :{load}')
