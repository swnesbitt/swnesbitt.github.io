import re
from pathlib import Path

import bibtexparser
from bibtexparser.bparser import BibTexParser

HIGHLIGHT_NAME = "Nesbitt"


def _clean(text):
    """Strip common LaTeX markup from a string."""
    text = re.sub(r"\{\\[a-zA-Z]+\s*\}", "", text)   # {\cmd}
    text = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", text)  # \cmd{text}
    text = re.sub(r"[{}]", "", text)
    return text.strip()


def _initials(first):
    return " ".join(p[0] + "." for p in first.split() if p)


def _format_authors(raw):
    if not raw:
        return ""
    parts = [a.strip() for a in re.split(r"\s+and\s+", raw, flags=re.IGNORECASE)]
    out = []
    for part in parts:
        if part.strip().lower() == "others":
            out.append("co-authors")
            continue
        if "," in part:
            last, first = part.split(",", 1)
            last, first = last.strip(), first.strip()
        else:
            tokens = part.split()
            last, first = tokens[-1], " ".join(tokens[:-1])
        name = f"{_clean(last)}, {_initials(first)}" if first else _clean(last)
        if HIGHLIGHT_NAME in last:
            name = f"**{name}**"
        out.append(name)

    if len(out) == 1:
        return out[0]
    if len(out) == 2:
        return f"{out[0]} and {out[1]}"
    return ", ".join(out[:-1]) + f", and {out[-1]}"


def _doi_link(entry):
    doi = entry.get("doi", "").strip()
    url = entry.get("url", "").strip()
    if doi:
        return f" [[doi](https://doi.org/{doi})]"
    if url:
        return f" [[link]({url})]"
    return ""


def _format_entry(entry):
    etype = entry.get("ENTRYTYPE", "misc").lower()
    authors = _format_authors(entry.get("author", entry.get("editor", "")))
    year = entry.get("year", "")
    title = _clean(entry.get("title", ""))
    link = _doi_link(entry)

    if etype == "article":
        journal = _clean(entry.get("journal", ""))
        volume = entry.get("volume", "")
        pages = entry.get("pages", "").replace("--", "–")
        vol_pages = f", **{volume}**" if volume else ""
        if pages:
            vol_pages += f", {pages}"
        return f"- {authors}, {year}: {title}. *{journal}*{vol_pages}.{link}"

    if etype in ("book", "incollection"):
        publisher = _clean(entry.get("publisher", ""))
        numpages = entry.get("pages", entry.get("numpages", ""))
        pp = f", {numpages} pp." if numpages else "."
        return f"- {authors}, {year}: *{title}*. {publisher}{pp}{link}"

    if etype == "phdthesis":
        school = _clean(entry.get("school", ""))
        return f"- {authors}, {year}: *{title}*. Ph.D. Dissertation, {school}.{link}"

    if etype == "mastersthesis":
        school = _clean(entry.get("school", ""))
        return f"- {authors}, {year}: *{title}*. M.S. Thesis, {school}.{link}"

    if etype == "inproceedings":
        booktitle = _clean(entry.get("booktitle", ""))
        return f"- {authors}, {year}: {title}. *{booktitle}*.{link}"

    # misc / techreport / unpublished / preprint
    note = _clean(entry.get("howpublished", entry.get("note", entry.get("journal", ""))))
    extra = f". {note}" if note else "."
    return f"- {authors}, {year}: {title}{extra}{link}"


def on_page_markdown(markdown, **kwargs):
    placeholder = "{{ bibliography }}"
    if placeholder not in markdown:
        return markdown

    bib_path = Path("references.bib")
    if not bib_path.exists():
        return markdown.replace(
            placeholder,
            "> **Note:** Place your BibTeX file at `references.bib` in the project root to populate this section.",
        )

    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    with open(bib_path, encoding="utf-8") as f:
        db = bibtexparser.load(f, parser)

    by_year = {}
    for entry in db.entries:
        year = entry.get("year", "Unknown")
        by_year.setdefault(year, []).append(entry)

    lines = []
    for year in sorted(by_year, key=lambda y: int(y) if y.isdigit() else 0, reverse=True):
        lines.append(f"\n### {year}\n")
        for entry in by_year[year]:
            lines.append(_format_entry(entry))

    return markdown.replace(placeholder, "\n".join(lines))
