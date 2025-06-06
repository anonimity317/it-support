from website import create_app, db
from website.models import User

# change username-'XXXXX' to elevate that user to admin
app = create_app()
with app.app_context():
    user = User.query.filter_by(username='admin').first()
    if user:
        user.pu = True
        db.session.commit()
        print("User 'admin' updated: pu=True")
    else:
        print("User 'admin' not found.")
