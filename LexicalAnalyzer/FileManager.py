from typing import List
from pathlib import Path


class FileManager:
    PROJECT_DIR = Path(__file__).parent.parent

    @staticmethod
    def get_code(relative_path: str, isrstrip=False) -> str:
        path = f'{FileManager.PROJECT_DIR}{relative_path}'

        code: str = ''
        with open(path, 'r', encoding='utf-8') as file:
            codelines = file.readlines()
        if isrstrip:
            codelines = [line[:-1] for line in codelines]
        code = ''.join(codelines)
        return code

    @staticmethod
    def create_file(relative_path: str, data: List[str]) -> None:
        path = f'{FileManager.PROJECT_DIR}{relative_path}'
        with open(path, 'w') as file:
            for line in data:
                file.write(line)
