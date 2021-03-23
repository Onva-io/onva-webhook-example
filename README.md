# Handling Onva webhooks

A simple example app for handling webhooks sent by the Onva platform.

Feel free to use any of the code here in your own platform.

## Run locally

### Run the webhook catcher

You can run this code using the following, assuming `virtualenv` is available. Please remember to change `use-a-secret-key` to something more secret.

```
$ virtualenv env
...
$ source env/bin/activate
(env) $ pip install -r requirements.txt 
...
(env) $ ONVA_SHARED_KEY=use-a-secret-key FLASK_APP=app flask run
 * Serving Flask app "app"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You now have the app listening on your local machine and you can use something like like localhost.run to expose it to the internet. Example:

### Expose yourself

```
$  ssh -R 80:localhost:5000 nokey@localhost.run                                     
===============================================================================
Welcome to localhost.run!

Follow your favourite reverse tunnel at https://twitter.com/localhost_run .

**You need a SSH key to access this service.**
If you get a permission denied follow Gitlab's most excellent howto:
https://docs.gitlab.com/ee/ssh/
*Only rsa and ed25519 keys are supported*

To set up and manage custom domains go to https://admin.localhost.run/

More details on custom domains (and how to enable subdomains of your custom
domain) at https://localhost.run/docs/custom-domains

To explore using localhost.run visit the documentation site:
https://localhost.run/docs/

===============================================================================


** your connection id is d2855723-f3c8-4c3e-b49f-c838727afad9, please mention it if you send me a message about an issue. **

015ec787d19e44.localhost.run tunneled with tls termination, https://015ec787d19e44.localhost.run
```

You're now visible to the internet with the link `https://015ec787d19e44.localhost.run`.

### Add webhook in dashboard

Login to https://app.onva.io/ and visit the webhook section. Give it a name such as "Test", the endpoint should be the URL you see in *your* terminal. The shared key will be the value that you set for `ONVA_SHARED_KEY=use-a-secret-key`.

### Webhook events

There are two webhook events currently - `ping` and `submission.complete` - and new events will be added over time. A `ping` payload is sent when setting up the webhook, and a `submission.complete` payload is sent when a submission completes. The envelope of a webhook payload looks like this:

```
{
    "event_type": "ping",
    "event_uuid": "unique-webhookevent-uuid",
    "data": {},
    "retry_number": 0
}
```

The value of `retry_number` indicates the number of attempts to deliver the payload *before* this attempt.

### Payload data

The payload data for a `ping` event will be empty, where-as the payload for a `submission.complete` event will match up with the response provided by a submission details API request detailed at https://api.onva.io/redoc/#operation/submission_get
