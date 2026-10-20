#!/usr/bin/env python3
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def set_run_font(run, name="Times New Roman", size=14, bold=False, italic=False):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic


def add_centered(doc, text, size=14, bold=False, space_after=0, space_before=0):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold)
    return p


def add_body(doc, text, bold=False, italic=False, first_line_indent=True, space_after=6):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    if first_line_indent:
        p.paragraph_format.first_line_indent = Cm(1.25)
    run = p.add_run(text)
    set_run_font(run, bold=bold, italic=italic)
    return p


def add_heading_like(doc, text, bold=True, size=14, center=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold)
    return p


def add_figure_placeholder(doc, caption):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run("[Місце для рисунка]")
    set_run_font(run, size=12, italic=True)
    run.font.color.rgb = RGBColor(128, 128, 128)

    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_after = Pt(12)
    cap.paragraph_format.space_before = Pt(0)
    run = cap.add_run(caption)
    set_run_font(run, size=12, bold=True)
    return cap


def add_qa(doc, question, answer):
    add_body(doc, "Запитання:", bold=True, first_line_indent=False, space_after=2)
    add_body(doc, question, first_line_indent=False, space_after=4)
    add_body(doc, f"Відповідь: {answer}", first_line_indent=False, space_after=8)


def main():
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(1.5)

    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(14)
    style._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")

    add_centered(doc, "Державний вищий навчальний заклад", size=14)
    add_centered(doc, "Ужгородський національний університет", size=14)
    add_centered(doc, "Факультет інформаційних технологій", size=14)
    add_centered(doc, "Кафедра програмного забезпечення систем", size=14, space_after=24)

    add_centered(doc, "ЛАБОРАТОРНА РОБОТА № 2", size=16, bold=True, space_before=24)
    add_centered(
        doc,
        "Тема: Packet Tracer – Підключення пристроїв до домашнього шлюзу та моніторинг мережі",
        size=14,
        bold=True,
        space_after=36,
    )

    add_centered(doc, "Виконала:", size=14, space_before=48)
    add_centered(doc, "студентка І курсу ОС Магістр", size=14)
    add_centered(doc, "спеціальності: 121 інженерія", size=14)
    add_centered(doc, "програмного забезпечення", size=14)
    add_centered(doc, "Чекета Юлія Михайлівна", size=14, bold=True, space_after=48)

    add_centered(doc, "Ужгород - 2026", size=14, space_before=72)

    doc.add_page_break()

    add_body(
        doc,
        "Мета роботи: Навчитися під’єднувати домашній шлюз (Home Gateway) та пристрої кінцевого користувача "
        "до наявної домашньої мережі в середовищі Cisco Packet Tracer, додавати дротові й бездротові пристрої IoT, "
        "реєструвати їх на сервері Home Gateway, налаштовувати Bluetooth-з’єднання та здійснювати моніторинг "
        "і керування пристроями через програму IoT Monitor.",
        first_line_indent=True,
    )

    add_heading_like(doc, "Цілі та задачі", bold=True, center=False)
    add_body(doc, "Частина 1. Підключення Home Gateway до мережі", first_line_indent=False, space_after=2)
    add_body(doc, "Частина 2. Додавання пристроїв кінцевого користувача до мережі", first_line_indent=False, space_after=2)
    add_body(doc, "Частина 3. Під’єднання пристроїв IoT до мережі", first_line_indent=False, space_after=2)
    add_body(doc, "Частина 4. Додавання пристроїв Bluetooth", first_line_indent=False, space_after=8)

    add_heading_like(doc, "Довідкова інформація / Сценарій", bold=True, center=False)
    add_body(
        doc,
        "У цій вправі під’єднується домашній шлюз Home Gateway і кілька пристроїв IoT до наявної домашньої мережі, "
        "а також проводиться моніторинг цих пристроїв за допомогою функції Home Gateway. "
        "Вправа оцінюється: після отримання вказівки змінюється значення «Відображуване ім’я», "
        "інакше оцінка буде неточною. У будь-який момент можна клацнути елемент «Перевірити результати», "
        "щоб побачити свої успіхи.",
    )

    add_heading_like(doc, "Частина 1: Підключення Home Gateway до мережі", bold=True, center=False)

    add_heading_like(doc, "Крок 1: Додавання Home Gateway", bold=True, size=14)
    add_body(
        doc,
        "a. У полі «Вибір типу пристрою» клацнуто елемент «Мережеві пристрої», а потім — «Бездротові пристрої».",
        first_line_indent=False,
    )
    add_body(
        doc,
        "b. Клацнуто елемент Home Gateway, а потім робочу область «Логічна», щоб додати пристрій.",
        first_line_indent=False,
    )
    add_body(
        doc,
        "c. Клацнуто елемент Home Gateway0, вкладку «Налаштування». Значення «Відображуване ім’я» змінено на Home Gateway.",
        first_line_indent=False,
    )
    add_figure_placeholder(doc, "Рис. 1 Додавання Home Gateway і зміна відображуваного імені")

    add_heading_like(doc, "Крок 2: Під’єднання Home Gateway до кабельного модема", bold=True, size=14)
    add_body(
        doc,
        "a. У вікні «Вибір типу пристрою» клацнуто елемент «Підключення», а потім — «Мідний кабель прямого з’єднання».",
        first_line_indent=False,
    )
    add_body(
        doc,
        "b. Клацнуто елемент «Кабельний модем» і під’єднано один кінець кабелю до порту Порт 1.",
        first_line_indent=False,
    )
    add_body(
        doc,
        "c. Клацнуто елемент Home Gateway і під’єднано інший кінець кабелю до порту «Інтернет».",
        first_line_indent=False,
    )
    add_figure_placeholder(doc, "Рис. 2 Підключення Home Gateway до кабельного модема")

    add_heading_like(doc, "Частина 2: Додавання пристроїв кінцевого користувача до мережі", bold=True, center=False)

    add_heading_like(doc, "Крок 1: Додайте бездротовий планшет до мережі", bold=True, size=14)
    add_body(
        doc,
        "a. У вікні «Вибір типу пристрою» натиснуто «Кінцеві пристрої», потім — «Планшет». "
        "Елемент «Планшет» додано до робочого простору.",
        first_line_indent=False,
    )
    add_body(
        doc,
        "b. Клацнуто Tablet PC0, вкладку «Налаштування». Значення «Відображуване ім’я» змінено на «Планшет».",
        first_line_indent=False,
    )
    add_figure_placeholder(doc, "Рис. 3 Додавання планшета до робочої області")

    add_heading_like(doc, "Крок 2: Під’єднання планшета до мережі Home Gateway", bold=True, size=14)
    add_body(
        doc,
        "Зверніть увагу: елемент «Планшет» уже під’єднано до стільникової мережі. "
        "Синій значок бездротового сигналу свідчить про під’єднання до хмарної мережі Інтернет, "
        "яка підтримується оператором стільникового зв’язку.",
    )
    add_body(
        doc,
        "a. Щоб під’єднати «Планшет» до домашньої бездротової мережі, клацнуто інтерфейс Wireless0 "
        "на лівій панелі у вкладці «Налаштування».",
        first_line_indent=False,
    )
    add_body(
        doc,
        "b. Для ідентифікатора SSID значення «За умовчуванням» змінено на HomeGateway. "
        "Планшет під’єднався до домашньої мережі Wi-Fi. Для зміни IP-адреси на адресу з мережі "
        "192.168.25.x може знадобитися хвилина або дві. Процес прискорено кнопкою «Прискорити час» (Alt+D).",
        first_line_indent=False,
    )
    add_body(
        doc,
        "c. Планшет має два бездротові з’єднання: стільниковий зв’язок і Wi-Fi. "
        "Це типова ситуація для планшетів і смартфонів із підтримкою стільникового зв’язку.",
        first_line_indent=False,
    )
    add_figure_placeholder(doc, "Рис. 4 Підключення планшета до SSID HomeGateway")

    add_heading_like(doc, "Крок 3: Отримання доступу до Home Gateway з планшета", bold=True, size=14)
    add_body(
        doc,
        "На планшеті клацнуто елемент «Моніторинг пристроїв IoT» на вкладці «Робочий стіл». "
        "Адреса сервера IoT — це IP-адреса Home Gateway, а значення admin використовується "
        "як для імені користувача, так і для пароля. Клацнуто «Увійти».",
    )
    add_body(
        doc,
        "Це підтверджує доступ до сервера IoT Home Gateway. У списку сервера IoT Home Gateway "
        "поки що не відображаються жодні пристрої.",
    )
    add_figure_placeholder(doc, "Рис. 5 Вхід у IoT Monitor на планшеті (список пристроїв порожній)")

    add_heading_like(doc, "Частина 3: Під’єднання пристроїв IoT до мережі", bold=True, center=False)
    add_body(
        doc,
        "У цій частині додано три нові пристрої IoT до мережі й зареєстровано їх на сервері Home Gateway.",
    )

    add_heading_like(doc, "Крок 1: Додайте IoT-пристрій до дротової мережі", bold=True, size=14)
    add_body(
        doc,
        "a. У вікні «Вибір типу пристрою» вибрано «Кінцеві пристрої» → «Головна сторінка», "
        "потім клацнуто елемент «Лампа» і додано його до робочого простору.",
        first_line_indent=False,
    )
    add_body(
        doc,
        "b. Клацнуто пристрій «Лампа», потім — «Додатково», щоб відобразити більше вкладок.",
        first_line_indent=False,
    )
    add_body(
        doc,
        "c. Клацнуто «Налаштування вводу/виводу» і змінено значення мережевого адаптера на PT-IOT-NM-1CFE.",
        first_line_indent=False,
    )
    add_body(
        doc,
        "d. На вкладці «Налаштування» пристрій перейменовано на «Лампа».",
        first_line_indent=False,
    )
    add_body(
        doc,
        "e. На лівій панелі клацнуто FastEthernet0 і вибрано перемикач DHCP, "
        "щоб лампа отримувала адресу IPv4 від Home Gateway.",
        first_line_indent=False,
    )
    add_body(
        doc,
        "f. Через «Підключення» → «Мідний кабель прямого підключення» порт FastEthernet0 пристрою «Лампа» "
        "під’єднано до одного з доступних портів Ethernet у Home Gateway.",
        first_line_indent=False,
    )
    add_figure_placeholder(doc, "Рис. 6 Підключення лампи до Home Gateway (дротове з’єднання, DHCP)")

    add_heading_like(doc, "Крок 2: Додайте пристрої IoT до бездротової мережі HomeGateway", bold=True, size=14)
    add_body(
        doc,
        "a. У вікні «Вибір типу пристрою» клацнуто «Кінцеві пристрої» → «Головна сторінка». "
        "До робочої області додано елементи «Вентилятор» і «Двері».",
        first_line_indent=False,
    )
    add_body(doc, "b. Відображуване ім’я вентилятора змінено на «Вентилятор».", first_line_indent=False)
    add_body(doc, "c. Відображуване ім’я дверей змінено на «Двері».", first_line_indent=False)
    add_body(
        doc,
        "d. У налаштуванні Wireless0 для кожного пристрою для параметра SSID уже встановлено значення HomeGateway, "
        "і кожен із пристроїв отримав IP-адресу з мережі 192.168.25.x. Для прискорення натиснуто «Прискорити час».",
        first_line_indent=False,
    )
    add_figure_placeholder(doc, "Рис. 7 Бездротове підключення вентилятора та дверей")

    add_heading_like(doc, "Крок 3: Налаштування реєстрації пристроїв IoT на сервері Home Gateway", bold=True, size=14)
    add_body(
        doc,
        "Для кожного з трьох пристроїв IoT («Лампа», «Вентилятор», «Двері») відкрито вкладку «Налаштування», "
        "потім елемент «Настройки» на лівій панелі. У списку параметрів «Сервер IoT» вибрано Home Gateway.",
    )
    add_figure_placeholder(doc, "Рис. 8 Реєстрація пристроїв IoT на сервері Home Gateway")

    add_heading_like(doc, "Крок 4: Перевірка реєстрації пристроїв на сервері Home Gateway", bold=True, size=14)
    add_body(
        doc,
        "На «Планшеті» відкрито «Моніторинг пристроїв IoT» на вкладці «Робочий стіл» і виконано вхід (Увійти). "
        "Відобразилися записи для всіх трьох нових пристроїв IoT. Записи розгорнуто для перегляду відомостей. "
        "Виконано керування пристроями з відстеженням результатів у робочій області.",
    )
    add_body(
        doc,
        "Примітка. Може знадобитися хвилина-дві, перш ніж три пристрої буде зареєстровано на сервері "
        "й вони відобразяться в списку «Моніторинг пристроїв IoT».",
        italic=True,
    )
    add_figure_placeholder(doc, "Рис. 9 Три пристрої IoT у списку IoT Monitor")

    add_heading_like(doc, "Частина 4: Додавання пристроїв Bluetooth", bold=True, center=False)
    add_body(
        doc,
        "У цій частині додано динамік Bluetooth до бездротової мережі та під’єднано до нього портативний музичний плеєр.",
    )

    add_heading_like(doc, "Крок 1: Додайте динамік Bluetooth до бездротової мережі", bold=True, size=14)
    add_body(
        doc,
        "a. У вікні «Вибір типу пристрою» вибрано «Кінцеві пристрої» → «Головна сторінка». "
        "До робочої області додано пристрій «Динамік Bluetooth».",
        first_line_indent=False,
    )
    add_body(
        doc,
        "b. Динамік автоматично підключився до Home Gateway. Через кілька хвилин для динаміка "
        "було налаштовано IP-адресу з мережі 192.168.25.x.",
        first_line_indent=False,
    )
    add_body(doc, "c. Відображуване ім’я динаміка змінено на «Динамік».", first_line_indent=False)
    add_body(
        doc,
        "d. На вкладці «Налаштування» для динаміка клацнуто «Bluetooth» на лівій панелі "
        "і для параметра «Стан порту» встановлено значення «Увімкн.».",
        first_line_indent=False,
    )
    add_figure_placeholder(doc, "Рис. 10 Додавання динаміка Bluetooth і увімкнення порту")

    add_heading_like(doc, "Крок 2: Додавання портативного медіаплеєра до бездротової мережі", bold=True, size=14)
    add_body(
        doc,
        "a. У вікні «Вибір типу пристрою» вибрано «Кінцеві пристрої» → «Головна сторінка». "
        "До робочого простору додано «Портативний музичний плеєр».",
        first_line_indent=False,
    )
    add_body(
        doc,
        "b. Музичний плеєр автоматично під’єднався до маршрутизатора Home Gateway "
        "і отримав IP-адресу в мережі 192.168.25.x.",
        first_line_indent=False,
    )
    add_body(doc, "c. Відображуване ім’я змінено на «Музичний плеєр».", first_line_indent=False)
    add_figure_placeholder(doc, "Рис. 11 Додавання музичного плеєра")

    add_heading_like(doc, "Крок 3: З’єднання музичного плеєра з динаміком", bold=True, size=14)
    add_body(
        doc,
        "a. Параметр «Стан порту» Bluetooth перемкнуто на «Увімкн.».",
        first_line_indent=False,
    )
    add_body(
        doc,
        "b. Клацнуто «Виявити» в розділі «Видимі пристрої», вибрано «Динамік», "
        "потім — «Створити пару», а потім — «Так».",
        first_line_indent=False,
    )
    add_body(
        doc,
        "c. Натиснувши й утримуючи клавішу Alt, клацнуто елемент «Музичний плеєр». "
        "(Динаміки фізичного комп’ютера мають бути увімкнені.)",
        first_line_indent=False,
    )

    add_qa(
        doc,
        "Що відбувається?",
        "Після створення Bluetooth-пари між «Музичним плеєром» і «Динаміком» "
        "і натискання Alt + клацання по музичному плеєру починає відтворюватися музика "
        "через динамік Bluetooth. Звук іде з динаміків комп’ютера, на якому запущено Packet Tracer, "
        "що демонструє успішне Bluetooth-з’єднання між пристроями.",
    )
    add_figure_placeholder(doc, "Рис. 12 Bluetooth-пара між музичним плеєром і динаміком")

    add_heading_like(doc, "Крок 4: Дослідження мережі", bold=True, size=14)
    add_body(
        doc,
        "До мережі додано додаткові дротові й бездротові пристрої. "
        "Натисканням і утриманням клавіші Alt можна взаємодіяти з пристроями IoT: "
        "увімкнути «Музичний плеєр», відкрити «Двері», увімкнути «Лампу» й «Вентилятор». "
        "Додатково пристроями IoT можна керувати за допомогою програми IoT Monitor на планшеті.",
    )
    add_figure_placeholder(doc, "Рис. 13 Керування пристроями IoT (Alt-клацання / IoT Monitor)")

    add_heading_like(doc, "Висновок", bold=True, center=False)
    add_body(
        doc,
        "Під час виконання даної лабораторної роботи я ознайомилася з підключенням домашнього шлюзу "
        "Home Gateway до кабельного модема та побудовою домашньої мережі в Cisco Packet Tracer. "
        "Було додано планшет кінцевого користувача, підключено його до бездротової мережі HomeGateway "
        "та перевірено доступ до сервера IoT через програму «Моніторинг пристроїв IoT». "
        "До мережі під’єднано дротовий пристрій IoT («Лампа») та бездротові («Вентилятор», «Двері»), "
        "зареєстровано їх на сервері Home Gateway і перевірено можливість віддаленого керування. "
        "Також налаштовано Bluetooth-з’єднання між музичним плеєром і динаміком, "
        "що підтверджує роботу різних типів підключень у домашній IoT-мережі.",
    )

    out = "/workspace/labs/Лабораторна_робота_2_Home_Gateway.docx"
    doc.save(out)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
