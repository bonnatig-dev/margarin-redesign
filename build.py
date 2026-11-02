import re,html
idx=open('index.html').read()
HEAD=re.search(r'<header class="top">.*?</header>',idx,re.S).group(0).replace('<header class="top">','<header class="top inner">')
CONTACTS='<div class="wrap hcontacts"><a class="pill glass" href="tel:+375173013015">+375 (17) 301-30-15 / приёмная</a><a class="pill glass" href="tel:+375173748625">+375 (17) 374-86-25 / отдел продаж</a><a class="pill glass" href="mailto:mail@margarin.by">mail@margarin.by</a><span class="pill glass">Минск, ул. Козлова, 27</span></div>'
FOOT=re.search(r'<footer.*?</footer>',idx,re.S).group(0)
HEADHTML=re.search(r'<head>.*?</head>',idx,re.S).group(0)
def page(fn,title,crumbs,body,lead=""):
  cr='<nav class="crumbs" aria-label="Навигация"><a class="pill glass" href="index.html">Главная</a>'+''.join(f'<a class="pill glass" href="{u}">{t}</a>' if u else f'<span class="pill line" aria-current="page">{t}</span>' for t,u in crumbs)+'</nav>'
  h=HEADHTML.replace('<title>Золотая капля / Минский маргариновый завод</title>',f'<title>{re.sub("<[^>]+>","",title)} / Золотая капля</title>')
  out=f'''<!doctype html><html lang="ru">{h}<body class="inner-page">
<div class="grain" aria-hidden="true"></div>
{HEAD}
{CONTACTS}
<section class="phead"><div class="wrap">{cr}<h1 class="grad ptitle">{title}</h1>{f'<p class="plead">{lead}</p>' if lead else ''}</div></section>
<main>{body}</main>
{FOOT}
<script src="main.js"></script></body></html>'''
  open(fn,'w').write(out)

CATS=[("Майонез","majonez.html","pack-provansal.jpg","Классический майонез на яичном желтке и растительном масле. Без ГМО, искусственных ароматизаторов и красителей."),
("Соус","","pack-vegan.png","Майонезные соусы для холодных и горячих блюд: «Веган», «Бургер», «Тар-тар», «Грибной», «Сливочно-чесночный»."),
("Кетчуп","","pack-bbq.png","Томатный, классический, шашлычный, барбекю и острый с красным перцем."),
("Хрен","","pack-hren.jpg","Хрен столовый «Белорусский»: классический и со свёклой."),
("Горчица","","pack-gorchica.jpg","«Европейская», «Нежная», «Аппетитная»."),
("Маргарин","","pack-margarin.png","Для выпечки дома и для производств: фасованный и в ящиках по 20 кг."),
("Спред","","spred.jpg","Спред растительно-жировой «Сливочный» с Омега-3 и провитамином А."),
("Масло растительное","","pack-oil.png","Рапсовое, подсолнечно-кукурузное, подсолнечно-оливковое, рапсово-подсолнечное."),
("Томатная группа","","pack-tomat.png","Соусы томатные «Краснодарский», «Минский», «Томатный классический» и паста томатная."),
("Гастрономические соусы","","pack-teriyaki.jpg","Терияки для обжарки, кунжутный, барбекю."),
("Жир кулинарный и кондитерский","","","Жиры для пищевых производств и кондитерских цехов.")]
rows=""
for i,(n,u,img,d) in enumerate(CATS):
  link=u or "majonez.html"
  note='' if u else '<small class="tmpl">Открывается шаблон категории на примере «Майонеза»</small>'
  im=f'<img src="assets/{img}" alt="" loading="lazy">' if img else ''
  rows+=f'<a class="crow{" noimg" if not img else ""}" href="{link}"><span class="cnum">{i+1:02d}</span><span class="cname">{n}</span><span class="cdesc">{d}{note}</span>{im}</a>'
page("catalog.html","Продукция",[("Продукция",None)],f'<section class="sec"><div class="wrap clist">{rows}</div></section>',
 "Больше 80 наименований под марками «Золотая капля» и «ВкуSноВ». Выберите категорию: внутри фасовка, количество в упаковке и сроки хранения.")

