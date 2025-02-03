from flask import Flask, render_template, request
from waitress import serve
from ip import get_default_ip_details, get_ip_details

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/fetch_ip')
def fetch_ip():

    # Run the API call
    ip_dump = get_default_ip_details()

    # Return results 
    return render_template(
        'ip.html',
        ip_address=ip_dump["ip"],
        isp=ip_dump["isp"]["isp"],
        state=ip_dump["location"]["state"],
        country=ip_dump["location"]["country"],
        mobile=ip_dump["risk"]["is_mobile"]
    )


@app.route('/get_ip')
def get_ip():

    # Take the input from the user
    ip_addr = request.args.get('ip_addr').strip()

    # Run the API call
    ip_dump = get_ip_details(ip_addr)

    # Check if the call is successful
    if ip_dump.get("error"): 
        return render_template('invalid.html')

    # Return results 
    return render_template(
        'ip.html',
        ip_address=ip_dump["ip"],
        isp=ip_dump["isp"]["isp"],
        state=ip_dump["location"]["state"],
        country=ip_dump["location"]["country"],
        mobile=ip_dump["risk"]["is_mobile"]
    )




if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)