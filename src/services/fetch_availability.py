from src.models.RequestModel import RequestModel
from src.models.ResponseModel import ResponseModel
from datetime import datetime
from src.services.email_service import EmailService
import requests
import sqlite3
import schedule
import time

class VaccineStatusService:

    def __init__(self, sub_requests: [RequestModel]):
        self.sub_requests = sub_requests

    def get_vaccine_availability(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        for request in self.sub_requests:
            url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/' \
                  'calendarByPin?pincode=' + request.pin_code + '&date=' + datetime.today().strftime('%d-%m-%Y')
            response = requests.get(url, headers=headers)
            self.process_response(response, request)

    def process_response(self, response, request):
        centers = response.json()['centers']
        responses = []
        for center in centers:
            for session in center['sessions']:
                if session['available_capacity'] > 0 and session['min_age_limit'] == 18:
                    response_model = ResponseModel(center['name'], center['address'], center['district_name'],
                                                   center['block_name'], center['fee_type'], session['vaccine'],
                                                   session['available_capacity'], session['date'], session['slots'])
                    responses.append(response_model)

        if len(responses) > 0:
            self.trigger_email(responses, request)

    def trigger_email(self, responses: [ResponseModel], request):
        email_service = EmailService(responses, request)
        email_service.trigger_email()


def get_db_connection():
    conn = sqlite3.connect('../database.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_config():
    conn = get_db_connection()
    requests_db = conn.execute('SELECT * FROM requests').fetchall()
    conn.close()
    requests_arr = []
    for data in requests_db:
        request_model = RequestModel(data['pin_code'], data['email_id'])
        requests_arr.append(request_model)

    vaccine_service = VaccineStatusService(requests_arr)
    vaccine_service.get_vaccine_availability()


if __name__ == '__main__':
    schedule.every().hour.do(init_config)
    while True:
        schedule.run_pending()
        time.sleep(1)