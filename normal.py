import pyperclip
import time

def normal_mode(filename, sleep):

    print('\nClipboard monitor is running in normal mode...')
    print('To run it in performance mode, add --performance as an option\n')
    print(f'mode: normal | filename: {filename} | sleep: {sleep}')

    current_value = pyperclip.paste()
    while True:

        try:
            new_value = pyperclip.paste()    
            if new_value != current_value:
                
                current_value = new_value
                
                with open(filename, 'a') as f:
                    f.write(new_value + '\n')

            time.sleep(sleep)

        except KeyboardInterrupt:
            print('\nTerminating... Goodbye!\n')
            return
