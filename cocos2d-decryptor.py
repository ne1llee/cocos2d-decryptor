import frida
import sys
import json
import os
     
# Android package name of Cocos2d game
PACKAGE_NAME = "com.my.package" 
# accompanied JS script (do not change)
SCRIPT_PATH = "cocos2d-decryptor.js"     
# where to save decrypted source code files 
OUTPUT_FOLDER = "./cocos2dgame-files"     

def on_message(message, data):
    if message['type'] == 'send':
        data = json.loads(message['payload'])
        file = data['file']
        contents = data['content']

        local_file = OUTPUT_FOLDER + file

        directory = os.path.dirname(local_file)
        if not os.path.exists(directory):
            os.makedirs(directory)

        open(local_file, "wb").write(bytes.fromhex(contents))
        print("Saved: " + local_file)
    else:
        print("[*] {}".format(message))


def attach_to_device_by_ip(process_name, js_script_path):
    session = frida.get_usb_device()
    pid = session.spawn([process_name])
    process = session.attach(pid)
    script_code = open(js_script_path, 'r').read()
    script = process.create_script(script_code)
    script.on('message', on_message)
    script.load()
    session.resume(pid)
    sys.stdin.read()


if __name__ == "__main__":
    attach_to_device_by_ip(PACKAGE_NAME, SCRIPT_PATH)