from repository.db import get_user_by_phone, get_user_by_id, get_status, get_trust_score, block_number


def getPhoneNumberInfo(phoneNumber):
    user = get_user_by_phone(phoneNumber)
    if user is not None:
        return {"name": user["name"] + user["surname"], "email": user["email"], "phone": phoneNumber}
    return {"message": "User not found!"}


def getIdInfo(userId):
    user = get_user_by_id(userId)
    if user is not None:
        return {"name": user["name"] + user["surname"], "email": user["email"], "phone": user["phone"]}
    return {"message": "User not found!"}


def getStatus(userId):
    return {"status": get_status(userId)}


def getTrustScore(userId):
    return {"trust_score": get_trust_score(userId)}


def blockNumber(userId, phoneNumber):
    user = get_user_by_id(userId)

    if phoneNumber in user["blocked_numbers"]:
        return {"message": "Number already blocked!"}

    block_number(userId, phoneNumber)
    return {"message": "Number blocked!"}
