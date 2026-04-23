import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import logging
from pathlib import Path

from launcher import launch_jnlp

logger = logging.getLogger("JNLPLauncher.gui")

class JnlpLauncherApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("JNLP Launcher")
        self.root.geometry("500x200")
        self.root.resizable(False, False)

        # Variável para armazenar o caminho selecionado
        self.selected_file = tk.StringVar()

        self._build_ui()

    def _build_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título
        ttk.Label(
            main_frame,
            text="Iniciar arquivo Java Web Start (.jnlp)",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 20))

        # Área de seleção de arquivo
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=5)

        self.file_label = ttk.Label(
            file_frame,
            text="Nenhum arquivo selecionado",
            foreground="gray",
            wraplength=400
        )
        self.file_label.pack(side=tk.LEFT, padx=(0, 10))

        select_btn = ttk.Button(
            file_frame,
            text="Selecionar .jnlp",
            command=self.select_file
        )
        select_btn.pack(side=tk.RIGHT)

        # Botão de executar
        self.launch_btn = ttk.Button(
            main_frame,
            text="Executar javaws",
            command=self.launch,
            state=tk.DISABLED
        )
        self.launch_btn.pack(pady=15)

        # Barra de status
        self.status_var = tk.StringVar(value="Pronto")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            padding=5
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)

        # Rodapé com informação do log
        try:
            log_path = logging.getLogger("JNLPLauncher").handlers[0].baseFilename
            ttk.Label(
                main_frame,
                text=f"Logs: {log_path}",
                foreground="gray",
                font=("Segoe UI", 8)
            ).pack(side=tk.BOTTOM, pady=(5, 0))
        except (IndexError, AttributeError):
            pass

    def select_file(self):
        """
        Abre o diálogo de seleção de arquivo filtrando .jnlp.
        """
        file_path = filedialog.askopenfilename(
            title="Selecione um arquivo .jnlp",
            filetypes=[
                ("Arquivos JNLP", "*.jnlp"),
                ("Todos os arquivos", "*.*")
            ]
        )

        if file_path:
            self.selected_file.set(file_path)
            # Exibe apenas o nome do arquivo na interface
            self.file_label.config(text=Path(file_path).name, foreground="black")
            self.launch_btn.config(state=tk.NORMAL)
            self.status_var.set("Arquivo selecionado. Clique em 'Executar'.")
            logger.info(f"Arquivo selecionado: {file_path}")
        else:
            self.status_var.set("Seleção cancelada pelo usuário.")
            logger.debug("Seleção de arquivo cancelada.")

    def launch(self):
        """
        Executa o javaws com o arquivo selecionado e exibe o resultado.
        """
        file = self.selected_file.get()
        if not file:
            messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")
            return

        self.status_var.set("Iniciando javaws...")
        self.launch_btn.config(state=tk.DISABLED)
        self.root.update_idletasks()  # força atualização da interface

        success = launch_jnlp(file)

        if success:
            self.status_var.set("javaws iniciado! A aplicação Java deve abrir em breve.")
            messagebox.showinfo(
                "Sucesso",
                "O javaws foi executado. A aplicação Java Web Start será iniciada separadamente."
            )
            logger.info("Lançamento concluído.")
        else:
            try:
                log_file = logging.getLogger("JNLPLauncher").handlers[0].baseFilename
                extra_msg = f"Verifique o log para detalhes:\n{log_file}"
            except (IndexError, AttributeError):
                extra_msg = "Verifique os logs da aplicação."

            error_msg = (
                "Falha ao executar o javaws.\n\n"
                "Possíveis causas:\n"
                "- Java não está instalado ou javaws não está no PATH\n"
                "- O arquivo .jnlp está corrompido\n"
                f"{extra_msg}"
            )
            self.status_var.set("Erro ao executar javaws. Veja o log.")
            messagebox.showerror("Erro", error_msg)

        # Reabilita o botão para novas tentativas
        self.launch_btn.config(state=tk.NORMAL)
