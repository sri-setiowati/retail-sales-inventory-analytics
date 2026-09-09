# Python Analysis Pipeline

`data_preparation.py` is the reproducible pipeline used to validate the raw data, create analytical fields, aggregate sales performance, classify inventory risk, and export Power BI-ready tables.

## Run

```bash
pip install -r ../requirements.txt
python data_preparation.py
```

The script expects the files in `../data/raw/` and writes outputs to `../data/processed/`.
