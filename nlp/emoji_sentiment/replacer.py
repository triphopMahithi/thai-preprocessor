class EmojiSentimentReplacer:
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
    
    def tag_emoji_sentiment(self, sentence : str) -> str:
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
