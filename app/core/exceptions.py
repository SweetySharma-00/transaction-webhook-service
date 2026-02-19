from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    custom_errors = []

    for error in exc.errors():
        field = error["loc"][-1]
        error_type = error["type"]

        if error_type == "missing":
            message = f"{field} is required"
        else:
            message = error["msg"]

        custom_errors.append({
            "field": field,
            "message": message
        })

    return JSONResponse(
        status_code=422,
        content={"errors": custom_errors},
    )
