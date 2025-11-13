import os
from flask import Flask, request, render_template

app = Flask(__name__)


def get_client_ip():
    """
    Get the client's IP address, handling proxy scenarios.
    Checks X-Forwarded-For and X-Real-IP headers first.
    """
    # Check X-Forwarded-For header (most common for proxies/load balancers)
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        # X-Forwarded-For can contain multiple IPs (client, proxy1, proxy2, ...)
        # The first IP is typically the original client
        ip = x_forwarded_for.split(',')[0].strip()
        return ip
    
    # Check X-Real-IP header (used by some proxies like nginx)
    x_real_ip = request.headers.get('X-Real-IP')
    if x_real_ip:
        return x_real_ip.strip()
    
    # Fall back to remote_addr (direct connection)
    return request.remote_addr

def get_system_label():
    """
    Get system info from SYSTEM_LABEL environment variable.
    Returns None if not set.
    """
    return os.environ.get('SYSTEM_LABEL', None)

@app.route('/')
def index():
    """Main route that displays the IP address."""
    client_ip = get_client_ip()
    
    # Gather additional information for display
    x_forwarded_for = request.headers.get('X-Forwarded-For', '')
    x_real_ip = request.headers.get('X-Real-IP', '')
    remote_addr = request.remote_addr
    user_agent = request.headers.get('User-Agent', None)
    system_label = get_system_label()
    
    # Determine if request came through a proxy
    behind_proxy = bool(x_forwarded_for or x_real_ip)

    #If this is a curl like reqeust just return the IP no nonsense
    if user_agent == None or user_agent.startswith('curl'):
        return raw_ip()
    
    return render_template(
        'index.html',
        ip_address=client_ip,
        x_forwarded_for=x_forwarded_for,
        x_real_ip=x_real_ip,
        remote_addr=remote_addr,
        user_agent=user_agent,
        behind_proxy=behind_proxy,
        system_label=system_label
    )

@app.route('/raw')
def raw_ip():
    """Raw IP endpoint that returns just the IP address."""
    client_ip = get_client_ip()
    return client_ip + "\n"

@app.route('/json')
def api_ip():
    """API endpoint that returns IP as JSON."""
    client_ip = get_client_ip()
    json_payload = {
        'ip': client_ip,
        'x_forwarded_for': request.headers.get('X-Forwarded-For', ''),
        'x_real_ip': request.headers.get('X-Real-IP', ''),
        'remote_addr': request.remote_addr,
        'behind_proxy': bool(request.headers.get('X-Forwarded-For') or request.headers.get('X-Real-IP'))
    }

    system_label = get_system_label()
    if system_label:
        json_payload['system_label'] = system_label

    return json_payload

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
