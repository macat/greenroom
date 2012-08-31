def send_request(outfit_id, recipients_list, sender):
    from .email import send_request as _send_request
    _send_request(outfit_id, recipients_list, sender)