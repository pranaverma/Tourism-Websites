from flask import Flask, render_template, redirect, flash, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/protravelo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

class Register(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Username = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Mobile_number = db.Column(db.String(255), nullable=False)


class Customer(db.Model):
    ID = db.Column(db.Integer, db.ForeignKey("register.ID"), primary_key=True)
    Name = db.Column(db.String(255))
    DOB = db.Column(db.Date)
    Gender = db.Column(db.String(255))
    Country = db.Column(db.String(255))
    Address = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    Mobile_number = db.Column(db.Integer)
    Alternate_mobile_number = db.Column(db.Integer)
    Language = db.Column(db.String(255))
    Currency = db.Column(db.String(255))
    Passport_number = db.Column(db.Integer)


class Travel_agent(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Rating = db.Column(db.Integer)
    Price = db.Column(db.Integer)


class Hotels(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Price = db.Column(db.Integer)


class Feedback(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Travel_agent_feedback = db.Column(db.String(255))
    Hotel_feedback = db.Column(db.String(255))
    Journey_feedback = db.Column(db.String(255))
    Suggestions = db.Column(db.String(255))


class Booking(db.Model):
    Booking_ID = db.Column(db.Integer, primary_key=True)
    ID = db.Column(db.Integer, db.ForeignKey("register.ID"))
    Start_date = db.Column(db.Date)
    Number_of_days = db.Column(db.Integer)
    Country = db.Column(db.String(255))
    City1 = db.Column(db.String(255))
    City2 = db.Column(db.String(255))
    City3 = db.Column(db.String(255))
    City4 = db.Column(db.String(255))
    Hotel1 = db.Column(db.String(255))
    Hotel2 = db.Column(db.String(255))
    Hotel3 = db.Column(db.String(255))
    Hotel4 = db.Column(db.String(255))
    Travel_agent_ID = db.Column(db.Integer, db.ForeignKey("travel_agent.ID"))
    Number_of_people = db.Column(db.Integer)
    Final_price = db.Column(db.Integer)
    Progress = db.Column(db.String(255))


class Group_details(db.Model):
    ID = db.Column(db.Integer, db.ForeignKey("register.ID"))
    Name = db.Column(db.String(255))
    DOB = db.Column(db.Date)
    Gender = db.Column(db.String(255))
    Address = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    Mobile_number = db.Column(db.Integer)
    Alternate_mobile_number = db.Column(db.Integer)
    Passport_number = db.Column(db.Integer, primary_key=True)


class Packages(db.Model):
    Package_ID = db.Column(db.Integer, primary_key=True)
    Package_name = db.Column(db.String(255))
    Individual_price = db.Column(db.Integer)


class Travel_agent_register(db.Model):
    Name = db.Column(db.String(255))
    DOB = db.Column(db.Date)
    Gender = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    Address = db.Column(db.String(255))
    Mobile_number = db.Column(db.String(255))
    Country = db.Column(db.String(255))
    Passport_number = db.Column(db.String(255), primary_key=True)
    Languages_known = db.Column(db.String(255))


class Selected_package(db.Model):
    Booking_ID = db.Column(db.Integer, primary_key=True)
    ID = db.Column(db.Integer, db.ForeignKey('register.ID'))
    Name = db.Column(db.String(255))
    Package_name = db.Column(db.String(255))
    Number_of_people = db.Column(db.Integer)
    Number_of_days = db.Column(db.Integer)
    Progress = db.Column(db.String(255))
    Departing_date = db.Column(db.String(255))
    Final_price = db.Column(db.Integer)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/countries")
def countries():
    return render_template("countries.html")


@app.route("/australia")
def australia():
    return render_template("australia.html")


@app.route("/france")
def france():
    return render_template("france.html")


@app.route("/greece")
def greece():
    return render_template("greece.html")


@app.route("/hong_kong")
def hong_kong():
    return render_template("hong_kong.html")


@app.route("/italy")
def italy():
    return render_template("italy.html")


@app.route("/mauritius")
def mauritius():
    return render_template("mauritius.html")


@app.route("/switzerland")
def switzerland():
    return render_template("switzerland.html")


@app.route("/uae")
def uae():
    return render_template("uae.html")


@app.route("/australia_hotel")
def australia_hotel():
    return render_template("australia_hotels.html")


@app.route("/france_hotel")
def france_hotel():
    return render_template("france_hotels.html")


@app.route("/greece_hotel")
def greece_hotel():
    return render_template("greece_hotels.html")


@app.route("/hong_kong_hotel")
def hong_kong_hotel():
    return render_template("hong_kong_hotel.html")


@app.route("/italy_hotel")
def italy_hotel():
    return render_template("italy_hotels.html")


@app.route("/mauritius_hotel")
def mauritius_hotel():
    return render_template("mauritius_hotel.html")


@app.route("/switzerland_hotel")
def switzerland_hotel():
    return render_template("switzerland_hotel.html")


@app.route("/uae_hotel")
def uae_hotel():
    return render_template("uae_hotel.html")


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@app.route("/feedback")
def feedback():
    return render_template("Feedback.html")


@app.route("/payment")
def payment():
    return render_template("payment.html")


@app.route("/customer_details")
def customer_details():
    return render_template("customer_details.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/choose_package")
def choose_package():
    return render_template("choose_package.html")


@app.route("/select_package")
def select_package():
    return render_template("select_package.html")


@app.route("/show_bookings")
def show_bookings():
    return render_template("show_bookings.html")


@app.route("/group_details")
def group_details():
    return render_template("group_details.html")


@app.route("/travel_agent_register")
def travel_agent_register():
    return render_template("travel_agent_register.html")


@app.route("/packages")
def packages():
    return render_template("packages.html")


@app.route("/australia_package")
def australia_package():
    return render_template("australia_package.html")


@app.route("/france_package")
def france_package():
    return render_template("france_package.html")


@app.route("/greece_package")
def greece_package():
    return render_template("greece_package.html")


@app.route("/hong_kong_package")
def hong_kong_package():
    return render_template("hong_kong_package.html")


@app.route("/italy_package")
def italy_package():
    return render_template("italy_package.html")


@app.route("/mauritius_package")
def mauritius_package():
    return render_template("mauritius_package.html")


@app.route("/switzerland_package")
def switzerland_package():
    return render_template("switzerland_package.html")


@app.route("/uae_package")
def uae_package():
    return render_template("uae_package.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/italy_and_switzerland")
def italy_and_switzerland():
    return render_template("group1_package.html")


@app.route("/greece_and_italy")
def greece_and_italy():
    return render_template("group2_package.html")


@app.route("/classical_europe")
def classical_europe():
    return render_template("group3_package.html")


@app.route("/fantastic_four")
def fantastic_four():
    return render_template("group4_package.html")


user_ID = 0

@app.route("/register", methods=['GET', 'POST'])
def register():
    if(request.method == 'POST'):

        name = request.form.get('name')
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        mobile_number = request.form.get('mobile_number')

        user = Register.query.filter_by(Username=user_name).first()
        if user:
            flash(
                'This username is already taken. Please login or retry with a different username!')
            return redirect(url_for('admin'))

        entry = Register(Name=name, Username=user_name,
                         Password=password, Mobile_number=mobile_number)
        db.session.add(entry)
        db.session.commit()

    return redirect(url_for('admin'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if (request.method == "POST"):
        user_name = request.form.get('user_name')
        password = request.form.get('password')

        user = Register.query.filter_by(Username=user_name).first()
        userpd = Register.query.filter_by(Password=password).first()

        if not user:
            flash('Please register before!')
            return redirect(url_for('admin'))
        elif not userpd:
            flash('Please check your password.')
            return redirect(url_for('admin'))
        global user_ID
        user_ID = user.ID

    return redirect(url_for('customer_details'))


@app.route("/customer", methods=['GET', 'POST'])
def customer():
    if (request.method == "POST"):
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        dob = request.form.get("dob")
        gender = request.form.get("gender")
        country = request.form.get("country")
        address1 = request.form.get("address1")
        address2 = request.form.get("address2")
        email = request.form.get("email")
        mobile_number = request.form.get("mobile_number")
        alternate_mobile_number = request.form.get("alternate_mobile_number")
        language = request.form.get("language")
        currency = request.form.get("currency")
        passport_number = request.form.get("passport_number")

        name = first_name+" "+last_name
        address = address1+" "+address2

        user = Customer.query.filter_by(ID=user_ID).first()
        if user:
            flash('You have already filled these details.')
            return redirect(url_for("customer_details"))

        entry = Customer(ID=user_ID, Name=name, DOB=dob, Gender=gender, Country=country, Address=address, Email=email, Mobile_number=mobile_number,
                         Alternate_mobile_number=alternate_mobile_number, Language=language, Currency=currency, Passport_number=passport_number)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("choose_package"))

    return redirect(url_for("choose_package"))


@app.route("/bookingform", methods=['GET', 'POST'])
def bookingform():
    if request.method == "POST":
        start_date = request.form.get("start_date")
        number_of_days = request.form.get("number_of_days")
        country = request.form.get("country")
        travel_agent = request.form.get("travel_agent")
        city1 = request.form.get("city1")
        city2 = request.form.get("city2")
        city3 = request.form.get("city3")
        city4 = request.form.get("city4")
        firsthotel = request.form.get("firsthotel")
        secondhotel = request.form.get("secondhotel")
        thirdhotel = request.form.get("thirdhotel")
        fourthhotel = request.form.get("fourthhotel")
        number_of_people = request.form.get("number_of_people")

        agent_price = 0
        firsthotel_price = 0
        secondhotel_price = 0
        thirdhotel_price = 0
        fourthhotel_price = 0
        country_price = 0
        if (travel_agent != "" or travel_agent != "None"):
            agent = Travel_agent.query.filter_by(Name=travel_agent).first()
            aprice = agent.Price
            agent_price = int(aprice)

        if (firsthotel != "" or firsthotel != "None"):
            firsthotelselect = Hotels.query.filter_by(Name=firsthotel).first()
            if(firsthotelselect!=""):
                firsthotel_price = int(firsthotelselect.Price)
        if (secondhotel != "" or secondhotel != "None"):
            secondhotelselect = Hotels.query.filter_by(Name=secondhotel).first()
            if(secondhotelselect!=""):
                secondhotel_price = int(secondhotelselect.Price)
        if (thirdhotel != "" or thirdhotel != "None"):
            thirdhotelselect = Hotels.query.filter_by(Name=thirdhotel).first()
            if(thirdhotelselect!=""):
                thirdhotel_price = int(thirdhotelselect.Price)
        if (fourthhotel != "" or fourthhotel != "None"):
            fourthhotelselect = Hotels.query.filter_by(Name=fourthhotel).first()
            if(fourthhotelselect!=""):
                fourthhotel_price = int(fourthhotelselect.Price)

        if (country == "Australia"):
            country_price = 70000
        elif(country == "France"):
            country_price = 71000
        elif(country == "Greece"):
            country_price = 72000
        elif(country == "Hong Kong"):
            country_price = 73000
        elif(country == "Italy"):
            country_price = 74000
        elif(country == "Mauritius"):
            country_price = 75000
        elif(country == "Switzerland"):
            country_price = 76000
        elif(country == "UAE"):
            country_price = 77000

        total = agent_price+(firsthotel_price+secondhotel_price+thirdhotel_price +
                             fourthhotel_price)*int(number_of_days)*int(number_of_people)/2+country_price*int(number_of_people)

        entry = Booking(ID=user_ID, Travel_agent_ID=agent.ID, Number_of_people=number_of_people, Start_date=start_date, Number_of_days=number_of_days, Country=country,
                        City1=city1, City2=city2, City3=city3, City4=city4, Hotel1=firsthotel, Hotel2=secondhotel, Hotel3=thirdhotel, Hotel4=fourthhotel, Final_price=total, Progress="Not Completed")
        db.session.add(entry)
        db.session.commit()

        return redirect(url_for("group_details"))

    return render_template(".html")


@app.route("/group_info_more", methods=["GET", "POST"])
def group_info_more():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        dob = request.form.get("dob")
        gender = request.form.get("gender")
        email = request.form.get("email")
        mobile_number = request.form.get("mobile_number")
        alternate_mobile_number = request.form.get("alternate_mobile_number")
        address = request.form.get("address")
        passport_number = request.form.get("passport_number")

        user = Group_details.query.filter_by(Passport_number=passport_number).first()
        if user:
            flash('we have saved your details')
            return redirect(url_for("group_details"))

        name = first_name+" "+last_name
        entry = Group_details(ID=user_ID, Name=name, DOB=dob, Gender=gender, Email=email, Mobile_number=mobile_number,
                              Alternate_mobile_number=alternate_mobile_number, Address=address, Passport_number=passport_number)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("group_details"))

    return redirect(url_for("group_details"))


@app.route("/group_info", methods=["GET", "POST"])
def group_info():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        dob = request.form.get("dob")
        gender = request.form.get("gender")
        email = request.form.get("email")
        mobile_number = request.form.get("mobile_number")
        alternate_mobile_number = request.form.get("alternate_mobile_number")
        address = request.form.get("address")
        passport_number = request.form.get("passport_number")

        user = Group_details.query.filter_by(Passport_number=passport_number).first()
        if user:
            flash('we have saved your details')
            return redirect(url_for("group_details"))

        name = first_name+" "+last_name
        entry = Group_details(ID=user_ID, Name=name, DOB=dob, Gender=gender, Email=email, Mobile_number=mobile_number,
                              Alternate_mobile_number=alternate_mobile_number, Address=address, Passport_number=passport_number)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("choose_package"))

    return redirect(url_for("choose_package"))


@app.route("/travel_agent_register_form", methods=["GET", "POST"])
def travel_agent_register_form():
    if request.method == "POST":
        name = request.form.get("name")
        dob = request.form.get("dob")
        gender = request.form.get("gender")
        email = request.form.get("email")
        address = request.form.get("address")
        mobile_number = request.form.get("mobile_number")
        country = request.form.get("country")
        passport_number = request.form.get("passport_number")
        languages_known = request.form.get("languages_known")

        user = Travel_agent_register.query.filter_by(Passport_number=passport_number).first()
        if user:
            flash('You have already applied. Wait for response from our side!')
            return redirect(url_for("travel_agent_register"))

        entry = Travel_agent_register(Name=name, DOB=dob, Gender=gender, Email=email, Address=address,
                                      Mobile_number=mobile_number, Country=country, Passport_number=passport_number, Languages_known=languages_known)
        db.session.add(entry)
        db.session.commit()

        return redirect(url_for("home"))

    return redirect(url_for("home"))


@app.route("/select_package_form", methods=["GET", "POST"])
def select_package_form():
    if (request.method == "POST"):

        name = request.form.get("name")
        package_name = request.form.get("package")
        number_of_people = request.form.get("number_of_people")
        departing_date = request.form.get("departing_date")
        number_of_days = "0"
        if(package_name =="Australia Package" or package_name=="Italy Package" or package_name=="Switzerland Package" or package_name=="Mauritius Package" or package_name=="France Package" or package_name=="Greece Package" or package_name=="Hong Kong Package" or package_name=="UAE Package"):
            number_of_days = "9";
        elif(package_name=="Italy and Switzerland" or package_name=="Greece and Italy" or package_name=="Classical Europe"):
            number_of_days = "11";
        else:
            number_of_days = "13";

        pack = Packages.query.filter_by(Package_name=package_name).first()
        package_price = pack.Individual_price

        total = int(package_price)* int(number_of_people)

        entry = Selected_package(ID=user_ID, Name=name, Package_name=package_name, Number_of_people=number_of_people, Progress="Not Completed", Departing_date=departing_date, Final_price=total,Number_of_days=number_of_days)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("group_details"))

    return redirect(url_for("group_details"))
@app.route("/show_booking_results", methods=["GET", "POST"])
def show_booking_results():
    bookings = Booking.query.filter_by(ID=user_ID).all()
    packages = Selected_package.query.filter_by(ID=user_ID).all()
    return render_template("show_bookings.html", bookings=bookings, packages=packages)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Booking.query.filter_by(Booking_ID=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("show_booking_results"))

@app.route('/deleteP/<int:sno>')
def deleteP(sno):
    todo = Selected_package.query.filter_by(Booking_ID=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("show_booking_results"))

@app.route('/payment_details', methods=['GET','POST'])
def payment_details():
    total1=0
    total2=0
    total=0
    bookings = Booking.query.filter_by(ID=user_ID).all()
    packages = Selected_package.query.filter_by(ID=user_ID).all()
    for member in bookings:
        if(member.Progress == "Not Completed"):
            total1 = total1+int(member.Final_price)
    for member in packages:
        if(member.Progress == "Not Completed"):
            total2 = total2+int(member.Final_price)

    total = total1+total2
    return render_template("payment.html", bookings=bookings, packages=packages, total=total)

@app.route('/payment_complete', methods=['GET', 'POST'])
def payment_complete():
    bookings = Booking.query.filter_by(ID=user_ID).all()
    packages = Selected_package.query.filter_by(ID=user_ID).all()
    for member in bookings:
        member.Progress = "Completed"
        db.session.add(member)
        db.session.commit()
    for member in packages:
        member.Progress = "Completed"
        db.session.add(member)
        db.session.commit()
    return redirect(url_for("choose_package"))

@app.route('/feedback_form', methods=['GET', 'POST'])
def feedback_form():
    if(request.method == "POST"):
        taf = request.form.get("rating1")
        hf = request.form.get("rating2")
        jf = request.form.get("rating")
        sugg = request.form.get("commentText")

        entry = Feedback(Travel_agent_feedback=taf,Hotel_feedback=hf,Journey_feedback=jf,Suggestions=sugg)

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("choose_package"))
    return redirect(url_for("choose_package"))


if __name__ == "__main__":
    app.run(debug=True)