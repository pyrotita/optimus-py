from project_db import SnippetDb


def main() -> None:
    for i in range(1_000_000):
        record: int = SnippetDb.set_snippet(
            name=f"register_{i}",
            content="any value",
        )

        if record == 0:
            print("error inserting ", i)


if __name__ == "__main__":
    main()
