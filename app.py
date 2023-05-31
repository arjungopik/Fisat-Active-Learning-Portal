from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:user@localhost:5432/active'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



   

class FormData(db.Model):
    __tablename__ = 'form_data'
    id = db.Column(db.Integer, primary_key=True)
    academic_year = db.Column(db.String)
    date = db.Column(db.Date)
    class_name = db.Column(db.String)
    faculty_id =  db.Column(db.String)
    faculty_in_charge = db.Column(db.String)
    course_code = db.Column(db.String)
    course_name = db.Column(db.String)
    topic = db.Column(db.String)
    activity =db.Column(db.String)


class SeminarFormData(db.Model):
    __tablename__ = 'seminar_form_data'
    id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.Integer)
    learning_outcome = db.Column(db.String)
    addressed_course_outcomes = db.Column(db.String)
    no_of_students_engaged = db.Column(db.String)
    assessment_strategy = db.Column(db.String)
    expected_proficiency = db.Column(db.String)
    total_assessment_marks = db.Column(db.String)
    assessment_analysis = db.Column(db.String)
    follow_up_actions = db.Column(db.String)

class SeminarData(db.Model):
    __tablename__ = 'seminardata'
    id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.Integer)
    stud_name = db.Column(db.String)
    rollno =  db.Column(db.String)
    contribution =  db.Column(db.String)


class TPSFormData(db.Model):
    __tablename__ = 'tps_form_data'
    id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.Integer)
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



class MinuteFormData(db.Model):
    __tablename__ = 'minute_form_data'
    id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.Integer)
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




class FlippedFormData(db.Model):
    __tablename__ = 'flipped_form_data'
    id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.Integer)
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
        if id== "1":
            tps_data = FormData.query.all()
            return render_template('hodpage.html', tps_data=tps_data)
        elif id=="2":
            tps_data = FormData.query.filter_by(faculty_in_charge="1").all()
            return render_template('facultypage.html', tps_data=tps_data)
        else:
            return " invalid user"
    else:
        return render_template('login.html')


