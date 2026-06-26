# def main():
#     print("Hello from fastapi-blog!")


# if __name__ == "__main__":
#     main()
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

posts:list[dict] =[
    {
        "id":1,
        "author": "David",
        "title": "fast api is awesome",
        "content": "great framework",
        "date_posted": "June 26, 2026"
    },
    {
        "id":1,
        "author": "Laura",
        "title": "Asyn is is awesome",
        "content": "great approach",
        "date_posted": "June 27, 2026"
    }
]

@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request,"home.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts