#!/usr/bin/python

import progressbar

def get_next_in_seq(x: int) -> int:
    if x % 2 == 0:
        return int(x/2)
    else:
        return int(3*x + 1)


def count_length(start: int) -> int:
    count = 1
    next = get_next_in_seq(start)
    while(next != 1):
        next = get_next_in_seq(next)
        count += 1
    count += 1
    return count

def print_seq(start: int):
    print(start, end="")

    next = get_next_in_seq(start)
    while(next != 1):
        print(f'-->{next}', end="")
        next = get_next_in_seq(next)
    
    print(f'-->{next}')


if __name__ == '__main__':
    max_count = 0
    int_with_max_count = 0

    max_value = 1000000

    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('*'),' (',
           progressbar.ETA(), ') ',
          ]
    bar = progressbar.ProgressBar(max_value=max_value, widgets=widgets).start()

    for i in range(1, max_value):
        count = count_length(i)
        if count > max_count:
            max_count = count
            int_with_max_count = i
        bar.update(i)

    print(f'Max count is {max_count} for {int_with_max_count}')
