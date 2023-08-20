# NLP tech assessment

## Main task

- Theme classification
- Sentiment analysis
- [LLM demo](https://colab.research.google.com/drive/1xQC9Qoo0ETPd76k1o09yMOwHyx7TBVAI#scrollTo=S9T3ujkVIAbj)


## Data

- `ce_cn_raw.csv`: cleaned ce_cn raw data
- `xwlb_raw.csv`: cleaned xwlb raw data
- `ce_cn_labeled.csv`: cleaned and labeled ce_cn data
- `xwlb_labeled.csv`: cleaned and labled xwlb_data


## Colab

Compute device limitation, model training task were implemented on the colab

For the Theme classification and Sentiment model: [colab](https://colab.research.google.com/drive/1jzfzf5uCpWDpH5qF4gqKX0J9pu2XD3dc#scrollTo=KmCOXMtlWUVd)

For the LLM demo [colab](https://colab.research.google.com/drive/1xQC9Qoo0ETPd76k1o09yMOwHyx7TBVAI#scrollTo=S9T3ujkVIAbj) 

## Local

- `eda.ipynb` is the main script
- `tools.py` is used to remove the stopwords
- `download.py` is used to download the source data
- `requirements.txt` runtime requirements