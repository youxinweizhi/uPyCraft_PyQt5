# uPyCraft_PyQt5
### This is my modified version of uPyCraft based on PyQt5. For now, ONLY Linux is supported.

## Environment
Ubuntu 18.04.1
Python 3.6.5
Qt 5.11.1
PyQt5

## Pre-Install

1. python3
	$ python --version
    Python 3.6.5
    $ pip --version
    pip 18.0 from ~/.local/lib/python3.6/site-packages/pip (python 3.6)
    $ pip3 --version
    pip 18.0 from ~/.local/lib/python3.6/site-packages/pip (python 3.6)

    pip3 install -U pyinstaller --user
    pip3 install -U pyflakes --user
    pip3 install -U pyserial --user

2. QT
    a. Download the NEWEST qt-opensource-linux-x64-5.11.1.run from https://www.qt.io/download
	b. $ sudo ./qt-opensource-linux-x64-5.11.1.run

3. SIP
    Refer to https://riverbankcomputing.com/software/sip/download
    pip3 install -U sip --user
        
4. PyQt5
    Refer to https://sourceforge.net/projects/pyqt/files/PyQt5/
	$ pip3 install -U pyqt5 --user

5. QScintilla2
    Refer to https://pypi.org/project/QScintilla/
    $ pip3 install -U QScintilla --user


## Package uPyCraft
    $ pyinstaller -F uPyCraft.py