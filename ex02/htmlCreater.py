from userInterface import temperatureView
from userInterface import windSpeedView
from userInterface import pressureView


def create(device = 1):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, temperatureView(device))
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, windSpeedView(device))
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressureView(device))
    html += '  </body>\n</html>'
    
    with open('index.html', 'w') as page:
        page.write(html)

    return html


'''
def new_create(data ,device = 1):
    t, p, w = data
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, w)
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '  </body>\n</html>'
    
    with open('new_index.html', 'w') as page:
        page.write(html)

    return data'''