import powerfactory

app = powerfactory.GetApplication()

Script = app.GetCurrentScript()

KZ = app.GetFromStudyCase('ComShc')
line = app.GetCalcRelevantObjects(f'{Script.nameline}.ElmLne')


def resultKZ(Obj, line, MestoKZ):
    Obj.iopt_net = 0
    Obj.iopt_allbus = 0
    Obj.shcobj = line[0]
    Obj.ppro = MestoKZ
    Obj.Execute()


if len(line) > 0:
    resultKZ(KZ, line, Script.MestoKZ)
    Ikss = line[0].GetAttribute('m:Ikss:busshc')
    Iks = line[0].GetAttribute('m:Iks:busshc')
    ip = line[0].GetAttribute('m:ip:busshc')
    app.PrintPlain(
        f'Параметры КЗ для {Script.nameline}:'
        f'\nНачальный ток КЗ: {Ikss}кА, '
        f'\nПереходной ток КЗ: {Iks}кА,'
        f'\nУдарный ток КЗ: {ip}кА')
else:
    app.PrintError(f'Линия с именем {Script.nameline} не найдена в проекте')
