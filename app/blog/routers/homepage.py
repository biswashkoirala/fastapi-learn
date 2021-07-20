from fastapi import APIRouter


router = APIRouter(
    tags=['Homepage']
)


@router.get('/')
def homepage():
    return 'Welcome. Please see docs page at /docs'
    return homepage()

# @app.get('/')
# def homepage():
#     return 'This is homepage. Please go to BASEURL/docs for more. dfgdsfg'