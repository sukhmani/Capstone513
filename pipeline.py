import asyncio


async def run_pipeline():

    print("Pipeline started")

    emails = [
        {
            "sender": "patient@example.com",
            "subject": "Missed medication dose",
            "body": (
                "Hello,\n\n"
                "I forgot to take my Keppra this morning. "
                "Should I take it late or wait until tonight?\n\n"
                "Thank you."
            )
        }
    ]

    for email_data in emails:

        print("\n--- EMAIL ---")

        print(email_data["sender"])

        print(email_data["subject"])

        print(email_data["body"])

    # get emails

    # summarize email

    # retrieve context

    # generate draft

    # review response

    # approve

    # send email


if __name__ == "__main__":

    asyncio.run(run_pipeline())