def generate_divs(buttons):
    final = '<div id="button-box">'
    for k, v in buttons.items():
        final += '<button onclick="getAjaxData({})" class="mui-btn mui-btn--raised mui-btn--primary">{}</button>'.format(v, k)
    return final + '</div>'

txt = [
    {
        'divs': generate_divs({'Пойти в школу': 2, 'Пойти домой': 1}),
        'h': 'Самый первый уровень',
        'text': 'Текстик'
    },
    {
        'divs': generate_divs({'Пойти в школу': 2}),
        'h': 'Дом',
        'text': 'Текстик'
    },
    {
        'divs': generate_divs({'Пойти куда-нибудь': 3}),
        'h': 'Школа',
        'text': 'Текст'
    }
]
