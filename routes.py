from flask import Flask, render_template, request, redirect, url_for
from models import db, Ticket

app = Flask(__name__)

@app.route('/tickets', methods=['GET'])
def view_tickets():
    tickets = Ticket.query.all()
    return render_template("tickets.html", tickets=tickets)

@app.route('/ticket/new', methods=['POST'])
def create_ticket():
    title = request.form.get("title")
    description = request.form.get("description")
    
    new_ticket = Ticket(title=title, description=description)
    db.session.add(new_ticket)
    db.session.commit()

    return redirect(url_for("view_tickets"))

@app.route('/ticket/update/<int:id>', methods=['POST'])
def update_ticket(id):
    ticket = Ticket.query.get(id)
    ticket.status = request.form.get("status")
    db.session.commit()

    return redirect(url_for("view_tickets"))
