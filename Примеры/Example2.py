import powerfactory

app = powerfactory.GetApplication()
prj = app.GetActiveProject()

folder = prj.GetContents('Модель сети\Данные сети\Копия сети.intPrjfolder')[0]
network = prj.GetContents('Модель сети\Данные сети\Сеть.ElmNet')[0]

# Чтобы скопировать сеть её сначала нужно деактивировать:
network.Deactivate()

# Создадим копию нашей текущей сети в папке 'Копия сети'
newnetwork = folder.AddCopy(network)

# И активируем её
newnetwork.Activate()
