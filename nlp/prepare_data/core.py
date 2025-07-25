import re
from typing import Callable
from typing import List
from pythainlp.tokenize import word_tokenize
from pythainlp.util import normalize
from pythainlp.corpus.common import thai_stopwords
from collections import Counter
pipeline= [str.lower,
            normalize,
            lambda text: word_tokenize(text, keep_whitespace=False)
            ]

def prepare(text: str, 
            pipeline: list[Callable[[str | list[str]], list[str]]]
            ) -> list[str]:
    """
    
        Data preparation process
        Args:
            text (str): The input string
            pipeline (list): The input list of pipeline
        Return: 
            list[str] word tokenize
        :example:

                >> text = "สั่งของจาก Lazada เมื่อวันศุกร์ ได้รับของวันจันทร์ morning เลย เร็วมาก! 👏 ตัว product ดูดี คุณภาพ OK ตามราคาเลยค่ะ"
                >> data = prepare(text, None)
                >> print(data)

        output:

            ['สั่ง', 'lazada', 'ศุกร์', 'จันทร์', 'morning', '!', '👏', 'ตัว', 'product', 'ดูดี', 'คุณภาพ', 'ok', 'ราคา']

    """
    tokens = text
    if pipeline is None:
        pipeline = [
            str.lower,
            normalize,
            lambda text: word_tokenize(text, keep_whitespace=False),
        ]
    for transform in pipeline:
        tokens = transform(tokens)
    
    # ลบ stopwords หลังจากผ่าน pipeline ทั้งหมด
    filtered = [t for t in tokens if t not in thai_stopwords()]
    
    return filtered

