"""
For verifying mobile number
"""
from django.conf import settings

import twilio
import twilio.rest


def send_twilio_message(to_number, body):
    """
    Send a user verification message to that phone number
    """
    client = twilio.rest.TwilioRestClient(
        settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    #call_id = client.caller_ids.validate(to_number, friendly_name=to_number)
    return client.messages.create(body=body, to=to_number, from_=settings.TWILIO_PHONE_NUMBER)
