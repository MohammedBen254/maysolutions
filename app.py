from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
mail = Mail(app)

# Sample project data
projects = [
    {
        'id': 1,
        'title': 'Portfolio Website',
        'description': 'Custom portfolio websites for professionals and businesses to showcase their work.'
    },
    {
        'id': 2,
        'title': 'Data Analysis Tool',
        'description': 'Advanced tools for processing and visualizing complex datasets.'
    },
    {
        'id': 3,
        'title': 'AI Model Development',
        'description': 'Custom AI solutions tailored to specific business needs.'
    },
    {
        'id': 4,
        'title': 'Chatbot Systems',
        'description': 'Intelligent chatbots for customer service and engagement.'
    },
    {
        'id': 5,
        'title': 'Reservation Websites',
        'description': 'Online booking systems for various industries.'
    },
    {
        'id': 6,
        'title': 'Stock Management System',
        'description': 'Inventory tracking and management solutions.'
    },
    {
        'id': 7,
        'title': 'Document Management System',
        'description': 'Secure systems for organizing and accessing documents.'
    },
    {
        'id': 8,
        'title': 'Invoicing System',
        'description': 'Automated billing and payment solutions.'
    },
    {
        'id': 9,
        'title': 'Navigation Agent AI',
        'description': 'AI-powered guidance systems for websites and applications.'
    },
    {
        'id': 10,
        'title': 'Social Media Analysis Platform',
        'description': 'Tools for tracking and analyzing social media performance.'
    },
    {
        'id': 11,
        'title': 'Appointment Booking Website',
        'description': 'Scheduling systems with integrated voting features.'
    },
    {
        'id': 12,
        'title': 'Analytics Website',
        'description': 'Comprehensive data analytics dashboards.'
    }
]

# Sample solutions data
solutions = [
    {
        'title': 'AI Integration',
        'description': 'Seamlessly incorporate artificial intelligence into your existing systems to enhance capabilities and efficiency.'
    },
    {
        'title': 'Data Analysis',
        'description': 'Transform raw data into actionable insights with our advanced analytics solutions.'
    },
    {
        'title': 'Web Development',
        'description': 'Custom, scalable web applications designed to meet your specific business needs.'
    },
    {
        'title': 'Process Automation',
        'description': 'Eliminate manual tasks and reduce errors with our intelligent automation solutions.'
    },
    {
        'title': 'Predictive Analytics',
        'description': 'Anticipate trends and make data-driven decisions with our forecasting models.'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solutions')
def solutions_page():
    return render_template('solutions.html', solutions=solutions)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# send email
@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    with open('messages_recived.txt', 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Message: {message}\n")
        file.write("\n\n")
        file.write("========================================\n")
        file.write("========================================\n")
        file.write("\n\n")
        file.close()
    # Here you would typically send the email using an email service
    flash('Your message has been sent successfully!', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)