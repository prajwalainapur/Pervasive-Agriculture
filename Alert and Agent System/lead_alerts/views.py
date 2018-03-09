from lead_alerts import app
from flask import flash, redirect, render_template, request
from twilio.base.exceptions import TwilioRestException


from .services.twilio_service import TwilioService

@app.route('/')
def index():
    house = {
                'title': 'P-Agri Solutions and Services',
                'price': 'Free*',
                'description':
                    'Once connected, you\'ll definitely love our services. ' +
                    'Showing best crops, best suitable fertilizers and other requirements' +
                    'with high efficiency, this joint is loaded to the max. ' +
                    'We are offering this service for FREE, act now!'
            }
    return render_template('index.html', house=house)

@app.route('/notifications', methods=['POST'])
def create():
    house_title = request.form["house_title"]
    name = request.form["name"]
    phone = request.form["phone"]
    message = request.form["message"]

    twilio_service = TwilioService()

    formatted_message = build_message(house_title, name, phone, message)
    try:
        twilio_service.send_message(formatted_message)
        flash('Thanks! An agent will be contacting you shortly', 'success')
    except TwilioRestException as e:
        print(e)
        flash('Oops! There was an error. Please try again.', 'danger')

    return redirect('/')

def build_message(house_title, name, phone, message):
    template = 'New lead received for {}. Call {} at {}. Message {}'
    return template.format(house_title, name, phone, message)
