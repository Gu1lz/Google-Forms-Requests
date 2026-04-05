# Google Forms Requests

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

## About

A Python script that automates form submissions to Google Forms. The tool scrapes a given Google Form URL to extract its field entry IDs and answer options, saves them to a local file, and then fires multiple concurrent POST requests to the form's response endpoint using threads.

## How It Works

The script runs in two stages:

**Stage 1 — Form scraping (`pega`)**

Given a Google Form URL (full or just the form ID), the script fetches the form HTML and parses it with BeautifulSoup. It extracts each question's `entry.*` field ID and its pre-defined answer options, then writes everything to `entry.txt` alongside the submission endpoint URL.

**Stage 2 — Bulk submission (`ir`)**

Reads `entry.txt`, builds the POST payload as a JSON object, and spawns 10 threads simultaneously. Each thread sends 100 POST requests to the form's `formResponse` endpoint, resulting in up to 1,000 submissions per run.

## Dependencies

- [requests](https://pypi.org/project/requests/) — HTTP requests for fetching and submitting the form
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) — HTML parsing to extract field entry IDs
- [threading](https://docs.python.org/3/library/threading.html) — Standard library module for concurrent execution

## Installation

```bash
# Clone the repository
git clone https://github.com/Gu1lz/Google-Forms-Requests.git
cd Google-Forms-Requests

# Install dependencies
pip install requests beautifulsoup4
```

## Usage

```bash
python Main.py
```

When prompted, enter either the full Google Form URL or just the form ID:

```
# Full URL
https://docs.google.com/forms/d/e/<FORM_ID>/viewform

# Or just the form ID
1FAIpQLSd...
```

The script will scrape the form, write the parsed entries to `entry.txt`, and immediately begin sending bulk submissions across 10 concurrent threads.

## Technical Details

| Feature | Details |
|---|---|
| Threads | 10 concurrent threads per run |
| Requests per thread | 100 POST requests |
| Total submissions per run | Up to 1,000 |
| URL input | Accepts full URL or bare form ID |
| Output file | `entry.txt` — overwritten on each run |

## Notes

- `entry.txt` is automatically generated and overwritten on every run. Do not edit it manually.
- The script targets the `/formResponse` endpoint, which is the same endpoint used by actual form submissions.
- Google Forms does not require authentication for public forms, so no API key or OAuth is needed.

## Author

**Gu1lz**  
[github.com/Gu1lz](https://github.com/Gu1lz)

---

> Project developed for learning purposes, exploring HTTP requests, HTML parsing, and multithreading in Python.