P=[("Розовый майонез","pack-pink.png",[("твист-офф 300 г","15 шт.","от 0 до 10 °C","120 сут.")],"Содержит сок из красной свеклы / экологичная многооборотная упаковка"),
("Майонез «С трюфелем»","pack-truffle.jpg",[("твист-офф 300 г","15 шт.","от 0 до 10 °C","120 сут.")],"Содержит пасту из трюфелей / экологичная многооборотная упаковка"),
("Майонез «Провансаль Премиум»","pack-provansal.jpg",[("твист-офф 300 г","15 шт.","от 0 до 10 °C","120 сут.")],"71% жирности / содержит яичный желток / 100% натуральный состав","product-provansal-premium.html"),
("Майонез «Провансаль» ТМ «ВкуSноВ»","pack-vkusnov.jpg",[("ПЭТ пакет 600 г","20 шт.","от 0 до 10 °C","110 сут.")],"Сделан из свежего растительного масла высшего качества"),
("Майонез «Провансаль» с лимонным соком","",[("DOY-PACK 230 г","13 шт.","от 0 до 10 °C","120 сут.")],"Без ГМО / содержит провитамин А / с йодированной солью"),
("Майонез «Провансаль с перепелиными яйцами»","",[("DOY-PACK 230 г","13 шт.","от 0 до 10 °C","120 сут.")],"Без ГМО / содержит провитамин А / с йодированной солью"),
("Соус майонезный «Провансаль Салатный»","",[("п/эт пакет 180 г","66 шт.","от 0 до 10 °C","120 сут."),("п/эт пакет 360 г","36 шт.","от 0 до 10 °C","120 сут."),("флакон 800 г","8 шт.","от 0 до 10 °C","30 сут.")],"Жир 20% / без ГМО / с йодированной солью"),
("Майонез «Школьный»","",[("п/эт пакет 200 г","60 шт.","от 0 до 6 °C","60 сут."),("п/эт пакет 400 г","30 шт.","от 0 до 6 °C","60 сут.")],"Жир 50% / без ГМО / с йодированной солью"),
("Майонез «Провансаль Оливковый»","",[("DOY-PACK 230 г","13 шт.","от 0 до 10 °C","120 сут.")],"Жир 50% / без ГМО / с йодированной солью")]
def table(r): return '<table class="ptable"><thead><tr><th>Фасовка</th><th>В упаковке</th><th>Хранение</th><th>Срок годности</th></tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td data-l="{l}">{c}</td>' for l,c in zip(["Фасовка","В упаковке","Хранение","Срок"],x))+'</tr>' for x in r)+'</tbody></table>'
feat=""; plain=""
for p in P:
  n,img,r,d=p[:4];u=p[4] if len(p)>4 else None
  t=f'<a href="{u}">{n} →</a>' if u else n
  if img: feat+=f'<article class="prow"><img src="assets/{img}" alt="{html.escape(n)}" loading="lazy"><div><h3>{t}</h3><p class="pmeta">{d}</p><details class="spec-d" open><summary class="pill line">Фасовка и хранение</summary>{table(r)}</details></div></article>'
  else: plain+=f'<article class="prow text"><div><h3>{t}</h3><p class="pmeta">{d}</p></div><details class="spec-d" open><summary class="pill line">Фасовка и хранение</summary>{table(r)}</details></article>'
page("majonez.html","Майонез",[("Продукция","catalog.html"),("Майонез",None)],
 f'<section class="sec"><div class="wrap"><div class="plist">{feat}</div><h2 class="sub">Ещё в категории</h2><div class="plist">{plain}</div><p class="gap-note">Фото этих позиций на текущем сайте нет, поэтому здесь только характеристики.</p></div></section>',
 "Классический продукт из натурального яичного желтка и растительного масла высшего качества. Подходит для маринада к мясу и птице, соуса к готовым блюдам и заправки салатов.")

