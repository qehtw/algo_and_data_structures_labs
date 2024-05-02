Iгровий сервер 88889
Код задачi: GAMSRV
Важливим фактором для багатокористувацької онлайн-гри є низька мережева затримка
вiд користувача до сервера. При цьому, пристрої в Iнтернетi спiлкуються один з
одним, використовуючи мережевi маршрути, якi проходять через низку промiжних
вузлiв-маршрутизаторiв. Кожна ланка цього маршруту має власну ненульову затримку.

• Кожен вузол мережi може виконувати одну з трьох ролей: Client, Router або
Server.
• Server може бути лише один на всю мережу.
• Усi комунiкацiї двостороннi: якщо вузол A може спiлкуватися з вузлом B,
вузол B може спiлкуватися з вузлом A з такою ж затримкою.
• Якщо iснує кiлька шляхiв вiд клiєнта до сервера, клiєнт гарантовано пiде
шляхом з найменшою сумарною затримкою (навiть якщо цей шлях пролягає
через iншого клiєнта).
• Усi затримки — сталi додатнi числа.
Для прикладу вище, затримки до клiєнтiв становлять:
• Client 1: 10 + 80 + 50 = 140 ms
• Client 2: 100 + 50 = 150 ms
• Client 3: 20 ms
Максимальною затримкою в такому випадку є 150 ms. Однак, якщо ми помiняємо
ролями вузли “Router 2” i “Server”, затримки скоротяться до 90 ms, 100 ms i 70 ms
вiдповiдно, тодi максимальна затримка буде становити 100 ms.

Ви розробляєте онлайн-гру для користувачiв зi всiєї країни, i бажаєте розмiстити
центральний iгровий сервер таким чином, щоб максимальна затримка мiж сервером
i кожним клiєнтом була мiнiмальною. В якостi сервера можна вибрати будь-який
вузол мережi, який не є клiєнтом.
Маючи iнформацiю про топологiю мережi (якi вузли з’єднанi з якими, i яка затримка
кожного з’єднання), знайдiть таке розташування сервера, яке мiнiмiзує найбiльше
значення затримки до клiєнта. Виведiть це значення затримки.
Вхiднi данi
Вхiдний файл gamsrv .in складається з M + 2 рядкiв.
• Перший рядок мiстить N i M — кiлькiсть вузлiв та з’єднань вiдповiдно.
3 ≤ N ≤ 1000, 2 ≤ M ≤ 1000
• Другий рядок мiстить перелiк цiлих чисел, роздiлених пробiлом — номери
вузлiв, якi є клiєнтами. Усi вузли в мережi нумеруються вiд 1 до N.
• Наступнi M рядкiв мiстять трiйки натуральних чисел startnode, endnode, latency
— номер початкового вузла, кiнцевого вузла та затримка для кожного з’єднання.
1 ≤ latency ≤ 109
.

Вихiднi данi
Вихiдний файл gamsrv .out повинен мiстити одне число — мiнiмальне значення найбiльшої
затримки до клiєнта (яке ми отримаємо при оптимальному розташуваннi сервера).
