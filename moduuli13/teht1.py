
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/alkuluku/<int:luku>")
def alkuluku(luku):
    on_alkuluku = True

    if luku < 2:
        on_alkuluku = False
    else:
        for i in range(2, luku):
            if luku % i == 0:
                on_alkuluku = False
                break

    return jsonify({
        "Number": luku,
        "isPrime": on_alkuluku
    })


app.run(port=3000)
