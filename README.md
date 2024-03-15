fig2latex
=========

Introduction
------------
`fig2latex` is a Python utility for converting figures to LaTeX format. This utility simplifies the process of including
figures in LaTeX documents by generating the necessary LaTeX code.

Installation
------------
You can install `fig2latex` via pip:
pip install fig2latex

Usage
-----

```python
from pathlib import Path
from fig2latex import fig2latex

# Example usage:
figure_path = Path("example.png")
label = "fig:example"
caption = "Example Figure"
latex_code = fig2latex(figure_path, label=label, caption=caption)
print(latex_code)
```


Convert a figure to LaTeX format.

- Parameters:
  - figure_path (Path): Path to the figure file.
  - label (str, optional): Label for the figure.
  - caption (str, optional): Caption for the figure.
  - centered (bool, optional): Whether to center the figure. Default is True.
  - text_width (float, optional): Width of the figure as a fraction of text width.
  - placement (str, optional): LaTeX placement specifier for the figure.

- Returns:
  - str: LaTeX representation of the figure.

- Example:
  ```python
  fig2latex(Path("example.png"), label="fig:example", caption="Example Figure")
  ```

  Output:
  ```latex
  \begin{figure}
  \includegraphics{example.png}
  \caption{Example Figure}
  \label{fig:example}
  \end{figure}
  ```

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.
```
