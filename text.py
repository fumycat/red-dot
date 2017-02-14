text_0 = 'Кот Матроскин, прибывший в Бердск прямо из деревни Простоквашино, хочет купить себе новый компьютер и узнать намного больше о мире информатики и современных технологиях. Но только вот в чем проблема, Кот Матроскин совсем не знает, как ему выбрать современный компьютер и ничего не знает об информатике. Помоги ему сделать правильный выбор!'
text_1 = 'Кот Матроскин решил отдохнуть после долгого пути и отправился гулять по площади. "Но стоит не забывать зачем я сюда приехал!", - сказал Кот Матроскин.'

txt = {
    0: {
        'divs': {'Пойти в магазин техники': 2, 'Пойти гулять по улице': 1},
        'h': 'Прибытие',
        'text': text_0,
        'pic_path': '/static/0.jpg'
    },
    1: {
        'divs': {},
        'h': 'На прогулке',
        'text': text_1,
        'pic_path': '/static/1.jpg'
    },
    2: {
        'divs': {},
        'h': 'На пути в магазин',
        'text': 'Кот Матроскин решает отправиться в магазин DNS на Универмаге в городе Бердске и купить себе компьютер.',
        'pic_path': '/static/2.jpg'
    }
}


def generate_buttons(buttons):
    final = '<div id="button-box">'
    for k, v in buttons.items():
        final += '<button onclick="getAjaxData({})" class="mui-btn mui-btn--raised mui-btn--primary">{}</button>'.format(v, k)
    return final + '</div>'


def generate_main_container(level_id):
    return '''
<div id="main-container">
    <h1>Приклечение кота Матроскина</h1>
    <h2 id="lvl-name">{}</h2>
    <img src="{}">
    <div id="main-text">{}</div>
    <div id="button-box">{}</div>
</div>'''.format(txt[level_id]['h'],
                 txt[level_id]['pic_path'],
                 txt[level_id]['text'],
                 generate_buttons(txt[level_id]['divs']))
