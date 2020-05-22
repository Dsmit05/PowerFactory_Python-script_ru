import powerfactory

app = powerfactory.GetApplication()

PSs = app.GetCalcRelevantObjects('*.ElmSubstat')
lines = app.GetCalcRelevantObjects('*.ElmLne')

# Выводим все ПС с их номинальным напряжением
for PS in PSs:
    app.PrintPlain(f"{PS.loc_name} - {PS.GetAttribute('cUnom')}кВ")

# Выводим длину всех линий в проекте
sum = 0
for line in lines:
    sum = sum + line.GetAttribute('dline')
app.PrintPlain(f"{sum}")
