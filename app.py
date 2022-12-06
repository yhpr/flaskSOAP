from flask import Flask, render_template, request
from suds.client import Client


app = Flask(__name__, static_folder='static')

url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'

client = Client(url)

@app.route('/', methods=["GET","POST"])
def index():
    f_info = []
    # if request.method == "POST":
    flag_name = request.form.get("fname")
    c_iso_name = client.service.CountryISOCode(flag_name)
    info_country= client.service.FullCountryInfo(c_iso_name)

    for i in range(6):
        f_info.append(info_country[i])

    flag = info_country[6]

    return render_template("index.html", info=f_info, flag=flag)

if __name__ == "__main__":
    app.run(debug=True)
