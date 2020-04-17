""" Execute python code using jupyter kernel gateway """

from uuid import uuid4

from tornado import gen
from tornado.escape import json_encode, json_decode, url_escape
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.ioloop import IOLoop
from tornado.websocket import websocket_connect

HTTP_URL = "http://127.0.0.1:8888"
WS_URL = "ws://127.0.0.1:8888"

@gen.coroutine
def code_run():
    """ This funnction picks code
        from code.txt and execute it
        using kernel and saves output
        in output.txt
    """

    kernel_name = "python"

    code = ""
    file_obj = open("code.txt", "r")
    for line in file_obj:
        code = code + "\n" + line
    file_obj.close()

    client = AsyncHTTPClient()

    # Create kernel
    # POST /api/kernels
    print("Creating kernel {}...".format(kernel_name))
    response = yield client.fetch(
        '{}/api/kernels'.format(HTTP_URL),
        method='POST',
        body=json_encode({'name': kernel_name})
    )
    kernel = json_decode(response.body)
    kernel_id = kernel['id']
    print("Created kernel {0}.".format(kernel_id))

    # Connect to kernel websocket
    # GET /api/kernels/<kernel-id>/channels

    print("Connecting to kernel websocket...")
    ws_req = HTTPRequest(url='{}/api/kernels/{}/channels'.format(
        WS_URL,
        url_escape(kernel_id)))
    web_socket = yield websocket_connect(ws_req)
    print("Connected to kernel websocket.")

    # Submit code
    print("Submitting code: \n{}\n".format(code))
    msg_id = uuid4().hex
    req = json_encode({
        'header': {
            'username': '',
            'version': '5.0',
            'session': '',
            'msg_id': msg_id,
            'msg_type': 'execute_request'
        },
        'parent_header': {},
        'channel': 'shell',
        'content': {
            'code': code,
            'silent': False,
            'store_history': False,
            'user_expressions': {},
            'allow_stdin': False
        },
        'metadata': {},
        'buffers': {}
    })
    web_socket.write_message(req)

    print("Code submitted. Waiting for response...")
    kernel_idle = False
    while not kernel_idle:
        msg = yield web_socket.read_message()
        msg = json_decode(msg)
        msg_type = msg['msg_type']
        print("Received message type:{}".format(msg_type))

        if msg_type == 'error':
            print('ERROR')
            print(msg)
            break

        if 'msg_id' in msg['parent_header'] and \
                        msg['parent_header']['msg_id'] == msg_id:
            if msg_type == 'stream':
                output = msg['content']['text']
                print("  Content: {}".format(msg['content']['text']))
            elif msg_type == 'status' and \
                            msg['content']['execution_state'] == 'idle':
                kernel_idle = True

    web_socket.close()

    # Delete kernel
    # DELETE /api/kernels/<kernel-id>
    print("Deleting kernel...")
    yield client.fetch(
        '{}/api/kernels/{}'.format(HTTP_URL, kernel_id),
        method='DELETE'
    )
    print("Deleted kernel {0}.".format(kernel_id))
    file_obj = open("output.txt", "w")
    for line in output:
        file_obj.write(line)
    file_obj.close()
    return output

if __name__ == '__main__':
    OUTPUT = IOLoop.current().run_sync(code_run)
    print(OUTPUT)
