import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import os
import sys

# Adiciona o diretório jnlp_launcher ao path para importar os módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from launcher import launch_jnlp

def test_launch_jnlp_file_not_found(caplog):
    with caplog.at_level("ERROR"):
        result = launch_jnlp("non_existent_file.jnlp")
        assert result is False
        assert "Arquivo não encontrado" in caplog.text

def test_launch_jnlp_wrong_extension(tmp_path, caplog):
    wrong_file = tmp_path / "test.txt"
    wrong_file.write_text("dummy content")
    
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0)
        with patch("subprocess.Popen") as mock_popen:
            result = launch_jnlp(str(wrong_file))
            assert "Extensão inesperada" in caplog.text

@patch("subprocess.run")
@patch("subprocess.Popen")
def test_launch_jnlp_success(mock_popen, mock_run, tmp_path):
    jnlp_file = tmp_path / "test.jnlp"
    jnlp_file.write_text("dummy jnlp content")
    
    # Simula javaws -help funcionando
    mock_run.return_value = MagicMock(returncode=0)
    
    result = launch_jnlp(str(jnlp_file))
    
    assert result is True
    mock_popen.assert_called_once()
    assert "javaws" in mock_popen.call_args[0][0]

@patch("subprocess.run")
def test_launch_jnlp_javaws_not_found(mock_run, tmp_path, caplog):
    jnlp_file = tmp_path / "test.jnlp"
    jnlp_file.write_text("dummy jnlp content")
    
    # Simula javaws não encontrado
    mock_run.side_effect = FileNotFoundError
    
    with caplog.at_level("CRITICAL"):
        result = launch_jnlp(str(jnlp_file))
        assert result is False
        assert "javaws não encontrado no PATH" in caplog.text
