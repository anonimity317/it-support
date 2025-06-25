import sys
import os
from website import create_app, db
from website.models import User, ActiveTicket
from werkzeug.security import generate_password_hash

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = create_app()
with app.app_context():
    # Drop and recreate all tables (restart the database)
    db.drop_all()
    db.create_all()

    # Create and commit admin user first
    admin = User(
        username='admin',
        first_name='admin',
        password=generate_password_hash('admin', method='pbkdf2:sha1', salt_length=8),
        pu=True
    )
    db.session.add(admin)
    db.session.commit()  # Commit admin so it's available for login

    # Example ticket messages
    ticket_messages = [
        "My computer won't start after the latest update.",
        "Unable to connect to the office Wi-Fi network.",
        "Forgot my email password and can't reset it.",
        "Printer on the 2nd floor is jammed and showing an error.",
        "Need access to the shared drive for the marketing team.",
        "Laptop battery drains too quickly, even when idle.",
        "Getting a blue screen error when launching Excel.",
        "Monitor flickers and sometimes goes black.",
        "Requesting installation of Adobe Photoshop for design work.",
        "VPN connection drops frequently when working remotely."
    ]

    # Create 9 regular users and a ticket for each
    for i in range(1, 10):
        username = f'user{i}'
        user = User(
            username=username,
            first_name=f'User{i}',
            password=generate_password_hash('password', method='pbkdf2:sha1', salt_length=8),
            pu=False
        )
        db.session.add(user)
        db.session.flush()  # Ensure user.user_id is available

        ticket = ActiveTicket(
            user_id=user.user_id,
            title=f"Ticket for {username}",
            content=ticket_messages[i-1],
            priority='Normal',
            status='Open'
        )
        db.session.add(ticket)

    db.session.commit()
    print("Database reset. Admin and 10 users with unique tickets created.")
