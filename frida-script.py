import frida

device_id = 'emulator-5554' # ID моего эмулятора


def intercept_requests(message, data): # функция, выгружающая ответы в аутпут
    if message['type'] == 'send':
        payload = message['payload']
        if 'url' in payload and 'method' in payload:
            url = payload['url']
            method = payload['method']
            print('URL:', url)
            print('Method:', method)

# подключение к эмулятору и приложению
device = frida.get_device(device_id)
pid = device.spawn(["com.dingtone.app.im"])
process = device.get_process("com.dingtone.app.im").pid
device.inject_library_file(process, '/data/local/tmp/gadget-android-arm64.so', 'gadget_entrypoint', 'data')
session = device.attach(pid)
device.resume(pid)

# считывание скрипта js
with open("new_file.js", "r") as file:
    script_code = file.read()

script = session.create_script(script_code)
script.on('message', intercept_requests)
script.load()
