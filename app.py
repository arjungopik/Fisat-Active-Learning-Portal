from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:user@localhost:5432/active'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    academic_year = db.Column(db.String)
    date = db.Column(db.Date)
    class_name = db.Column(db.String)
    faculty_id =  db.Column(db.String)
    faculty_in_charge = db.Column(db.String)
    course_code = db.Column(db.String)
    course_name = db.Column(db.String)
    topic = db.Column(db.String)

class MinuteFormData(db.Model):
    __tablename__ = 'minute_form_data'
    id = db.Column(db.Integer, primary_key=True)
    academic_year = db.Column(db.String)
    date = db.Column(db.Date)
    class_name = db.Column(db.String)
    faculty_in_charge = db.Column(db.String)
    course_code = db.Column(db.String)
    course_name = db.Column(db.String)
    topic = db.Column(db.String)
    learning_outcome = db.Column(db.String)
    addressed_course_outcomes = db.Column(db.String)
    no_of_students_engaged = db.Column(db.String)
    assessment_questions = db.Column(db.String)
    alloted_time = db.Column(db.Integer)
    students_supposed_to = db.Column(db.String)
    expected_proficiency = db.Column(db.String)
    total_assessment_marks = db.Column(db.String)
    assessment_analysis = db.Column(db.String)
    concepts_expansion = db.Column(db.String)
    percentage_students_expansion = db.Column(db.String)
    follow_up_actions = db.Column(db.String)


class TPSFormData(db.Model):
    __tablename__ = 'tps_form_data'
    id = db.Column(db.Integer, primary_key=True)
    academic_year = db.Column(db.String)
    date = db.Column(db.Date)
    class_name = db.Column(db.String)
    faculty_in_charge = db.Column(db.String)
    course_code = db.Column(db.String)
    course_name = db.Column(db.String)
    topic = db.Column(db.String)
    learning_outcome = db.Column(db.String)
    addressed_course_outcomes = db.Column(db.String)
    knowledge_level_assessment = db.Column(db.String)
    questions = db.Column(db.String)
    think_phase = db.Column(db.String)
    pair_phase = db.Column(db.String)
    share_phase = db.Column(db.String)
    alloted_time = db.Column(db.String)
    students_engaged = db.Column(db.String)
    conclusion = db.Column(db.String)
    expected_proficiency = db.Column(db.String)
    total_assessment_marks = db.Column(db.String)
    assessment_analysis = db.Column(db.String)
    concepts_expansion = db.Column(db.String)
    percentage_students_expansion = db.Column(db.String)
    follow_up_actions = db.Column(db.String)

class FlippedFormData(db.Model):
    __tablename__ = 'flipped_form_data'
    id = db.Column(db.Integer, primary_key=True)
    academic_year = db.Column(db.String)
    date = db.Column(db.Date)
    class_name = db.Column(db.String)
    faculty_in_charge = db.Column(db.String)
    course_code = db.Column(db.String)
    course_name = db.Column(db.String)
    topic = db.Column(db.String)
    learning_outcome = db.Column(db.String)
    addressed_course_outcomes = db.Column(db.String)
    video_url = db.Column(db.String)
    outside_activity = db.Column(db.String)
    outside_assessment_strategy = db.Column(db.String)
    inside_activity = db.Column(db.String)
    inside_assessment_activity = db.Column(db.String)
    knowledge_level = db.Column(db.String)
    students_engaged = db.Column(db.String)
    expected_proficiency = db.Column(db.String)
    total_assessment_marks = db.Column(db.String)
    assessment_analysis = db.Column(db.String)
    follow_up_actions = db.Column(db.String)


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        id = request.form.get('gid')
        psw = request.form.get('password')
        if id== psw:
            tps_data = TPSFormData.query.all()
            return render_template('hodpage.html', tps_data=tps_data)
    else:
        return render_template('login.html')


@app.route('/minute', methods=['GET', 'POST'])
def minute():
    if request.method == 'POST':
        academic_year = request.form.get('academic_year')
        date = request.form.get('date')
        class_name = request.form.get('cls')
        faculty_in_charge = request.form.get('faculty_in_charge')
        course_code = request.form.get('course_code')
        course_name = request.form.get('course_name')
        topic = request.form.get('topic')
        learning_outcome = request.form.get('learning_outcome')
        addressed_course_outcomes = request.form.get('addressed_course_outcomes')
        no_of_students_engaged = request.form.get('no_of_students_engaged')
        assessment_questions = request.form.get('assessment_questions')
        alloted_time = request.form.get('alloted_time')
        students_supposed_to = request.form.get('students_supposed_to')
        expected_proficiency = request.form.get('expected_proficiency')
        total_assessment_marks = request.form.get('total_assessment_marks')
        assessment_analysis = request.form.get('assessment_analysis')
        concepts_expansion = request.form.get('concepts_expansion')
        percentage_students_expansion = request.form.get('percentage_students_expansion')
        follow_up_actions = request.form.get('follow_up_actions')

        minute_form_data = MinuteFormData(academic_year=academic_year, date=date, class_name=class_name,
                                          faculty_in_charge=faculty_in_charge, course_code=course_code,
                                          course_name=course_name, topic=topic, learning_outcome=learning_outcome,
                                          addressed_course_outcomes=addressed_course_outcomes,
                                          no_of_students_engaged=no_of_students_engaged,
                                          assessment_questions=assessment_questions, alloted_time=alloted_time,
                                          students_supposed_to=students_supposed_to,
                                          expected_proficiency=expected_proficiency,
                                          total_assessment_marks=total_assessment_marks,
                                          assessment_analysis=assessment_analysis,
                                          concepts_expansion=concepts_expansion,
                                          percentage_students_expansion=percentage_students_expansion,
                                          follow_up_actions=follow_up_actions)

        db.session.add(minute_form_data)
        db.session.commit()
        return "Form submitted successfully"
    else:
      return render_template('minute.html')


