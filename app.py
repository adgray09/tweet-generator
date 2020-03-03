from flask import Flask, render_template
from generate_sentence import generate_sentence
import os
from read_file import read_file
from markov import MarkovChain

app = Flask(__name__)

@app.route('/')
def render_page():
        
    my_list = read_file('tintern_abbey.txt')
    chain = MarkovChain(my_list)
    num_words = int(10) - 1
    my_sentence = chain.walk(num_words)
    print(my_sentence)
    return render_template('index.html', sentence=my_sentence)
    # print(type(of thing you are looping through))

if __name__ == '__main__':
    app.run(debug=True)