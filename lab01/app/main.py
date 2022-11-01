from flask import Blueprint, render_template

server=Blueprint('main', __name__, url_prefix='/')

@server.route('/')
def main():
    return "Hello "