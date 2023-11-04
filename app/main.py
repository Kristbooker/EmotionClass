import os
import pickle
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from app.predict import predict_emote


# model_path = '/Users/krist/EmotionalClass/model/TextModel.pkl'
# model_path = os.getenv('/Users/krist/EmotionalClass/model/TextModel.pkl')

# m = pickle.load(open(model_path,'rb'))
m = pickle.load(open(os.getcwd()+r'/model/TextModel.pkl', 'rb'))

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)


@app.get("/")
def root():
    return {"message": "This is my api"}

@app.post("/api/textemote")
async def read_str(data : Request):
    json=await data.json()
    text_string=json["text"]
    emote = predict_emote(m,text_string)
    return {"Emotion":emote}