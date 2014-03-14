#!/usr/bin/env python2
# started 25.08.2009

from random import randint

class color:
    normal = "\033[0m"
    black = "\033[0;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    blue = "\033[0;34m"
    magenta = "\033[0;35m"
    cyan = "\033[0;36m"
    white = "\033[0;37m"
    b_black = "\033[1;30m"
    b_red = "\033[1;31m"
    b_green = "\033[1;32m"
    b_yellow = "\033[1;33m"
    b_blue = "\033[1;34m"
    b_magenta = "\033[1;35m"
    b_cyan = "\033[1;36m"
    b_white = "\033[1;37m"

def block_text(text, maxlen = 80):
    """Returns same-width text."""
    lines = ['']
    k = 0
    for word in text.split(' '):
        if len(word) + len(lines[k]) + 1> maxlen:
            k += 1
            lines.append('')
        lines[k] += ' ' + word
        while len(lines[k]) > maxlen:
            lines.append(lines[k][maxlen:])
            lines[k] = lines[k][:maxlen]
            k += 1
    lines = [x[1:] for x in lines] # remove the extra space
    lines = [x + ' '*(maxlen - len(x)) for  x in lines] # equalize the lines
    return '\n'.join(lines)

def frame(text, text_color = color.white, frame_color = color.yellow):
    lines = text.split('\n')
    maxlen = len(lines[0])

    text  = frame_color + ' _' + '_' * maxlen + '_ \n'
    text += '/ ' + ' ' * maxlen + ' \\\n'
    for l in lines:
        text += '| ' + text_color + l + frame_color + ' |\n'
    text += '\_   ' + '_'*(maxlen-3)  + '_/\n'
    text += '  | /\n'
    text += '  |/' + color.normal
    return text

if __name__ == '__main__':
    maxlen = 80 - 4
    list = [ x for x in open('texts').read().split('\n') if len(x) > 0 and x[0] != "#" ]
    message = list[randint(0, len(list) - 1)]
    print frame(block_text(message, maxlen), color.yellow, color.b_black)
