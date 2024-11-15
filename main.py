from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "kkprofile_db"

mysql = MySQL(app)

# Home Route
@app.route('/')
def home():
    return render_template('home.html')  # Display the home page with Register button

# Register Form Route
@app.route('/register')
def register_form():
    return render_template('register.html')  # Display the registration form

# Register Post Route (Handle form submission)
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        address = request.form.get('address')
        age = request.form.get('age')
        birthday = request.form.get('birthday')
        gender = request.form.get('gender')
        contact = request.form.get('contact')
        email = request.form.get('email')
        civil_status = request.form.get('civil_status')
        youth_age_group = request.form.get('youth_age_group')
        youth_classification = request.form.get('youth_classification')
        education_background = request.form.get('education_background')
        work_status = request.form.get('work_status')
        registered_sk_voter = request.form.get('registered_sk_voter')
        registered_national_voter = request.form.get('registered_national_voter')
        vote_last_sk = request.form.get('vote_last_sk')
        kk_assembly = request.form.get('kk_assembly')
        kk_assembly_attendance = request.form.get('kk_assembly_attendance')
        no_kk_reason = request.form.get('no_kk_reason')

        # Database insertion
        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO kk_profiles (
                name, address, age, birthday, gender, contact, email,
                civil_status, youth_age_group, youth_classification, education_background,
                work_status, registered_sk_voter, registered_national_voter, vote_last_sk,
                kk_assembly, kk_assembly_attendance, no_kk_reason
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            name, address, age, birthday, gender, contact, email,
            civil_status, youth_age_group, youth_classification, education_background,
            work_status, registered_sk_voter, registered_national_voter, vote_last_sk,
            kk_assembly, kk_assembly_attendance, no_kk_reason
        ))
        mysql.connection.commit()
        cursor.close()
        
        flash(f"Registration successful for {name}!", "success")
        return redirect(url_for('home'))  # Redirect to home page after successful registration

    return redirect(url_for('register_form'))  # In case of invalid request, reload the register form

if __name__ == '__main__':
    app.run(debug=True)


