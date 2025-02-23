<h1>Документация</h1>

<h3>Установка</h3>
<h4>for Windows</h4>
<p>После распаковки репозитория необходимо установить:
  <lu>
    <li>Python</li>
    <li>Pip</li>
    <li>Django</li>
  </lu>
Порядок установки:
<lu>
  <li>Устанавливаем Python с официального сайта - https://www.python.org/downloads/ ;</li>
  <li>В каталоге преокта через Terminal\cmd\bash создаем виртуальное окружение: <code>python -m venv .venv</code>;</li>
  <li>Активируем виртуальное окружение: <code>.venv\Scripts\activate.bat</code>;</li>
  <li>Затем необходимо установить систему управления пакетами Python - https://bootstrap.pypa.io/get-pip.py. После установки переходим в каталог, в котором находится система и вводим: <code>python get-pip.py</code>;</li>
  <li>Обновляем менеджер пакетов pip: <code>python -m pip install -U pip</code>;</li>
  <li>Устанавливаем в каталоге проекта фреймворк Django: <code>pip install django</code>.</li>
</lu>
  Теперь можно начинать работать!
</p>
<h5>Примечание:</h5>
<p>Удобно использовать терминал в VS Code, и писать все команды в bash терминале. Также следует предупредить, что вместо команды <code>python</code>, могут работать команды 
<lu>
  <li><code>python</code>;</li>
  <li><code>python3</code>;</li>
  <li><code>python.exe</code>;</li>
  <li><code>py</code>.</li>
</lu>
</p>
<h4>for Linux:</h4>
<p>
  Во всех дистрибутивах Python установлен по умолчанию.
  Порядок установки:
<lu>
  <li>Открываем терминал: <code>Ctrl+Alt+T</code>;</li>
  <li>Вводим <code>python --version</code>, если версия интерпретатора не актуальна, то вводим: <code>sudo apt update</code>, затем <code>sudo apt-y upgrade</code>;</li>
  <li>Устанавливаем менеджер пакетов: <code>sudo apt install -y python3-pip</code>;</li>
  <li>Обновляем менеджер пакетов: <code>sudo -H pip3 install --upgrade pip</code>;</li>
  <li>В каталоге преокта создаем виртуальное окружение: <code>python -m venv .venv</code>;</li>
  <li>Активируем виртуальное окружение: <code>source .venv/bin/activate</code>;</li>
  <li>Устанавливаем в каталоге проекта фреймворк Django: <code>pip install django</code>.</li>
</lu>
  Теперь можно начинать работать!
</p>

<hr>
<h3>Начало работы: </h3>
<p>В терминале ввести <code>cd config</code>, а затем ввести <code>python manage.py runserver</code>. <code>Ctrl+C</code> - закрывает работу локального сервера. <code>Ctrl+LMB</code> по <code>http://127.0.0.1:8000/</code>. Страницу в бразуере обновлять нажатием горячих клавиш <code>Ctrl+F5</code> после изменений, введенных в коде.</p>
<p>При изменении models.py <code>python manage.py makemigrations</code>, а затем <code>python manage.py migrate</code>. Если создан файл с некоторой функцией, работающей с БД, необходимо писать в терминал <code>python manage.py file.py</code></p>

<hr>
<h3>Комманды git частого использования: </h3>
<li><code>$ git add .</code> - добавление всех файлов в область подготовленных файлов;</li>
<li><code>$ git add example.format</code> - добавление конкретного файла в область подготовленных файлов;</li>
<li><code>$ git status</code> - проверка статуса репозитория;</li>
<li><code>$ git commit -m "Example for commit's heading"</code> - внесение изменений однострочным сообщений;</li>
<li><code>$ git commit</code> - внесение изменений через редактор;</li>
<li><code>$ git log -p</code> - просмотр истории коммитов с изменениями.</li>
<p><b>Примечание: </b>использование сопроваждается с обсуждением между всеми разработчиками</p>

<hr>
<h3>Работа с коммитом в редакторе Vim: </h3>
<li>Чтобы перейти в режим редактирования, необходимо нажать на: <code>i</code>;</li>
<li>Чтобы выйти из режима редактирования и сохранить изменения, необходимо нажать на <code>Esc</code> и набрать <code>:wqa!</code>;</li>
<li>Чтобы выйти из режима редактирования и отменить изменения, необходимо нажать на <code>Esc</code> и набрать <code>:qa!</code>.</li>
<p>Если редактор закрылся через <code>Ctrl+X</code> или <code>Ctrl+Z</code>, то необходимо ввести в терминал комманду: <code>fg</code>, тогда будет запущена последняя задача, отправленная "в фон".</p>

<hr>
<h3>Поясние структуры каталога: </h3>
<p><code>config/templates</code> - содержит html страницы<br><code>config/static</code> - содержит статические файлы<br><code>config/static/assets</code> - содержит статические изображения<br><code>config/static/styles</code> - содержит css файлы<br><code>config/static/utils</code> - содержит js функции<br><code>config/config/urls.py</code> - конфигурация URL<br><code>config/config/settings.py<br></code> - конфигурация приложения<br><code>config/app/forms.py</code> - классы приложения<br><code>config/app/models.py</code> - определение моделей<br><code>config/app/views.py</code> - логика работы приложения</p>

<hr>
<h3>Приложение: </h3>
<li>https://html5book.ru/html-tags/ - документация по HTML тегам</li>
<li>https://developer.mozilla.org/ru/docs/Web/CSS - документация по CSS</li>
<li>https://docs.djangoproject.com/en/5.1/ - документация по Django</li>
