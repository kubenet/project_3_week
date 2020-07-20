# project_3_week

Вам предстоит создать сайт, у которого будет "база данных" в виде JSON-файлов.

При ответе на запрос данные из "базы данных" нужно прочитать, а при сохранении пользовательских заявок данные нужно записать в "базу данных".

Вы можете использовать WTForms в этом проекте, а можете не использовать :)

1. Распишите роуты, выведите текст:

    - главной / – здесь будет главная),

    - цели /goals/<goal>/  – здесь будет цель <goal>,
    - профиля учителя /profiles/<id учителя>/ – здесь будет преподаватель <id учителя>,

    - заявки на подбор /request/ – здесь будет заявка на подбор,
    - принятой заявки на подбор /request_done/ – заявка на подбор отправлена,

    - формы бронирования /booking/<id учителя>/<день недели>/<время>/ – здесь будет форма бронирования <id учителя>,
    - принятой заявки на подбор /booking_done/   – заявка отправлена.

2. Скопируйте мок-данные в JSON-файл

Напишите скрипт, который из мок-данных в data.py сохранит их в нашу  "базу данных".

Этот скрипт должен быть отдельным .py файлом и должен быть выполнен один раз.

https://github.com/kushedow/flask-html/blob/master/Project%202/data.py

3. Скачайте или склонируйте репозиторий с шаблонами.

https://github.com/kushedow/flask-html/tree/master/Project%202

Скопируйте шаблоны в вашу папку templates:

– index.html главной,
– goal.html цели,

– profile.html профиля преподавателя,

– request.html для заявки на подбор,
– request_done.html для отправленной заявки,

– booking.html заявки на бронирование,
– booking_done.html для отправленной заявки.

4. Выведите страницу преподавателя

– изучите мок-данные,
– прочитайте  данные о преподавателе из JSON-файла,
– отредактируйте шаблон,
– проверьте результат,
– выведите табличку занятости,
– из кнопки выбора времени сделайте ссылку на страницу бронирования
     (cформируйте ссылку типа /booking/215/monday/12).

5А. Реализуйте страницу бронирования 

    – изучите шаблон,
    – выведите форму, используя данные о преподавателе, а также день и время
    – выведите данные о времени и дне недели в скрытых полях из адреса запроса (типа /booking/215/monday/12)
    – проверьте результат.

5B. Реализуйте страницу завершения бронирования

    – примите данные через booking_done,
    – сохраните данные в JSON файле booking.json. Не потеряйте заявки при записи новых!
    – выведите сообщение что все успешно,
    – проверьте результат.

6А. Реализуйте страницу запроса подбора

    – выведите форму.

6B. Реализуйте страницу завершения запроса подбора

    – примите данные через request,
    – сохраните данные в JSON файле request.json.  Не потеряйте заявки при записи новых!
    – выведите сообщение, что все успешно,
    – проверьте, что запрос записался в файле.  
   

7. Реализуйте страницу цели, например, "для переезда"

    – получите цель,
    – получите список преподавателей, отфильтруйте преподавателей по цели,
    – выведите их на странице в порядке убывания рейтинга,
    – проверьте результат.

8. Выведите главную страницу

    – получите 6 случайных преподавателей 
    – выведите их на странице,
    – добавьте ссылки на цели,
    – проверьте результат.

9. Добавьте еще одну цель

   – проверьте, что, используя цели в шаблонах, вы всегда получаете их из python- кода
   – добавьте новую цель "для программирования" преподавателям   8,9,10,11
   – проверьте, что цель корректно отображается на всех страницах
