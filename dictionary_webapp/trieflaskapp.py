#!/usr/bin/env python3.4

from flask import Flask, render_template, jsonify, request
from trie import trie

# application context
app = Flask(__name__)

t = trie.Trie(bootstrap_dict=True)

@app.route("/")
def hello():
    return render_template('frontpage.html')

@app.route('/search')
def search():
    query = request.args.get('q')

    # validate query
    if query is not "" or query is not None:
        # do the query
        #result will be the list of completions_word
        completions_result = t.get_completions(query)

    result = {"query": query, 'results':completions_result}
    return jsonify(result)

    #t = trie_cli.func(code)
    #return render_template('frontpage.html', test = t)

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=5002)