import random
import os
import pandas as pd


random.seed(42)


SPAM_SUBJECTS = [
    "Urgent: Your account requires verification",
    "Congratulations! You have won a prize",
    "You have been selected for a reward",
    "Your payment has failed",
    "Important security alert",
    "Claim your exclusive reward now",
    "Your account will be suspended",
    "Limited time offer - act now",
    "You are our lucky winner",
    "Verify your account immediately",
    "Unusual login detected",
    "Final notice: account suspension",
    "Get your free gift today",
    "Exclusive cash reward waiting for you",
    "Your refund is waiting",
    "Immediate action required",
    "You've won $1,000,000",
    "Claim your lottery winnings",
    "Your subscription has expired",
    "Security verification required"
]


SPAM_OPENINGS = [
    "Dear Customer,",
    "Dear Valued Customer,",
    "Congratulations!",
    "Important Notice!",
    "Dear Account Holder,",
    "Attention User,",
    "Dear Winner,"
]


SPAM_BODIES = [
    "We detected unusual activity on your account.",
    "You have been selected to receive an exclusive reward.",
    "Our system shows that your account requires immediate verification.",
    "You are eligible for a special cash reward.",
    "Your account has been selected for a limited-time promotion.",
    "We were unable to process your recent payment.",
    "You must confirm your identity to avoid service interruption.",
    "You have won a special prize in our customer reward program.",
    "Your refund is ready and waiting to be claimed.",
    "We detected a suspicious login attempt."
]


SPAM_ACTIONS = [
    "Click the link below to verify your account.",
    "Confirm your information immediately.",
    "Claim your reward before the offer expires.",
    "Verify your account within 24 hours.",
    "Click here to prevent your account from being suspended.",
    "Complete the verification process now.",
    "Follow the link below to receive your payment.",
    "Confirm your details to release the reward.",
    "Log in immediately to secure your account."
]


SPAM_URGENCY = [
    "Failure to act within 24 hours may result in permanent suspension.",
    "This offer expires today.",
    "You must respond immediately.",
    "Your account may be closed if you do not verify it.",
    "This is your final notification.",
    "The offer is available for a limited time only.",
    "Act now before it is too late."
]


SPAM_URLS = [
    "http://secure-account.example.com/verify",
    "http://claim-reward.example.com/login",
    "http://account-security.example.com/update",
    "http://payment-confirm.example.com/verify",
    "http://winner-claim.example.com/reward"
]


HAM_SUBJECTS = [
    "Project meeting tomorrow",
    "Meeting notes",
    "Weekly team update",
    "Lunch tomorrow?",
    "Assignment submission reminder",
    "Project progress update",
    "Schedule for next week",
    "Can we reschedule the meeting?",
    "Documents for review",
    "Team meeting at 10 AM",
    "College project discussion",
    "Updated presentation",
    "Monthly report",
    "Follow-up regarding our discussion",
    "Conference schedule",
    "Invoice for last month",
    "Vacation plans",
    "Class timetable",
    "Event details",
    "Thank you for your help"
]


HAM_OPENINGS = [
    "Hi,",
    "Hello,",
    "Hi Team,",
    "Hi John,",
    "Hello everyone,",
    "Good morning,",
    "Dear Team,",
    "Hi Rahul,"
]


HAM_BODIES = [
    "I wanted to share a quick update regarding the project.",
    "Just confirming that our meeting is scheduled for tomorrow.",
    "Please find the updated document attached for your review.",
    "I have completed the changes we discussed yesterday.",
    "Could you please review the presentation when you have time?",
    "The team has completed the assigned tasks for this week.",
    "I wanted to check whether you are available for a meeting.",
    "Here are the notes from today's discussion.",
    "The deadline has been moved to next Friday.",
    "I will send the remaining documents later today.",
    "Thanks for your feedback on the project.",
    "Please let me know if anything needs to be changed."
]


HAM_CLOSINGS = [
    "Thanks,",
    "Best regards,",
    "Regards,",
    "Thank you,",
    "Best,",
    "See you tomorrow,",
    "Have a great day,"
]


NAMES = [
    "Rahul",
    "John",
    "Sarah",
    "Michael",
    "Priya",
    "David",
    "Alex",
    "Daniel",
    "Emily",
    "Sam"
]


def generate_spam():

    subject = random.choice(SPAM_SUBJECTS)

    opening = random.choice(SPAM_OPENINGS)

    body = random.choice(SPAM_BODIES)

    action = random.choice(SPAM_ACTIONS)

    urgency = random.choice(SPAM_URGENCY)

    url = random.choice(SPAM_URLS)

    variation = random.choice([
        "CLICK NOW!",
        "ACT NOW!",
        "URGENT!",
        "FINAL NOTICE!",
        "IMPORTANT!",
        "",
        ""
    ])

    email = f"""
Subject: {subject} {variation}

{opening}

{body}

{action}

{urgency}

{url}

Please do not ignore this message.

Regards,
Customer Security Department
"""

    return email.strip()


def generate_ham():

    subject = random.choice(HAM_SUBJECTS)

    opening = random.choice(HAM_OPENINGS)

    body = random.choice(HAM_BODIES)

    closing = random.choice(HAM_CLOSINGS)

    name = random.choice(NAMES)

    email = f"""
Subject: {subject}

{opening}

{body}

{closing}
{name}
"""

    return email.strip()


def main():

    spam_count = 6000
    ham_count = 6000

    data = []

    for _ in range(spam_count):

        data.append({
            "email": generate_spam(),
            "label": "spam"
        })


    for _ in range(ham_count):

        data.append({
            "email": generate_ham(),
            "label": "ham"
        })


    random.shuffle(data)

    df = pd.DataFrame(data)

    os.makedirs(
        "dataset",
        exist_ok=True
    )

    output = "dataset/spam_emails.csv"

    df.to_csv(
        output,
        index=False
    )

    print("\n================================")
    print("DATASET CREATED")
    print("================================")

    print(f"Total emails: {len(df)}")

    print("\nClass distribution:")

    print(df["label"].value_counts())

    print(f"\nSaved to: {output}")


if __name__ == "__main__":
    main()