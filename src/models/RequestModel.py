class RequestModel(object):

    pin_code = ''
    email_id = ''

    def __init__(self):
        print('request model initialize')

    def __init__(self, pin_code, email_id):
        self.pin_code = pin_code
        self.email_id = email_id

    def get_pin_code(self):
        return self.pin_code

    def get_email_id(self):
        return self.email_id

    def __str__(self):
        return self.pin_code + '|' + self.email_id
