import dataclasses
from typing import Optional


@dataclasses.dataclass
class ForeignKey:
    name: str
    from_table: str
    from_column: str
    to_table: str
    to_column: str
    options: Optional[str] = None