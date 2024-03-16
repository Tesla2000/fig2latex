import unittest
from pathlib import Path

from src.fig2latex import fig2latex


class TestFig2Latex(unittest.TestCase):

    def test_basic_functionality(self):
        figure_path = Path("example.png")
        expected_output = (
            r"\begin{figure}" + "\n"
                                r"\centering" + "\n"
            + r"\includegraphics{" + str(figure_path) + "}\n"
            + r"\end{figure}"
        )
        self.assertEqual(fig2latex(figure_path), expected_output)

    def test_with_caption_and_label(self):
        figure_path = Path("example.png")
        label = "fig:example"
        caption = "Example Figure"
        expected_output = (
            r"\begin{figure}" + "\n"
                                r"\centering" + "\n"
            + r"\includegraphics{" + str(figure_path) + "}\n"
            + r"\caption{" + caption + "}\n"
            + r"\label{" + label + "}\n"
            + r"\end{figure}"
        )
        self.assertEqual(fig2latex(figure_path, label=label, caption=caption), expected_output)

    def test_centered(self):
        figure_path = Path("example.png")
        expected_output = (
            r"\begin{figure}" + "\n"
            + r"\includegraphics{" + str(figure_path) + "}\n"
            + r"\end{figure}"
        )
        self.assertEqual(fig2latex(figure_path, centered=False), expected_output)

    def test_placement(self):
        figure_path = Path("example.png")
        expected_output = (
            r"\begin{figure}[h]" + "\n"
            + r"\centering" + "\n"
            + r"\includegraphics{" + str(figure_path) + "}\n"
            + r"\end{figure}"
        )
        self.assertEqual(fig2latex(figure_path, placement='h'), expected_output)


if __name__ == '__main__':
    unittest.main()