page("product-provansal-premium.html","Майонез «Провансаль Премиум»",[("Продукция","catalog.html"),("Майонез","majonez.html"),("Провансаль Премиум",None)],
 f'''<section class="sec"><div class="wrap prod">
 <figure class="prod-ph"><img src="assets/pack-provansal.jpg" alt="Майонез «Провансаль Премиум»"></figure>
 <div class="prod-tx"><ul class="facts"><li><b>71%</b>жирности</li><li><b>300 г</b>твист-офф</li><li><b>120</b>суток хранения</li></ul>
 <ul class="tags"><li class="pill line">Без искусственных ароматизаторов и красителей</li><li class="pill line">100% натуральный состав</li><li class="pill line">Содержит яичный желток</li><li class="pill line">Многооборотная упаковка</li></ul>
 <details class="spec-d" open><summary class="pill line">Фасовка и хранение</summary>{table([("твист-офф 300 г","15 шт.","от 0 до 10 °C вкл.","120 суток")])}</details>
 <div class="btns"><a class="pill solid" href="partners.html#form">Запросить условия поставки</a><a class="pill line" href="majonez.html">Весь майонез</a></div></div></div></section>''',
 "Майонез с домашним вкусом в стеклянной банке.")

REC=[("Медовик с клубникой на маргарине «Сливочный»","recipe-medovik.html","medovik.jpg"),("Чебуреки на рапсовом масле","","cheburek.jpg"),("Блинчики на молоке с мороженым","",""),("Кабачки в кляре на масле рапсовом","",""),("Драники","",""),("Макароны с сосисками","",""),("Медовик с цедрой апельсина","",""),("Паста «Карбонара»","",""),("Апельсиновый пирог","","")]
big="".join(f'<a class="rbig" href="{u or "recipe-medovik.html"}"><img src="assets/{i}" alt="" loading="lazy"><span>{n}</span></a>' for n,u,i in REC if i)
lst="".join(f'<li><a href="recipe-medovik.html">{n}</a></li>' for n,u,i in REC if not i)
page("recipes.html","Рецепты",[("Рецепты",None)],f'<section class="sec"><div class="wrap rlay"><div class="rbigs">{big}</div><div><h2 class="sub" style="margin-top:0">Все рецепты</h2><ul class="rlist">{lst}</ul><p class="gap-note">Фото к этим рецептам в демо нет. Ссылки ведут на шаблон страницы рецепта.</p></div></div></section>',
 "Домашние блюда с продуктами «Золотой капли»: выпечка, жарка, соусы.")

ING=[("Маргарин «Сливочный» ТМ «Золотая капля»","100 г"),("Мука высший сорт","4–5 стаканов"),("Яйца","2 шт."),("Мёд","4–5 ст. л. с горкой"),("Сахар","40 г"),("Ванильный сахар","1 пакетик"),("Соль","щепотка"),("Сода","0,5 ч. л."),("Сгущёнка (варёная)","1 банка"),("Масло сливочное","100 г"),("Клубника","200–300 г")]
ST=["Яйца, сахар, ваниль, маргарин и мёд смешайте и поставьте на водяную баню, пока ингредиенты не растворятся. Добавьте соду, постоянно помешивайте.","Снимите с бани и постепенно добавляйте муку, пока тесто не станет вымешиваться.","Хорошо замесите тесто на коврике и разрежьте на 7 частей.","Каждую часть раскатайте в круг (по размеру тарелки) и выпекайте по очереди до золотого цвета.","Крем: сварите сгущёнку, немного остудите и смешайте с мягким сливочным маслом.","Смажьте каждый корж кремом. Обрезки измельчите и обсыпьте торт, сверху украсьте клубникой."]
page("recipe-medovik.html","Медовик с клубникой на маргарине «Сливочный»",[("Рецепты","recipes.html"),("Медовик",None)],
 f'''<section class="sec"><div class="wrap rec">
 <div class="rec-l"><figure class="rec-ph"><img src="assets/medovik.jpg" alt="Медовик с клубникой"></figure>
 <h2 class="sub">Приготовление</h2><ol class="steps">{"".join(f"<li>{s}</li>" for s in ST)}</ol></div>
 <aside class="rec-r"><div class="ingbox glass"><h2 class="sub" style="margin-top:0">Ингредиенты</h2><ul>{"".join(f"<li><span>{a}</span><b>{b}</b></li>" for a,b in ING)}</ul></div>
 <a class="prodlink" href="catalog.html"><img src="assets/pack-margarin.png" alt=""><span>Маргарин в каталоге →</span></a></aside></div></section>''')

