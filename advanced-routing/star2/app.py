from bottle import run, route, error, static_file
import feedparser


@route('/get_RSS_feed/<feed_select>')
def get_feed(feed_select):
    switcher = {
        'reuters': 'http://feeds.reuters.com/news/artsculture',
        "DM": 'http://www.dailymail.co.uk/articles.rss',
        "wired": 'http://feeds.wired.com/wired/index'
    }
    feed_link = switcher.get(feed_select)
    return feedparser.parse(feed_link)


@route('/')
def index():
    return static_file('index.html', root='static')


@route('/<filename:path>')
def serve_file(filename):
    return static_file(filename, root='static')


@error(404)
def error_404(error):
    return static_file('error.html', root='static')


if __name__ == "__main__":
    run(host='localhost', port='7000', reloader=True)
