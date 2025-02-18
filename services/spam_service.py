from repository.db import check_for_spam, add_spam


def addSpam(userId, phone):
    add_spam(userId, phone)
    return {"message": "Spam reported!"}


def isPhoneSpam(phone):
    spam_count = check_for_spam(phone)
    if spam_count > 2:
        return {"message": "Phone number is spam!"}
    else:
        return {"message": "Phone number is not spam!"}
