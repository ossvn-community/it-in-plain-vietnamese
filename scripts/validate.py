from collections import Counter
from datetime import datetime
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS = ROOT / "concepts"

ALLOWED_CATEGORIES = {
    "software-development",
    "git-open-source",
    "web",
    "systems-networking",
    "data",
    "security",
    "cloud-devops",
    "ai",
    "embedded-iot",
}
ALLOWED_STATUS = {"draft", "reviewed"}
REQUIRED_FIELDS = {
    "title",
    "category",
    "core",
    "status",
    "last_reviewed",
    "reviewers",
}
SKIP_FILES = {CONCEPTS / "README.md", CONCEPTS / "_template.md"}
SOURCE_LINK = re.compile(r"^-\s+\[[^\]]+\]\(https?://[^)\s]+\)$")


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'\"', "'"}:
        return value[1:-1]
    return value


def parse_front_matter(path: Path) -> tuple[dict[str, str], list[str], int]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening front matter delimiter")

    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValueError("missing closing front matter delimiter") from exc

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid front matter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"invalid front matter key: {line}")
        if key in metadata:
            raise ValueError(f"duplicate front matter field: {key}")
        metadata[key] = value.strip()

    return metadata, lines, end + 1


def validate_sources(relative: Path, lines: list[str], body_start: int) -> list[str]:
    errors: list[str] = []
    source_header = None

    for index in range(body_start, len(lines)):
        if lines[index].strip() == "## Nguồn":
            source_header = index
            break

    if source_header is None:
        return [f"{relative}: missing '## Nguồn' section"]

    source_count = 0
    for line in lines[source_header + 1 :]:
        stripped = line.strip()
        if stripped.startswith("## "):
            break
        if not stripped or stripped.startswith("<!--"):
            continue
        if not SOURCE_LINK.fullmatch(stripped):
            errors.append(
                f"{relative}: source must be a direct Markdown link bullet: {stripped}"
            )
        else:
            source_count += 1

    if source_count == 0:
        errors.append(f"{relative}: '## Nguồn' must contain at least one Markdown link")

    return errors


def validate() -> list[str]:
    errors: list[str] = []
    core_counts: Counter[str] = Counter()
    concept_count = 0

    for path in sorted(CONCEPTS.rglob("*.md")):
        if path in SKIP_FILES:
            continue

        concept_count += 1
        relative = path.relative_to(ROOT)

        try:
            metadata, lines, body_start = parse_front_matter(path)
        except ValueError as exc:
            errors.append(f"{relative}: {exc}")
            continue

        missing = REQUIRED_FIELDS - metadata.keys()
        if missing:
            errors.append(f"{relative}: missing metadata: {', '.join(sorted(missing))}")
            continue

        title = clean_scalar(metadata["title"])
        category = clean_scalar(metadata["category"])
        status = clean_scalar(metadata["status"])
        last_reviewed = clean_scalar(metadata["last_reviewed"])
        core = metadata["core"].strip()
        reviewers = metadata["reviewers"].strip()

        if not title:
            errors.append(f"{relative}: title must not be empty")

        if category not in ALLOWED_CATEGORIES:
            errors.append(f"{relative}: unsupported category: {category}")

        if path.parent == CONCEPTS:
            errors.append(f"{relative}: concept must live in a category folder")
        elif category != path.parent.name:
            errors.append(
                f"{relative}: category '{category}' does not match folder '{path.parent.name}'"
            )

        if core not in {"true", "false"}:
            errors.append(f"{relative}: core must be boolean true or false")
        elif core == "true":
            core_counts[category] += 1

        if status not in ALLOWED_STATUS:
            errors.append(f"{relative}: unsupported status: {status}")

        try:
            datetime.strptime(last_reviewed, "%Y-%m-%d")
        except ValueError:
            errors.append(f"{relative}: last_reviewed must use YYYY-MM-DD")

        if not (reviewers.startswith("[") and reviewers.endswith("]")):
            errors.append(f"{relative}: reviewers must use a YAML inline list")

        errors.extend(validate_sources(relative, lines, body_start))

    for category, count in sorted(core_counts.items()):
        if count > 5:
            errors.append(f"{category}: has {count} concepts with core: true; maximum is 5")

    if not errors:
        print(f"Concept validation passed ({concept_count} files).")

    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(f"- {problem}" for problem in problems))
        sys.exit(1)
