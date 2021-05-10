# import sys
# sys.path.append('../')
# Importing Necessary modules
# from fastapi import FastAPI
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import uvicorn
from predict import predict_tone
from pydantic import BaseModel

# Declaring our FastAPI instance
app = FastAPI()
templates = Jinja2Templates(directory="templates/")


class request_body(BaseModel):
    input_sentence: str

# Defining path operation for root endpoint
# @app.get('/')
# def main():
#     return {'message': 'Welcome to GeeksforGeeks!'}

# Defining path operation for /name endpoint

# @app.post('/predict')
# def predict(data : request_body):
#     # Making the data in a form suitable for prediction
#     test_data = data.input_sentence
#     # print(test_data)
#     # test_data = str(test_data)
#     # Predicting the Class
#     output = accent_sentence(test_data)

#     # Return the Result
#     return {'prediction': output}


@app.get("/")
def form_post(request: Request):
    # result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request})


@app.post("/")
def form_post(request: Request, data: str = Form(None)):
    if not data:
        return templates.TemplateResponse('form.html', context={'request': request, 'result': "", 'olddata': ""})
    else:
        result = predict_tone(data)
        return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'olddata': data})

# @app.post("/form")
# def form_post(request: Request, num: int = Form(...)):
#     result = gennum()
#     return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


# @app.get('/{name}')
# def hello_name(name : str):
#     # Defining a function that takes only string as input and output the
#     # following message.
#     return {'message': f'Welcome to GeeksforGeeks!, {name}'}


# text = "Tuy nhien, tren thuc te, moi nguoi deu hieu rang, viec cuoc cai to noi cac lan nay cua ba May la mot canh bac nham xac dinh va ap dat quyen luc lanh dao cua ba doi voi nhung thanh vien noi cac, trong do co nhung nguoi da the hien bat dong chinh kien voi ba trong van de Brexit va mot so van de khac ve chinh tri, kinh te, xa hoi."
# accent_text = accent_sentence(text)
# print(accent_text)
