import unittest
from website import create_app


class FlaskRoutesTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def login(self, username, password):
        return self.client.post('/login', data={
            'username': username,
            'password': password
        }, follow_redirects=True)

    def test_home_page_requires_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_login_success_user(self):
        response = self.login('user1', 'password')
        self.assertIn(b'Active Tickets', response.data)
        self.assertEqual(response.status_code, 200)

    def test_login_success_admin(self):
        response = self.login('admin', 'admin')
        self.assertIn(b'Active Tickets', response.data)
        self.assertEqual(response.status_code, 200)

    def test_login_failure(self):
        response = self.login('user1', 'wrongpassword')
        self.assertIn(b'Incorrect password', response.data)
        self.assertEqual(response.status_code, 401)

    def test_404_page(self):
        response = self.client.get('/nonexistent-page')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Page Not Found', response.data)

    def test_add_ticket_page(self):
        with self.client:
            self.client.post('/login', data={'username': 'user1', 'password': 'password'})
            response = self.client.get('/add_ticket')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Add New Ticket', response.data)

    def test_update_ticket_page(self):
        with self.client:
            self.client.post('/login', data={'username': 'user1', 'password': 'password'})
            response = self.client.get('/update_ticket/1')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Update Ticket', response.data)

    def test_update_ticket_not_found(self):
        with self.client:
            self.client.post('/login', data={'username': 'user1', 'password': 'password'})
            response = self.client.get('/update_ticket/9999')
            self.assertEqual(response.status_code, 404)

    def test_add_ticket_without_login(self):
        response = self.client.get('/add_ticket')
        self.assertEqual(response.status_code, 302)

    def delete_ticket_without_login(self):
        response = self.client.get('/delete_ticket/1')
        self.assertEqual(response.status_code, 302)

    def test_update_ticket_without_login(self):
        response = self.client.get('/update_ticket/1')
        self.assertEqual(response.status_code, 302)

    def test_add_ticket_with_invalid_data(self):
        with self.client:
            self.client.post('/login', data={'username': 'user1', 'password': 'password'})
            response = self.client.post('/add_ticket', data={'title': '', 'content': '', 'priority': 'Normal'})
            self.assertEqual(response.status_code, 200)

    def test_update_ticket_with_invalid_data(self):
        with self.client:
            self.client.post('/login', data={'username': 'user1', 'password': 'password'})
            response = self.client.post('/update_ticket/1', data={'title': '', 'content': '', 'priority': 'Normal'})
            self.assertEqual(response.status_code, 200)

    def test_signup_invalid_data(self):
        response = self.client.post('/sign-up', data={
            'username': 'test',
            'first_name': 'Test',
            'password1': 'test',
            'password2': 'test'
        })
        self.assertEqual(response.status_code, 400)
