import pyperclip
import time

def performance_mode(filename, sleep):

    print('\nClipboard monitor is running in performance mode...')
    print('To run it in normal (live) mode, remove --performance as an option\n')
    print(f'mode: performance | filename: {filename} | sleep: {sleep}')

    with open(filename, 'a') as f:

        current_value = pyperclip.paste()
        while True:

            try:
                new_value = pyperclip.paste()

                if new_value != current_value:        
                    current_value = new_value
                    f.write(new_value + '\n')

                time.sleep(sleep)

            except KeyboardInterrupt:
                print('\nTerminating... Goodbye!\n')
                return