@app.route('/tps', methods=['GET', 'POST'])
def tps():
    if request.method == 'POST':
        academic_year = request.form.get('academic_year')
        date = request.form.get('date')
        class_name = request.form.get('cls')
        faculty_in_charge = request.form.get('faculty_in_charge')
        course_code = request.form.get('course_code')
        course_name = request.form.get('course_name')
        topic = request.form.get('topic')
        learning_outcome = request.form.get('learning_outcome')
        addressed_course_outcomes = request.form.get('addressed_course_outcomes')
        knowledge_level_assessment = request.form.get('knowledge_level_assessment_activity')
        questions = [request.form.get('question1'), request.form.get('question2'), request.form.get('question3')]
        think_phase = request.form.get('think_phase')
        pair_phase = request.form.get('pair_phase')
        share_phase = request.form.get('share_phase')
        alloted_time = request.form.get('alloted_time')
        students_engaged = request.form.get('students_engaged')
        conclusion = request.form.get('conclusion')
        expected_proficiency = request.form.get('expected_proficiency')
        total_assessment_marks = request.form.get('total_assessment_marks')
        assessment_analysis = request.form.get('assessment_analysis')
        concepts_expansion = request.form.get('concepts_expansion')
        percentage_students_expansion = request.form.get('percentage_students_expansion')
        follow_up_actions = request.form.get('follow_up_actions')

        tps_form_data = TPSFormData(academic_year=academic_year, date=date, class_name=class_name,
                                    faculty_in_charge=faculty_in_charge, course_code=course_code,
                                    course_name=course_name, topic=topic, learning_outcome=learning_outcome,
                                    addressed_course_outcomes=addressed_course_outcomes,
                                    knowledge_level_assessment=knowledge_level_assessment,
                                    questions=questions, think_phase=think_phase, pair_phase=pair_phase,
                                    share_phase=share_phase, alloted_time=alloted_time,
                                    students_engaged=students_engaged, conclusion=conclusion,
                                    expected_proficiency=expected_proficiency,
                                    total_assessment_marks=total_assessment_marks,
                                    assessment_analysis=assessment_analysis,
                                    concepts_expansion=concepts_expansion,
                                    percentage_students_expansion=percentage_students_expansion,
                                    follow_up_actions=follow_up_actions)

        db.session.add(tps_form_data)
        db.session.commit()
        inserted_id = tps_form_data.id
        return f"Form data inserted with id: {inserted_id}"
        
    else:
    
        return render_template('tps.html')
    
@app.route('/flip', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        academic_year = request.form.get('academic_year')
        date = request.form.get('date')
        class_name = request.form.get('cls')
        faculty_in_charge = request.form.get('faculty_in_charge')
        course_code = request.form.get('course_code')
        course_name = request.form.get('course_name')
        topic = request.form.get('topic')
        learning_outcome = request.form.get('learning_outcome')
        addressed_course_outcomes = request.form.get('addressed_course_outcomes')
        video_url = request.form.get('video_url')
        outside_activity = request.form.get('outside_activity')
        outside_assessment_strategy = request.form.get('outside_assessment_strategy')
        inside_activity = request.form.get('inside_activity')
        inside_assessment_activity = request.form.get('inside_assessment_activity')
        knowledge_level = request.form.get('knowledge_level')
        students_engaged = request.form.get('students_engaged')
        expected_proficiency = request.form.get('expected_proficiency')
        total_assessment_marks = request.form.get('total_assessment_marks')
        assessment_analysis = request.form.get('assessment_analysis')
        follow_up_actions = request.form.get('follow_up_actions')


        flipped_form_data = FlippedFormData(academic_year=academic_year, date=date, class_name=class_name,
                                    faculty_in_charge=faculty_in_charge, course_code=course_code,
                                    course_name=course_name, topic=topic, learning_outcome=learning_outcome,
                                    addressed_course_outcomes=addressed_course_outcomes, video_url=video_url,
                                    outside_activity=outside_activity,
                                    outside_assessment_strategy=outside_assessment_strategy,
                                    inside_activity=inside_activity,
                                    inside_assessment_activity=inside_assessment_activity,
                                    knowledge_level=knowledge_level, students_engaged=students_engaged,
                                    expected_proficiency=expected_proficiency,
                                    total_assessment_marks=total_assessment_marks,
                                    assessment_analysis=assessment_analysis, follow_up_actions=follow_up_actions)

        db.session.add( flipped_form_data)
        db.session.commit()
        return "Form submitted successfully!"
    else:
        return render_template('flipped.html')
    

@app.route('/method_selection', methods=['POST','GET'])
def meth():
    if request.method == 'POST':
        if request.form['submit_button'] == "Tps":
            return render_template("tps.html")
        elif request.form['submit_button'] == "Seminar" :
            return render_template("seminar.html")
        elif request.form['submit_button'] == "Flipped" :
            return render_template("flipped.html")
        elif request.form['submit_button'] == "Minute" :
            return render_template("minute.html")
        
        
    else:
        return render_template("al-method.html")

@app.route('/filter', methods=['POST','GET'])
def fil():
    if request.method == 'POST':
        if request.form['submit_button'] == "Filter":
            return render_template("filter.html")
        elif request.form['submit_button'] == "Add" :
            return render_template("al-method.html")




if __name__ == '__main__':
    with app.app_context():
        # Create the database
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
