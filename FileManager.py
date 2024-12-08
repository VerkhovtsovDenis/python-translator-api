from typing import List
from pathlib import Path
import os

class FileManager:
    PROJECT_DIR = Path(__file__).parent

    @staticmethod
    def create_file(relative_path: str, data: List[str]) -> None:
        path = f'{FileManager.PROJECT_DIR}{relative_path}'
        with open(path, 'w') as file:
            for line in data:
                file.write(line)

    @staticmethod
    def change_path_for_os(path: str):
        """преобразует путь под ос."""

        if os.name == "posix":
            path = path.replace('\\', '/')
        elif os.name == "nt":
            path = path.replace('/', '\\')
        return path
        
    
    @staticmethod
    def get_code(relative_path: str, isrstrip=False) -> str:
        path = f'{FileManager.PROJECT_DIR}{relative_path}'
        path = FileManager.change_path_for_os(path)

        code: str = ''
        with open(path, 'r', encoding='utf-8') as file:
            codelines = file.readlines()
        if isrstrip:
            codelines = [line[:-1] for line in codelines]
        code = ''.join(codelines)
        return code