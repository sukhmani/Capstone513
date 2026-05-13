def fetch_latest_email():
    return "Hi"


def reader(email):
    return " update"


def responder(email, summary):
    return "projectn"


def reviewer(draft):
    return draft


def send_email(toaddr, subject, body):
    print("sending email")
    print(toaddr)
    print(subject)
    print(body)


def run_workflow():

    rawemail = fetch_latest_email()
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
    run_workflow()