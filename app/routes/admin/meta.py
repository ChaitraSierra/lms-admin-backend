from fastapi import APIRouter


router=APIRouter(
    prefix="/admin/meta",
    tags=["Fetching MetaData"]
)


@router.get("/languages")
def fetch_languages():
    return ["C","JAVA","PYTHON","MySql"]


