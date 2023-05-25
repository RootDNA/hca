#!/usr/bin/env python3

import click

@click.command()
@click.option("--name",default='p',help='Enter your name as argument')
def sayIt(name):
    if name[0] != "p":
        print(name)

if __name__ == '__main__':
     
    sayIt()
