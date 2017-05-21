#!/usr/bin/env python3.4

from flask import Flask, render_template, jsonify, request

import trie

# application context
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('frontpage.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    print ("query is in flask app " + query)

    result_list = []

    # validate query
    if query is not None and query is not "":
        # do the query
        #result will be the list of word completions
        trie_index = trie.Trie()
        result_list = trie_index.get_completions(query)

    result = {"query": query, 'results':result_list}
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
