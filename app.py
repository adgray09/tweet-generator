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
    
    my_list2 = read_file("the_rime.txt")
    chain2 = MarkovChain(my_list2)
    num_words2 = int(10) - 1
    my_sentence2 = chain2.walk(num_words2)    
    
    return render_template('index.html', sentence=my_sentence, sentence2=my_sentence2)

if __name__ == '__main__':
    app.run(debug=True)