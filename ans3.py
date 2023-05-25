#!/usr/bin/env python3

import fire

def sayIt():
    
    print('Calling the say It  method')


class Cli():
    def __init__(self):
         self.sayIt = sayIt

if __name__ == '__main__':
    fire.Fire(Cli)
    
