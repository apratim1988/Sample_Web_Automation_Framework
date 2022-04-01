import requests

def send_slack_message(message):

    payload = '{"text":"%s"}' % message
    myToken = 'xoxb-222667903840-2829029809671-QS4nUmL2XytsXN5bCTYOPejx'
    myUrl = 'https://hooks.slack.com/services/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'
    head = {'Authorization': 'token {}'.format(myToken)}
    response = requests.post(myUrl, headers=head,data=payload)
    print(response.text)

