from datetime import datetime
def get_date_time(func):
    def wrapper():
        print("function name="+ func.__name__)
        print(datetime.today().strftime("%Y-%M-%D %H:%M:%S"))
        func()
    return wrapper
@get_date_time
def login():
    print("login")
login()
@get_date_time
def logout():
    print("logout")
logout()
