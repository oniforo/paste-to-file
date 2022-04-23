from performance import performance_mode
from normal import normal_mode

import sys

opts = sys.argv[1:]
invalid_opts = []

# default values of the variables
filename = 'default.txt' 
sleep = 1
performance = False

for opt in opts:

    if opt.startswith('--filename'):
        filename = opt.split('=')[1]
    
    elif opt.startswith('--sleep'):
        sleep = int(opt.split('=')[1])
    
    elif opt.startswith('--performance'):
        performance = True
    
    else:
        invalid_opts.append(opt)

if invalid_opts:
    print(f'Unknown option(s): {", ".join(invalid_opts)}')
else:
    if performance:
        performance_mode(filename, sleep)
    else:
        normal_mode(filename, sleep)
