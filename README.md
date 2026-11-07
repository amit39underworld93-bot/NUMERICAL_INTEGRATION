# Numerical Integration Engine ⨋

A robust, pure Python Command-Line Interface (CLI) application designed to evaluate definite integrals mathematically from scratch. 
This toolkit provides highly accurate numerical approximations for single (1D), double (2D), and triple (3D) integrals using core computational theorems, without relying on external scientific libraries like SciPy

## 🚀 Key Features

- **Multi-Dimensional Integration:** Capable of approximating definite integrals for $1D$, $2D$, and $3D$ mathematical functions over user-defined continuous intervals.

- **Three Core Approximation Methods:**

  - Midpoint Rule: Approximates the integral using the center point of each sub-interval block.

  - Trapezoidal Rule: Evaluates the area under the curve (or volume under the surface) using trapezoidal bounds.
  
  - Simpson's 1/3 Rule: Applies parabolic arcs for high-precision approximations.
 
- **Built-in Mathematical Safeguards:** Automatically validates that the number of sub-intervals ($m, n, o$) are strictly even when Simpson's 1/3 Rule is selected, preventing inaccurate computations.

- **Dynamic Parsing:** Uses Python's `eval()` method safely with a restricted local namespace to dynamically process complex user-inputted string expressions (e.g., `sin(x) * exp(y)`).

## 🛠️ Tech Stack

- **Language:** Python 3

- **Core Logic:** Built-in math module (for standard functions like trigonometric, logarithmic, and exponential) and raw nested loop structures for multidimensional summation.

## 💻 How to Run (Installation & Execution)

*This is a pure Python project with zero external dependencies (no `pip install required`).*

1. ### Clone the repository:

   git clone https://github.com/amit39underworld93-bot/NUMERICAL_INTEGRATION.git cd NUMERICAL_INTEGRATION

2. ### Execute the desired script:

   *The repository includes dedicated scripts for each dimension, plus a unified engine.*

   - **For 1D Integration:** `python3 main1_D.py`

   - **For 2D Integration:** `python3 main2_D.py`
  
   - **For 3D Integration:** `python3 main3_D.py`
  
   - **For Unified Engine:** `python3 numerical_integration.py`
  
## 📸 Usage Example

*When you run the unified `numerical_integration.py script`, follow the interactive prompts:*

***Example: 2D Double Integration***

Enter the dimension between 1 to 3: 2

==== CHOOSE APPROXIMATION METHOD ====
1. Midpoint Rule

2. Trapezoidal Rule

3. Simpson's 1/3 Rule

Enter your choice between 1 to 3: 3

Enter the function f(x, y): x**2 + y**2

Enter the value of a (lower limit x): 0

Enter the value of b (upper limit x): 2

Enter the value of c (lower limit y): 0

Enter the value of d (upper limit y): 2

Enter the value of m (sub-intervals for x): 100

Enter the value of n (sub-intervals for y): 100

***The application will then output the precise numerical approximation of the double integral.***
