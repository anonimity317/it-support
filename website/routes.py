from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import ActiveTicket

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    return render_template('index.html', user=current_user) 

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