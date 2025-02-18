from fastapi import FastAPI

from routers import ai_router

app = FastAPI()
app.include_router(ai_router.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app!"}


# block_number_by_id(id: str, phoneNumber: str) -> str:
# """
# Blocks numbers to call or message to the user.
#
# Args:
#     id: this is the user id who wants to block given phone number.
#     phoneNumber: Given phone number to block by id.
#
# Returns:
#     A string message to describe the result of the action.
# """