from typing import List, Callable, Optional, Union
import pandas as pd
from collections import Counter
from pythainlp.tokenize import word_tokenize

def get_token_frequencies(
    docs: List[List[str]],
    min_freq: int = 2
) -> pd.DataFrame:
    """
    Count word frequencies from list of token lists.

    Args:
        docs: A list of tokenized documents (List of List of str)
        min_freq: Minimum frequency threshold to include in output

    Returns:
        DataFrame with word frequencies
    
    :example:
            >> df = pd.DataFrame(data=data)
            >> df["tokens"] = df["content"].apply(tokenize)
            >> print(get_token_frequencies(df["tokens"]))
    output:
                        freq
            token        11
            ของ          4
            เศรษฐกิจ      4
            ใน           3
            ปี            3
            และ          3
            ยังคง         3

    """

    counter = Counter()
    for tokens in docs:
        counter.update(tokens)

    freq_df = pd.DataFrame.from_dict(counter, orient='index', columns=['freq'])
    freq_df.index.name = 'token'
    return freq_df.query("freq > @min_freq").sort_values('freq', ascending=False)


def count_words_from_dataframe(
    df: pd.DataFrame,
    column: str = 'tokens',
    preprocess: Optional[Callable[[Union[str, List[str]]], List[str]]] = None,
    min_freq: int = 2
) -> pd.DataFrame:
    """
    Count word frequencies from a DataFrame column.

    Args:
        df: Input DataFrame
        column: Name of the column that contains raw text or tokens
        preprocess: Optional function to preprocess or tokenize each document
        min_freq: Minimum frequency threshold

    Returns:
        DataFrame with word frequencies

    :example: 
            >> df = pd.DataFrame(data=data)
            >> df["tokens"] = df["content"].apply(tokenize)
            >> freq_df = count_words_from_dataframe(df)
            >> print(freq_df)
    output:
                       freq
            token        11
            ของ          4
            เศรษฐกิจ      4
            ใน           3
            ปี            3
            และ          3
            ยังคง         3
    """
    try:
        docs = df[column].apply(lambda x: preprocess(x) if preprocess else x).tolist()
    except KeyError:
        raise KeyError(f"Column '{column}' not found in DataFrame. Please check that the column exists.")

    return get_token_frequencies(docs, min_freq=min_freq)


def summarize_token_frequencies(freq_df: pd.DataFrame, top_n: int = 10) -> dict:
    """
    Summarize a frequency DataFrame returned by get_token_frequencies or count_words_from_dataframe.

    Args:
        freq_df: A DataFrame with index as tokens and a column 'freq'
        top_n: Number of top frequent words to show

    Returns:
        A summary dictionary

    :example:
            >> freq_df = count_words_from_dataframe(df)
            >> summary = summarize_token_frequencies(freq_df)
            >> print(summary)
    output:
         {'total_tokens': 31, 'unique_tokens': 7, 'singleton_tokens': 0, 'average_frequency': 4.428571, 
         'median_frequency': 3.0, 'top_percentile_90': 6.8, 'top_percentile_99': 10.58}
    """
    if "freq" not in freq_df.columns:
        raise ValueError("DataFrame must contain a 'freq' column.")

    total_tokens = freq_df['freq'].sum()
    unique_tokens = len(freq_df)
    singletons = (freq_df['freq'] == 1).sum()
    avg_freq = round(freq_df['freq'].mean(), 6)
    median_freq = round(freq_df['freq'].median(), 6)
    top_percentile_90 = round(freq_df['freq'].quantile(0.90), 6)
    top_percentile_99 = round(freq_df['freq'].quantile(0.99), 6)
    

    return {
        "total_tokens": total_tokens,
        "unique_tokens": unique_tokens,
        "singleton_tokens": singletons,
        "average_frequency": avg_freq,
        "median_frequency": median_freq,
        "top_percentile_90": top_percentile_90,
        "top_percentile_99": top_percentile_99
    }

