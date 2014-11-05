Opbeat to Datadog hook
--------------

Receive notifications from Opbeat as Datadog events.
(Uses the new Opbeat API hooks.)

## Setup

It is really simple to set up with a few clicks. Follow these steps:

1. Create a <a href="https://app.datadoghq.com/account/settings#api" target="_blank">new Datadog API Key</a> and copy it.

1. Press this button to create a new Heroku app:

    <a href="https://heroku.com/deploy" target="_blank">
        <img src="https://www.herokucdn.com/deploy/button.png" alt="Deploy">
    </a>

1. Paste the API key into the `DATADOT_API_KEY` field and deploy the app.

1. After deployment, click **"View it"** to open the new app and copy the hook url.

1. Go to `https://opbeat.com/<yourorg>/settings/` and enter the hook url.

Hooks are now configured.