@app.route('/minute', methods=['GET', 'POST'])
def minute():
    if request.method == 'POST':
        academic_year = request.form.get('academic_year')
        date = request.form.get('date')
        class_name = request.form.get('class_name   ')
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
        concepts_expansion = request.form.get('concepts_need_expansion')
        percentage_students_expansion = request.form.get('percentage_students_expansion')
        follow_up_actions = request.form.get('follow_up_actions')

        form_data = FormData(academic_year=academic_year, date=date, class_name=class_name,
                                    faculty_in_charge=faculty_in_charge, course_code=course_code,
                                    course_name=course_name, topic=topic,activity="THE MINUTE PAPER")
        
        db.session.add(form_data)
        db.session.commit()
        inserted_id =form_data.id

        minute_form_data = MinuteFormData(data_id=inserted_id, learning_outcome=learning_outcome,
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
        return redirect(url_for('previewtps', id=inserted_id))
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

        form_data = FormData(academic_year=academic_year, date=date, class_name=class_name,
                                    faculty_in_charge=faculty_in_charge, course_code=course_code,
                                    course_name=course_name, topic=topic,activity="THINK PAIR SHARE")
        
        db.session.add(form_data)
        db.session.commit()
        inserted_id =form_data.id

        tps_form_data = TPSFormData(data_id=inserted_id, learning_outcome=learning_outcome,
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
        return redirect(url_for('previewtps', id=inserted_id))
        
    else:
    
        return render_template('tps.html')
    
@app.route('/flip', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        academic_year = request.form.get('academic_year')
        date = request.form.get('date')
        class_name = request.form.get('class_name')
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


        form_data = FormData(academic_year=academic_year, date=date, class_name=class_name,
                                    faculty_in_charge=faculty_in_charge, course_code=course_code,
                                    course_name=course_name, topic=topic,activity="FLIPPED CLASSROOM")
        
        db.session.add(form_data)
        db.session.commit()
        inserted_id =form_data.id

        flipped_form_data = FlippedFormData(data_id=inserted_id, learning_outcome=learning_outcome,
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
        return redirect(url_for('previewtps', id=inserted_id))
        
    else:
        return render_template('flipped.html')
    


@app.route('/activity_seminar', methods=['POST'])
def activity_seminar():
    if request.method == 'POST':
        academic_year = request.form.get('academic_year')
        date = request.form.get('date')
        class_name = request.form.get('class_name')
        faculty_in_charge = request.form.get('faculty_in_charge')
        course_code = request.form.get('course_code')
        course_name = request.form.get('course_name')
        topic = request.form.get('topic')   
        learning_outcome = request.form.get('learning_outcome')
        addressed_course_outcomes = request.form.get('addressed_course_outcomes')

        assessment_strategy = request.form.get('assessment_strategy')
        expected_proficiency = request.form.get('expected_proficiency')
        total_assessment_marks = request.form.get('total_assessment_marks')
        assessment_analysis = request.form.get('assessment_analysis')
        follow_up_actions = request.form.get('follow_up_actions')
        



        form_data = FormData(academic_year=academic_year, date=date, class_name=class_name,
                                    faculty_in_charge=faculty_in_charge, course_code=course_code,
                                    course_name=course_name, topic=topic,activity="SEMINAR")
        
       


        db.session.add(form_data)
        db.session.commit()
        inserted_id =form_data.id

        counter=1
        name=request.form.get('name'+str(counter))     

        rollno=request.form.get('roll_no'+str(counter))
        contribution=request.form.get('contribution'+str(counter))
        seminardata=SeminarData(data_id=inserted_id,stud_name=name,rollno=rollno,contribution=contribution)
        counter+=1
        db.session.add(seminardata)
        db.session.commit()
        semianr_form_data = SeminarFormData(data_id=inserted_id,
        learning_outcome=learning_outcome,
        addressed_course_outcomes=addressed_course_outcomes,
        assessment_strategy=assessment_strategy,
        expected_proficiency=expected_proficiency,
        total_assessment_marks=total_assessment_marks,
        assessment_analysis=assessment_analysis,
        follow_up_actions=follow_up_actions)

        db.session.add(semianr_form_data)
        db.session.commit()

        return redirect(url_for('previewtps', id=inserted_id))
    else:
        return render_template('seminar.html')


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
        
@app.route('/preview/<id>')
def previewtps(id):
    data = FormData.query.filter_by(id=id).first()
    if data.activity=="THINK PAIR SHARE":
        tpsdata = TPSFormData.query.filter_by(data_id=id).first()
        dict = {
            'academic_year': data.academic_year,
            'date': data.date,
            'class_name': data.class_name,
            'faculty_id': data.faculty_id,
            'faculty_in_charge': data.faculty_in_charge,
            'course_code': data.course_code,
            'course_name': data.course_name,
            'topic': data.topic,
            'activity': data.activity,
            'learning_outcome': tpsdata.learning_outcome,
            'addressed_course_outcomes': tpsdata.addressed_course_outcomes,
            'knowledge_level_assessment': tpsdata.knowledge_level_assessment,
            'questions': tpsdata.questions,
            'think_phase': tpsdata.think_phase,
            'pair_phase': tpsdata.pair_phase,   
            'share_phase': tpsdata.share_phase,
            'alloted_time': tpsdata.alloted_time,
            'students_engaged': tpsdata.students_engaged,
            'conclusion': tpsdata.conclusion,
            'expected_proficiency': tpsdata.expected_proficiency,
            'total_assessment_marks': tpsdata.total_assessment_marks,
            'assessment_analysis': tpsdata.assessment_analysis,
            'concepts_expansion': tpsdata.concepts_expansion,
            'percentage_students_expansion': tpsdata.percentage_students_expansion,
            'follow_up_actions': tpsdata.follow_up_actions
        }
        return render_template('preview.html', dict=dict)
    elif data.activity=="FLIPPED CLASSROOM":
        flipped_data = FlippedFormData.query.filter_by(data_id=id).first()
        dict = {
            'academic_year': data.academic_year,
            'date': data.date,
            'class_name': data.class_name,
            'faculty_id': data.faculty_id,
            'faculty_in_charge': data.faculty_in_charge,
            'course_code': data.course_code,
            'course_name': data.course_name,
            'topic': data.topic,
            'activity': data.activity,
            'data_id': flipped_data.data_id,
            'learning_outcome': flipped_data.learning_outcome,
            'addressed_course_outcomes': flipped_data.addressed_course_outcomes,
            'video_url': flipped_data.video_url,
            'outside_activity': flipped_data.outside_activity,
            'outside_assessment_strategy': flipped_data.outside_assessment_strategy,
            'inside_activity': flipped_data.inside_activity,
            'inside_assessment_activity': flipped_data.inside_assessment_activity,
            'knowledge_level': flipped_data.knowledge_level,
            'students_engaged': flipped_data.students_engaged,
            'expected_proficiency': flipped_data.expected_proficiency,
            'total_assessment_marks': flipped_data.total_assessment_marks,
            'assessment_analysis': flipped_data.assessment_analysis,
            'follow_up_actions': flipped_data.follow_up_actions
        }
        return render_template('preview.html', dict=dict)
    elif data.activity=="THE MINUTE PAPER":
        minute_data = MinuteFormData.query.filter_by(data_id=id).first()
        dict = {
            'academic_year': data.academic_year,
            'date': data.date,
            'class_name': data.class_name,
            'faculty_id': data.faculty_id,
            'faculty_in_charge': data.faculty_in_charge,
            'course_code': data.course_code,
            'course_name': data.course_name,
            'topic': data.topic,
            'activity': data.activity,
            'learning_outcome': minute_data.learning_outcome,
            'addressed_course_outcomes': minute_data.addressed_course_outcomes,
            'no_of_students_engaged': minute_data.no_of_students_engaged,
            'assessment_questions': minute_data.assessment_questions,
            'alloted_time': minute_data.alloted_time,
            'students_supposed_to': minute_data.students_supposed_to,
            'expected_proficiency': minute_data.expected_proficiency,
            'total_assessment_marks': minute_data.total_assessment_marks,
            'assessment_analysis': minute_data.assessment_analysis,
            'concepts_expansion': minute_data.concepts_expansion,
            'percentage_students_expansion': minute_data.percentage_students_expansion,
            'follow_up_actions': minute_data.follow_up_actions
        }
        return render_template('preview.html', dict=dict)
    elif data.activity=="SEMINAR":
        data = FormData.query.filter_by(id=id).first()
        seminar_data = SeminarFormData.query.filter_by(data_id=id).first()
        dict = {
            'academic_year': data.academic_year,
            'date': data.date,
            'class_name': data.class_name,
            'faculty_id': data.faculty_id,
            'faculty_in_charge': data.faculty_in_charge,
            'course_code': data.course_code,
            'course_name': data.course_name,
            'topic': data.topic,
            'activity': data.activity,
            'learning_outcome': seminar_data.learning_outcome,
            'addressed_course_outcomes': seminar_data.addressed_course_outcomes,
            'assessment_strategy': seminar_data.assessment_strategy,
            'expected_proficiency': seminar_data.expected_proficiency,
            'total_assessment_marks' : seminar_data.total_assessment_marks,
            'assessment_analysis': seminar_data.assessment_analysis,
            'follow_up_actions': seminar_data.follow_up_actions
        }
        return render_template('preview.html', dict=dict)

    else:
        return "error"


    
    



if __name__ == '__main__':
    with app.app_context():
        # Create the database
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
