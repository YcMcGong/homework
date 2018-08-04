# endpoints
SERVER_ENDPOINT = 'http://0.0.0.0:8000'
class endpoints():
    home = SERVER_ENDPOINT
    signin = SERVER_ENDPOINT + '/signin'
    signup = SERVER_ENDPOINT + '/signup'
    testimonial = SERVER_ENDPOINT + '/add_testimonial'
    faq = SERVER_ENDPOINT + '/add_faq'