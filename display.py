from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def show_repos(repos):
    table = Table(
        title=" GitHub Trending Repositories",
        box=box.SQUARE,
        show_lines=True,
        header_style="bold cyan"
    )

    table.add_column("#",         style="dim",          width=4)
    table.add_column("Repository",style="bold white",   min_width=25)
    table.add_column("⭐ Stars",  style="yellow",       justify="right")
    table.add_column("Language",  style="magenta")
    table.add_column("Description",style="white",       max_width=45)
    table.add_column("URL",       style="blue underline")

    for i, repo in enumerate(repos, start=1):
        table.add_row(
            str(i),
            repo["full_name"],
            f"{repo['stargazers_count']:,}",
            repo.get("language") or "N/A",
            repo.get("description") or "—",
            repo["html_url"],
        )

    console.print(table)
