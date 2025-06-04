from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import ActiveTicket

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    if current_user.pu:
        tickets = ActiveTicket.query.all()
    else:
        tickets = current_user.tickets
    return render_template('index.html', user=current_user, tickets=tickets)

@routes.route('/add_ticket', methods=['GET', 'POST'])
@login_required
def add_ticket():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        priority = request.form.get('priority')

        if not title or not content:
            flash('Title and content are required.', category='error')
        else:
            new_ticket = ActiveTicket(user_id=current_user.id, title=title, content=content, priority=priority)
            db.session.add(new_ticket)
            db.session.commit()
            flash('Ticket added successfully!', category='success')
            return redirect(url_for('routes.home'))
    return render_template('add_ticket.html', user=current_user)

@routes.route('/update_ticket/<int:ticket_id>', methods=['GET', 'POST'])
@login_required
def update_ticket(ticket_id):
    ticket = ActiveTicket.query.get_or_404(ticket_id)
    if request.method == 'POST':
        # Soft delete if admin clicked "Close Ticket"
        if current_user.pu and request.form.get('close_ticket'):
            ticket.status = 'Closed'
            db.session.commit()
            flash('Ticket closed successfully!', category='success')
            return redirect(url_for('routes.home'))

        ticket.title = request.form.get('title')
        ticket.content = request.form.get('content')
        ticket.priority = request.form.get('priority')

        if not ticket.title or not ticket.content:
            flash('Title and content are required.', category='error')
        else:
            db.session.commit()
            flash('Ticket updated successfully!', category='success')
            return redirect(url_for('routes.home'))
    return render_template('update_ticket.html', user=current_user, ticket=ticket)