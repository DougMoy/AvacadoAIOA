from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Article(BaseModel):
    text: str

@app.post("/process-text/")
async def process_text(article: Article):
    processed_text = article.text.upper()
    return {"processedText": processed_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

#TEST WITH 
#Invoke-RestMethod -Uri "http://localhost:8000/process-text/" -Method Post -ContentType "application/json" -Body '{"text": "This is an example article text."}'
