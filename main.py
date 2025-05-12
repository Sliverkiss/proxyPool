from flask import Flask
import random
from request_abt import get_request
from output import http_yanzheng

app = Flask(__name__)

# 初始化代理池文件数据
get_request.get_http()
http_yanzheng.main()

@app.route('/random', methods=['GET'])
def random_route():
    output_filename = "output/http.txt"
    proxies = http_yanzheng.read_proxies_from_file(output_filename)
    if proxies:
        return random.choice(proxies)
    else:
        return 'No proxies found', 404

@app.route('/verify', methods=['GET'])
def verify_route():
    get_request.get_http()
    result=http_yanzheng.main()
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=33333, debug=False)
