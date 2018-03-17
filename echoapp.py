#!/usr/bin/python3

from bottle import Bottle

app = Bottle()


@app.route('/', method='GET')
def cs(filename='index.html'):
    return "welcome!\n"


@app.get('/echo/<text:path>')
def get_echo_text(text):
    res = "RESULT:\n" + text + "\n"
    print(res)
    return res


def main(host, port):
    app.run(host=host, port=port, debug=True)


if __name__ == '__main__':
    main('localhost', '9090')
