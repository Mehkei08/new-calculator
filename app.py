from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template inside Python (to keep it simple)
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
</head>
<body style="font-family: Arial; text-align:center; margin-top:50px;">
    <h2>🔢 Simple Flask Calculator</h2>
    <form method="post">
        <input type="number" name="num1" step="any" required>
        <select name="operation">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" name="num2" step="any" required>
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/wtfever", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operation"]

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2 if num2 != 0 else "Error: Divide by zero"
        except Exception as e:
            result = f"Error: {e}"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
