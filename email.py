import random
import json

def fetchemail():
    with open("emails.json", "r") as f:
        emails = json.load(f)
    return random.choice(emails)


def reader(email):

    if "update" in email:
        return "update"
    return " update"


def responder(email, summary):
    with open("responses.json", "r") as f:
        responses = json.load(f)
    if delayed in summary:
        return responses["delayed"]
    elif "going well" in summary:
        return responses["going well"]
    elif "on track" in summary:
        return responses["on track"]
    return responses["default"]


def reviewer(draft):
    return draft


def sendemail(toaddr, subject, body):
    print("sending email")
    print(toaddr)
    print(subject)
    print(body)


def runworkflow():

    rawemail = fetchemail()
    print(rawemail)

    summary = reader(rawemail)
    print(summary)

    draft = responder(rawemail, summary)
    print(draft)

    reviewed = reviewer(draft)
    print(reviewed)

    choice = input("send? y/n: ")

    if choice == "y":
        sendemail("sukhmani@gmail.com", "re: update", reviewed)
        print("done")
    else:
        print("not sent")


if __name__ == "__main__":
    runworkflow()