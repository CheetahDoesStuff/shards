from __future__ import annotations

from termcolor import colored
from datetime import datetime
from pathlib import Path
import re
from os import mkdir

class Logger():
    def __init__(self, name: str,
                sub_name: str = "",
                do_timestamps: bool=True,
                do_log_saving: bool=False,
                print_logs: bool=True,
                do_saved_log_decolouring: bool=True,
                log_save_folder: str="logs",
                ):
        
        self.ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        
        self.name = name
        if sub_name.strip() != "":
            self.sub_name = "/" + sub_name
        else:
            self.sub_name = ""

        self.timestamps = do_timestamps
        self.log_saving = do_log_saving
        self.save_folder = log_save_folder
        self.print = print_logs
        self.decoulor = do_saved_log_decolouring

        self.start_timestamp = str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))



    def _handle_log(self, message):
        if self.print:
            print(message)
        
        if self.decoulor:
            message = self.ansi_escape.sub('', message)
        
        if not Path(self.save_folder).exists():
            Path(self.save_folder).mkdir(parents=True, exist_ok=True)

        if self.log_saving:
            with open(Path(self.save_folder) / f"{self.start_timestamp}.log", "a+") as f:
                f.write(message + "\n")
    


    def _gen_log(self, message):
        timestamp = ""
        if self.timestamps:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{colored(timestamp, 'green')} ( {self.name}{self.sub_name} ) {colored('|', 'green')} {message}"



    def _log_with_type(self, log_type, message, sublog=False, sublog_layer=1):
        spacing = ('    ' * sublog_layer + "- ") if sublog else ' '
        log = self._gen_log(f"{log_type}{spacing}{message}")
        self._handle_log(log)

    

    def log(self, message, sublog=False, sublog_layer=1):
        self._log_with_type("[LOG]", message, sublog, sublog_layer)

    def info(self, message, sublog=False, sublog_layer=1):
        self._log_with_type(colored("[INFO]", "green"), message, sublog, sublog_layer)

    def warn(self, message, sublog=False, sublog_layer=1):
        self._log_with_type(colored("[WARN]", "yellow"), message, sublog, sublog_layer)

    def error(self, message, sublog=False, sublog_layer=1):
        self._log_with_type(colored("[ERROR]", "red"), message, sublog, sublog_layer)

    def critical(self, message, sublog=False, sublog_layer=1):
        self._log_with_type(colored("[CRITICAL]", "red"), message, sublog, sublog_layer)

    def raw(self, message, sublog=False, sublog_layer=1):
        log = f"{' ' * sublog_layer}{message}" if sublog else message
        self._handle_log(log)
    
    def space(self):
        self._handle_log("")

    
    def make_child_logger(self, child_name: str) -> Logger: # type: ignore
        child = Logger(
            self.name, 
            sub_name=child_name, 
            do_timestamps=self.timestamps, 
            do_log_saving=self.log_saving, 
            print_logs=self.print,
            do_saved_log_decolouring=self.decoulor,
            log_save_folder=self.save_folder
            )
        
        child.start_timestamp = self.start_timestamp
        return child