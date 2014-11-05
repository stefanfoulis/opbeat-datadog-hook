import os
from bottle import get, post, run, request
from bottle import jinja2_template as template
from dogapi import dog_http_api as api

title_template = """
{{app['name']}}: {{title}}
"""

text_template = """
{{html_url}}

{{summary}}
"""


DATADOG_API_KEY = os.environ.get('DATADOG_API_KEY')
if not DATADOG_API_KEY:
    print("Missing environment variable DATADOG_API_KEY")
    exit(1)
else:
    api.api_key = DATADOG_API_KEY


TAGS = [tag.strip() for tag in os.environ.get('TAGS', "").split(',')]


def send(data):
    title = template(title_template, **data)
    text = template(text_template, **data)
    tags = [tag for tag in TAGS if tag]
    tags.append('app:{}'.format(data['app']['short_name']))
    tags.append('subject_type:{}'.format(data['subject_type']))
    tags.append('organization:{}'.format(data['organization']['short_name']))
    subject_type = data.get('subject_type', '')
    if subject_type in ['release']:
        alert_type = 'success'
    elif subject_type in ['errorgroup']:
        alert_type = 'error'
    else:
        alert_type = 'info'
    tags.append(alert_type)
    api.event_with_response(
        title,
        text,
        tags=tags,
        alert_type=alert_type,
    )


@post('/new-activity')
def new_activity():
    data = request.json
    send(data)
    return "ok"


@get('/setup')
def setup():
    url = request.url.replace("/setup", "/new-activity")
    return template("This is your hook url, copy it:<h3>{{url}}</h3>", url=url)


run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
