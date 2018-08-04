# endpoints
SERVER_ENDPOINT = 'http://10.0.0.195:8000'
class endpoints():
    home = SERVER_ENDPOINT
    signin = SERVER_ENDPOINT + '/signin'
    signup = SERVER_ENDPOINT + '/signup'
    testimonial = SERVER_ENDPOINT + '/add_testimonial'
    faq = SERVER_ENDPOINT + '/add_faq'