import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plot_expression(expression, x_range=(-10, 10), output_file="graph.png"):
    x = sp.symbols('x')
    try:
        expr = sp.sympify(expression)
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"

    f_lambdify = sp.lambdify(x, expr, "numpy")
    x_values = np.linspace(x_range[0], x_range[1], 400)

    try:
        y_values = f_lambdify(x_values)
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f"f(x) = {expression}", color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graph of the Function")
    plt.legend()
    plt.savefig(output_file)
    return output_file