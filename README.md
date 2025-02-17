<h1>Документация или напоминание!?</h3>

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
<h3>Начало работы: </h3>
<p>В терминале ввести <code>cd config</code>, а затем ввести <code>python manage.py runserver</code>. <code>Ctrl+C</code> - закрывает работу локального сервера. <code>Ctrl+LMB</code> по <code>http://127.0.0.1:8000/</code>. Страницу в бразуере обновлять нажатием горячих клавиш <code>Ctrl+F5</code> после изменений, введенных в коде.</p>
<p>При изменении models.py <code>python manage.py makemigrations</code>, а затем <code>python manage.py migrate</code>. Если создан файл с некоторой функцией, работающей с БД, необходимо писать в терминал <code>python manage.py file.py</code></p>

<hr>
<h3>Приложение: </h3>
<li>https://html5book.ru/html-tags/ - документация по HTML тегам</li>
<li>https://developer.mozilla.org/ru/docs/Web/CSS - документация по CSS</li>
<li>https://docs.djangoproject.com/en/5.1/ - документация по Django</li>
