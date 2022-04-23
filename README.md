# Paste to File

![GitHub top language](https://img.shields.io/github/languages/top/oniforo/paste-to-file) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/oniforo/paste-to-file)

The following script was made to help whenever there is a **repetitive copy and paste process**. It automates the pasting part, so you just have to copy whatever you want and all the pasting occurs in a specific file.

## Installation

Download and extract the contents from the compressed folder, or clone the repository using the command below:

```bash
git clone https://github.com/oniforo/paste-to-file.git
```

## Usage

```text
Usage: python main.py [options]

Options:
  --filename=FILENAME      Name of the file to be outputted
  --sleep=SLEEP            Number of seconds to look for updates
  --performance            Run in performance mode
```

## Options

### filename
Everytime you execute the script, it will search for a file with the specified name. If there is none, the file will be created. If no filename is provided, it will assume the standard filename ```default.txt```. Please provide filename and extension. Paths are relative to the root of the project, where ```main.py``` is located.

### sleep
Sleep is an integer that specifies the interval in seconds the clipboard will be searched for updates. Default value is ```1```. Larger intervals will improve overall performance.

### performance
Performance is an option to toggle between normal and performance modes. In ```normal mode```, the document is updated at every new entry into the clipboard, thus opening and closing the text file every time. In ```performance mode``` that file is only updated once the script is exited. 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)