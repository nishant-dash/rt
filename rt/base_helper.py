from rich.console import Console
from rich.table import Table
from rich import box

# Initialize console object for print
console = Console()


class BaseToRichTable:
    def __init__(self, **kwargs):
        """Initialize input dict as class attributes."""
        for k, v in kwargs.items():
            setattr(self, k, v)

    def load(self, data) -> {}:
        """Load data in from a file or variable."""
        loaded_data = None
        return loaded_data

    def create_table(self) -> Table():
        """Create a rich table object."""
        return Table(box=box.ROUNDED, highlight=not self.suppress)

    def run(self, stdin_data, skip_load: str = False) -> None:
        """Load stdin as json and transform into rich table."""
        if skip_load:
            data = stdin_data
        else:
            data = self.load(stdin_data)
        if not data:
            console.print(f"Can not load stdin into {type(self).__name__}")

        # Initialize table object and misc.
        table = self.create_table()
        td = type(data)
        columns = None

        # List Logic
        if td == list:
            columns = [k for k in data[0].keys()]
            for c in columns:
                table.add_column(c)
            for r in data:
                temp_row = [str(v) for v in r.values()]
                table.add_row(*temp_row)
        elif td == dict:
            # Show Logic
            table.add_column("Key")
            table.add_column("Value")
            for k, v in data.items():
                table.add_row(k, str(v))
        else:
            console.print(f"Unsupported type {td}")
            return None

        console.print(table)
