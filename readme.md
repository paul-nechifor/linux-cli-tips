# Linux CLI tips

A script that prints bubbles with Linux command-line interface tips. It's best
used as a terminal startup program.

## Example

    $ python2 linux-cli-tips.py
     ______________________________________________________________________________ 
    /                                                                              \
    | You can press Ctrl-D to exit a terminal in place of `exit` since Ctrl-D      |
    | sends the EOT character (end of transmission). It also works in other        |
    | situations in which a program reads commands from the standard input (like   |
    | `python`).                                                                   |
    \_   __________________________________________________________________________/
      | /
      |/
    $ python2 linux-cli-tips.py
     ______________________________________________________________________________ 
    /                                                                              \
    | `id -un` is the same as `whoami`. They both print the user name.             |
    \_   __________________________________________________________________________/
      | /
      |/

## License

MIT
