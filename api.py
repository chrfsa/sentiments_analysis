from transformers import pipeline
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() 

# Load the pipeline for sentiment analysis
nlp_sentiment = pipeline("sentiment-analysis")



class Item(BaseModel):
    prompts: str

@app.post("/analyse")
async def analyse_sentiments(item: Item):
    """api for sentiment analysis

    Args:
        item (Item): string like prompts and feeling

    Returns:
        json: felling and probability of the felling negative or positive.
    """
    return nlp_sentiment(item.prompts)