C15=["Россия","Эстония","Латвия","Литва","Польша","Украина","Сербия","Нидерланды","Дания","Китай","Сингапур","Грузия","Армения","Азербайджан","Саудовская Аравия"]
page("partners.html","Партнёрам",[("Партнёрам",None)],f'''
<section class="sec"><div class="wrap chan">
 <div class="ch"><p class="kick">Беларусь</p><h3>Торговым сетям и оптовикам</h3><p>Приглашаем торговые сети, оптовую и розничную торговлю, ИП и госучреждения. Оплата: предоплата, возможно рассмотрение отсрочки. Доставка по Беларуси транспортом предприятия или самовывоз со складов отделов прямых продаж.</p><p class="cont"><a href="tel:+375173748625">+375 (17) 374-86-25</a> / <a href="mailto:sales@margarin.by">sales@margarin.by</a></p></div>
 <div class="ch"><p class="kick">Производствам</p><h3>Кондитерам и HoReCa</h3><p>Маргарины весовые и фасованные, жиры кулинарные и кондитерские. Маргарин в крупноблочной упаковке 20 кг.</p><p class="cont"><a href="catalog.html">Смотреть продукцию →</a></p></div>
 <div class="ch"><p class="kick">Экспорт</p><h3>Зарубежным партнёрам</h3><p>Условия обсуждаем с каждым партнёром отдельно. Отвечает сектор внешнеэкономической деятельности.</p><p class="cont"><a href="tel:+375173975011">+375 (17) 397-50-11</a> / <a href="mailto:export@margarin.by">export@margarin.by</a></p></div>
</div></section>
<section class="sec alt"><div class="wrap docs"><div><h2 class="sub" style="margin-top:0">Для договора поставки нужны</h2><ol class="steps"><li>Свидетельство о государственной регистрации</li><li>Доверенность на право заключения договора</li><li>Устав (при необходимости)</li><li>Банковские реквизиты</li></ol></div>
<div><h2 class="sub" style="margin-top:0">Поставляем в 15 стран</h2><ul class="countries">{"".join(f"<li>{c}</li>" for c in C15)}</ul></div></div></section>
<section class="sec" id="form"><div class="wrap formlay"><div><h2>Заявка</h2><p class="plead">Выберите тему, оставьте контакты. В рабочей версии заявка уйдёт в отдел продаж.</p></div>
<form class="rform" onsubmit="event.preventDefault();this.querySelector('.fnote').hidden=false">
<label class="full">Тема<select><option>Партнёрство</option><option>Прайс-лист</option><option>Экспорт</option><option>Другое</option></select></label>
<label>Компания<input></label><label>Имя<input required></label><label>Телефон<input type="tel" required></label><label>Email<input type="email"></label>
<label class="full">Комментарий<textarea rows="3"></textarea></label>
<button class="pill solid full">Отправить</button><p class="fnote full" hidden>Это демо-версия: форма никуда не отправляется. Пишите на sales@margarin.by.</p></form></div></section>''',
 "Работаем с сетями, оптовиками, производствами и импортёрами. Условия обсуждаем с каждым партнёром отдельно.")

