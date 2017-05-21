#!/usr/bin/env python3.4

from flask import Flask, render_template, jsonify, request
import time
import trie

# application context
app = Flask(__name__)
trie_index = trie.Trie()

@app.route("/")
def hello():
    return render_template('frontpage.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    start = time.time()
    result_list = []
    # validate query
    if query is not None and query is not "":
        # do the query
        #result will be the list of word completions
        result_list = trie_index.get_completions(query)
    end = time.time()

    result = {"query": query, 'results':result_list[:10], 'server_time':str(int(end-start))+"seconds"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
