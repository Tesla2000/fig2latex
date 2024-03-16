from pathlib import Path


def fig2latex(
    figure_path: Path,
    label: str = None,
    caption: str = None,
    centered: bool = True,
    text_width: float = None,
    placement: str = None,
) -> str:
    """
    Converts a figure to LaTeX format.

    :param figure_path: Path to the figure file.
    :type figure_path: Path
    :param label: Label for the figure.
    :type label: str, optional
    :param caption: Caption for the figure.
    :type caption: str, optional
    :param centered: Whether to center the figure. Default is True.
    :type centered: bool, optional
    :param text_width: Width of the figure as a fraction of text width.
    :type text_width: float, optional
    :param placement: LaTeX placement specifier for the figure.
    :type placement: str, optional
    :return: LaTeX representation of the figure.
    :rtype: str

    Example:
        >>> fig2latex(Path("example.png"), label="fig:example", caption="Example Figure")
        '\\begin{figure}\\n\\includegraphics{example.png}\\n\\caption{Example Figure}\\n\\label{fig:example}\\n\\end{figure}'
    """
    return (
        r"\begin{figure}" + (("[" + placement + "]") if placement is not None else "") +
        "\n"
        + (r"\centering" "\n" if centered else "")
        + r"\includegraphics"
        + (r"[width={}\textwidth]".format(text_width) + "{" if text_width is not None else "{")
        + str(figure_path)
        + "}\n"
        + (r"\caption{" + caption + "}\n" if caption else "")
        + (r"\label{" + label + "}\n" if label else "")
        + r"\end{figure}"
    )