HIS=[("1951","Выпущена первая пачка маргарина. Через год объём производства маргариновой продукции составил 8 000 тонн."),("1953","Выпущена первая пачка майонеза. Закуплены линии по выпуску маргарина в мелкой расфасовке («Джонсон», Англия) и линия непрерывной дезодорации («Де-Смет», Бельгия)."),("1970–1980","Выпуск маргарина вырос с 25,4 до 51 тыс. тонн, майонеза в 2,4 раза."),("1993","Госпредприятие преобразовано в ОАО «Минский маргариновый завод» и вошло в концерн «Белгоспищепром»."),("Конец 1990-х","Растительное масло в ПЭТ-бутылке, первым было рапсовое. Линия маргарина в крупноблочной упаковке 20 кг."),("2006","Линия розлива масел до 3 000 бутылок в час, система менеджмента качества СТБ ISO 9001."),("2008–2011","Модернизация майонезного цеха с немецким оборудованием. Появились хрен, горчица в стекле, кетчуп в дой-паке."),("2016","Линия непрерывной дезодорации масел «Кирхфельд»."),("2021","Создана торговая марка «ВкуSноВ».")]
page("about.html","О компании",[("О компании",None)],f'''
<section class="sec"><div class="wrap ab2"><div><p class="big">ОАО «Минский маргариновый завод» — один из крупнейших производителей масложировой продукции в Беларуси. Продукция выходит под марками «Золотая капля» и «ВкуSноВ».</p>
<ul class="facts"><li><b>80+</b>наименований продукции</li><li><b>130+ т</b>продукции в сутки</li><li><b>15</b>стран экспорта</li></ul></div>
<figure class="zavod"><img src="assets/zavod.jpg" alt="Здание завода, иллюстрация"><figcaption>ул. Козлова, 27, Минск</figcaption></figure></div></section>
<section class="sec alt"><div class="wrap"><h2>История</h2><ol class="timeline">{"".join(f"<li><b>{y}</b><p>{t}</p></li>" for y,t in HIS)}</ol></div></section>
<section class="sec"><div class="wrap ab2"><div><h2>Качество и безопасность</h2></div><div><ul class="tags"><li class="pill line">СТБ ISO 9001</li><li class="pill line">СТБ 1470 (ХАССП)</li></ul><p style="margin-top:20px;color:var(--mute)">Вся продукция имеет декларации о соответствии или свидетельства о государственной регистрации.</p></div></div></section>''')

DEP=[("Приёмная","Секретарь-референт Веремейко Алла Петровна",["+375 (17) 301-30-15"],"mail@margarin.by"),("Отдел продаж","Начальник отдела Марцинкевич Дмитрий Владимирович",["+375 (17) 374-86-25","+375 (17) 374-46-25"],"sales@margarin.by"),("Внешнеэкономическая деятельность","Начальник сектора Неменков Денис Валентинович",["+375 (17) 397-50-11","+375 (29) 399-35-77"],"export@margarin.by"),("Отдел маркетинга","Начальник отдела Пекарская Анастасия Николаевна",["+375 (17) 374-46-45","+375 (44) 756-48-26"],"marketing@margarin.by"),("Материально-техническое снабжение","Начальник отдела Хотько Сергей Александрович",["+375 (17) 394-71-29","+375 (17) 374-97-12"],""),("Отдел кадров","",["+375 (17) 361-01-05"],"")]
tel=lambda s:"tel:+"+re.sub(r"\D","",s)
deps="".join(f'<li><h3>{a}</h3><p>{b}</p><p class="cont">{" / ".join(f"<a href=\'{tel(t)}\'>{t}</a>" for t in ts)}{f" / <a href=mailto:{m}>{m}</a>" if m else ""}</p></li>' for a,b,ts,m in DEP)
page("contacts.html","Контакты",[("Контакты",None)],f'''
<section class="sec"><div class="wrap ct"><div class="ct-main"><p class="kick">Адрес</p><p class="big">220037, Минск,<br>ул. Козлова, 27</p>
<div class="btns"><a class="pill solid" href="https://yandex.by/maps/?text=%D0%9C%D0%B8%D0%BD%D1%81%D0%BA%2C%20%D1%83%D0%BB.%20%D0%9A%D0%BE%D0%B7%D0%BB%D0%BE%D0%B2%D0%B0%2C%2027" target="_blank" rel="noopener">Открыть на Яндекс Картах</a><a class="pill line" href="https://www.google.com/maps/search/?api=1&query=%D0%9C%D0%B8%D0%BD%D1%81%D0%BA%2C+%D1%83%D0%BB.+%D0%9A%D0%BE%D0%B7%D0%BB%D0%BE%D0%B2%D0%B0%2C+27" target="_blank" rel="noopener">Google Maps</a></div>
<p class="kick" style="margin-top:40px">Реквизиты</p><p class="req">ОАО «Минский маргариновый завод» / УНП 100185236 / ОКПО 00333635<br>р/с BY65BAPB30122708900170000000 в ОАО «Белагропромбанк», БИК BAPBBY2X</p></div>
<ul class="deps">{deps}</ul></div></section>''')
print("ok")
