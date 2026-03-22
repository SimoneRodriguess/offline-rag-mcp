import argparse


def embed(text: str) -> list[float]:
    raise NotImplementedError


def ingest_file(filepath: str) -> None:
    raise NotImplementedError


def ingest_all(docs_dir: str = "./docs") -> None:
    raise NotImplementedError


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--path")
    group.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.all:
        ingest_all()
    else:
        ingest_file(args.path)