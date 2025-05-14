from flask import Flask, request, render_template, send_file, jsonify
from utils import plot_expression
import os
# goal: user input (NO y= something or f(x)), then feed it into plot_expression() with user input range, finally, feed it back/download it

app = Flask(__name__)

@app.route("/")
def home(): return render_template("index.html")

@app.route("/getimg")
def serve_graph():
    return send_file('graph.png', mimetype='image/png')

        
@app.route("/plot", methods=["POST"])
def plot_graph():
    if os.path.exists("graph.png"):
        os.remove("graph.png")
    try:
        data = request.get_json()
        expression = data.get("expression")
    except Exception as e:
        return jsonify({"error": f"Invalid JSON: {str(e)}"}), 400
    plot_expression(expression=expression, x_range=(-10, 10), output_file="graph.png")
    return jsonify({}), 200

if __name__ == "__main__":
    app.run(debug=True)