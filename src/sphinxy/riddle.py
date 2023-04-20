from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """_summary_

        Args:
            answer (str): _description_

        Returns:
            bool: _description_
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """_summary_

        Yields:
            Iterator[str]: _description_
        """
        yield from iter(self.answer)
