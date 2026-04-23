import pytest
import tkinter as tk
from unittest.mock import patch, MagicMock
import os
import sys

# Adiciona o diretório jnlp_launcher ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gui import JnlpLauncherApp

@pytest.fixture
def root():
    root = tk.Tk()
    yield root
    root.destroy()

@patch("gui.filedialog.askopenfilename")
def test_gui_select_file(mock_ask, root):
    app = JnlpLauncherApp(root)
    mock_ask.return_value = "C:/test.jnlp"
    
    app.select_file()
    
    assert app.selected_file.get() == "C:/test.jnlp"
    assert str(app.launch_btn["state"]) == "normal"

@patch("gui.launch_jnlp")
@patch("gui.messagebox.showinfo")
def test_gui_launch_success(mock_info, mock_launch, root):
    app = JnlpLauncherApp(root)
    app.selected_file.set("C:/test.jnlp")
    mock_launch.return_value = True
    
    app.launch()
    
    mock_launch.assert_called_once_with("C:/test.jnlp")
    mock_info.assert_called_once()

@patch("gui.launch_jnlp")
@patch("gui.messagebox.showerror")
def test_gui_launch_failure(mock_error, mock_launch, root):
    app = JnlpLauncherApp(root)
    app.selected_file.set("C:/test.jnlp")
    mock_launch.return_value = False
    
    app.launch()
    
    mock_launch.assert_called_once_with("C:/test.jnlp")
    mock_error.assert_called_once()
