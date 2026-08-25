# JLPT N5 Listening and Practice Dataset

This private repository contains the two supplied N5 audio archives normalized into a deterministic, APK-friendly layout. The integration entry point is [`metadata/catalog.json`](metadata/catalog.json). Every audio record contains a repository-relative `path`, stable `id`, source filename/path, codec, duration, byte size, and SHA-256 checksum.

## Contents

| Collection | Audio assets | Organization |
|---|---:|---|
| Textbook | 251 | Lessons 1–35; vocabulary/kotoba, bunkei, reibun, kaiwa, mondai, and Renshuu C where present |
| Model test | 147 | Source groups 1–29; original N5 track codes retained in `source_code` |

The textbook archive also contains five scanned PDFs and two JPEG reference assets. The canonical files are preserved under [`references/source-documents/`](references/source-documents/), and page-level machine OCR is under [`references/ocr/`](references/ocr/). The OCR is explicitly **not safe for automatic answer scoring**; use the original scanned PDF when verifying answers. Temporary Office/OS files were excluded and listed in [`metadata/excluded_files.json`](metadata/excluded_files.json).

## APK usage

Bundle the repository's `audio/` directory with the app and resolve each record's `path` relative to the asset root. Do not derive asset identity from display filenames. For example, the record with `id` `textbook-lesson-01-vocabulary` points to `audio/textbook/lesson-01/lesson-01-vocabulary.mp3`. WMA sources from lessons 26–35 were converted to MP3; the record retains `converted_from: "wma"`.

Run `python3 scripts/validate_dataset.py` before shipping. The validator checks file existence, exact byte sizes, SHA-256 checksums, unique IDs/paths, and positive durations.

## Accuracy note

Audio metadata is deterministically validated. No answer is inferred from audio or OCR. The preserved `Fukushu Answer.pdf`, `Mondai.pdf`, and `Renshu B C.pdf` remain the authoritative source materials for answer verification.
