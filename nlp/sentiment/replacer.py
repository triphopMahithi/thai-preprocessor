import re 

class SentimentReplacer:
    """

    Replaces emojis in a text with sentiment tags based on a predefined emoji-to-sentiment mapping.

    Attributes:
        emoji_to_tag (dict): A dictionary mapping each emoji character to its corresponding sentiment tag.
                             For example, '😊' -> '<<EMO_POS>>'.

    Example:
        >>> emoji_sentiment = {
                "POS": ["😊", "😁", "🎉"],
                "NEG": ["😢", "😠", "😡"],
                "NEU": ["😐"]
            }
        >>> replacer = EmojiSentimentReplacer(emoji_sentiment)
        >>> text = "I feel happy 😊 but also a bit sad 😢."
        >>> print(replacer.tag_emoji_sentiment(text))
        I feel happy <<EMO_POS>> but also a bit sad <<EMO_NEG>>.

    """
    def __init__(self, emoji_sentiment : dict):
        self.emoji_to_tag = {
            emo : f'<<EMO_{sentiment}>>'
            for sentiment, emojis in emoji_sentiment.items()
            for emo in emojis
        }
    
    def tag_emoji_sentiment(self, sentence: str) -> str:
        """
        Replace emojis in the input sentence with their corresponding sentiment tags.

        Args:
            sentence (str): The input string potentially containing emojis to be replaced.

        Returns:
            str: The processed string where all emojis found in the mapping
                 are replaced by their corresponding sentiment tags.

        Example:
            >>> text = "I am happy 😊 but sometimes sad 😢."
            >>> replacer.tag_emoji_sentiment(text)
            'I am happy <<EMO_POS>> but sometimes sad <<EMO_NEG>>.'
        """
        for emo, tag in self.emoji_to_tag.items():
            sentence = sentence.replace(emo, tag)
        return sentence

def tag_hashtag(sentence : str) -> str:
    """
    Replace hashtag in the input sentence 

    Args: 
        sentence (str): The input string 
    
    Return: 
        str : The processed string where all hashtag found in the mapping 
                are replaced 
    Example: 
        >>> sentence = ""วันนี้อากาศดีมาก #สดชื่น#สดชื่นสุดๆ #สุดยอด #อากาศไทย""
        >>> tagged = tag_hashtag(sentence)
            'วันนี้อากาศดีมาก <TAG_สดชื่น_><TAG_สดชื่นสุดๆ_> <TAG_สุดยอด_> <TAG_อากาศไทย_>'
    """
    def tag_hashtag_sentiment(match : str) -> str:
        hashtag = match.group(1)
        return f'<TAG_{hashtag}_\1>'
    return re.sub(r"#([ก-๙a-zA-Z0-9_]+)", tag_hashtag_sentiment, sentence)
emoji_sentiment = {
                "POS": ["😊", "😁", "🎉"],
                "NEG": ["😢", "😠", "😡"],
                "NEU": ["😐"]
            }

text= """
วันนี้ตื่นเช้ามาพร้อมกับแดดอ่อนๆ ☀️ อากาศสดชื่นมาก #สดชื่น #วันหยุด  
แวะไปคาเฟ่เปิดใหม่ ☕️ ร้านตกแต่งน่ารักมาก #คาเฟ่สวย #บรรยากาศดี  
พนักงานบริการดีสุดๆ ยิ้มแย้มและใส่ใจ 😊 ประทับใจเลย #บริการดี  
แต่เจอรถติดนิดหน่อยตอนขากลับ 😤 เหนื่อยนิดนึง  
รวมๆ แล้วถือว่าเป็นวันหยุดที่ดีมาก 💖 #ชีวิตดีๆที่ลงตัว
"""

