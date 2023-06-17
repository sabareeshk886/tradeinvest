import smtplib

from flask import Flask, render_template, request, session, redirect, jsonify
from DBConnection import Db

app = Flask(__name__)
app.secret_key="123"

import json
from web3 import Web3, HTTPProvider
blockchain_address = 'http://127.0.0.1:7545'
web3 = Web3(HTTPProvider(blockchain_address))
web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path = 'C:\\smartcontracts\\build\\contracts\\Investment.json'
deployed_contract_address = '0x1C060a6a63B06b37dc9101DEbB8C3436c417E9c3'
deployed_contract_addressa = web3.eth.accounts[5]



@app.route('/')
def login():
    return render_template('login_index.html')


@app.route('/login_post',methods=['post'])
def login_post():
    username=request.form['textfield']
    password=request.form['textfield2']
    db=Db()
    qry="SELECT * FROM login WHERE `user_name`='"+username+"' AND `password`='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        session['lid']=res['login_id']
        if res['type']=='admin':
            return redirect('/a_home')
        elif res['type']=='company':
            return redirect('/c_home')
        else :
            return '''<script>alert('invalid');window.location='/'</script>'''
    else :
        return '''<script>alert('invalid');window.location='/'</script>'''


@app.route('/logout')
def logout():
    session['lid']=''
    return redirect('/')


@app.route('/signup_app')
def signup_app():
    return render_template('app_index.html')





@app.route('/approve_company/<id>')
def approve_company(id):
    if session['lid'] != '':
        db=Db()
        qry="UPDATE `company`SET`status`='approved' WHERE `C_id`='"+id+"'"
        res=db.update(qry)
        return '''<script>alert('approved');window.location='/company_list'</script>'''
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/rejected_company/<id>')
def rejected_company(id):
    if session['lid'] != '':
        db=Db()
        qry="UPDATE `company`SET`status`='rejected' WHERE `C_id`='"+id+"'"
        res=db.update(qry)
        return '''<script>alert('rejected');window.location='/company_list'</script>'''
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/approved_list')
def approved_list():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM company WHERE STATUS='approved'"
        res = db.select(qry)
        return render_template("admin/APPROVED LIST.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/rejected_list')
def rejected_list():
    if session['lid'] != '':
        db=Db()
        qry="SELECT * FROM company WHERE STATUS='rejected'"
        res=db.select(qry)
        return render_template("admin/REJECTED LIST.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/change_password')
def change_password():
    if session['lid'] != '':
        return render_template("admin/change passsword.html")
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/change_password_post',methods=['post'])
def change_password_post():
    if session['lid'] != '':
        CURRENTPASSWORD=request.form['textfield']
        NEWPASSWORD=request.form['textfield2']
        CONFIRMPASSWORD=request.form['textfield4']
        db=Db()
        qry="SELECT * FROM login WHERE `password`='"+CURRENTPASSWORD+"' AND `login_id`='"+str(session['lid'])+"'"
        res=db.selectOne(qry)
        if NEWPASSWORD==CONFIRMPASSWORD :
            db=Db()
            qry="UPDATE login SET `password`='"+CONFIRMPASSWORD+"' WHERE `login_id`='"+str(session['lid'])+"'"
            res=db.update(qry)
            return '''<script>alert('Sucessfully changed');window.location='/'</script>'''
        else :
            return '''<script>alert('Invalid credentials');window.location='/change_password'</script>'''
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/company_list')
def company_list():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM company where status='pending'"
        res = db.select(qry)
        return render_template("admin/COMPANY LIST.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/company_list_post',methods=['post'])
def company_list_post():
    if session['lid'] != '':
        search=request.form['textfield']
        db=Db()
        qry="SELECT * FROM company WHERE STATUS='pending' and `c_name` LIKE '%"+search+"%'"
        res=db.select(qry)
        return render_template("admin/COMPANY LIST.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/send_reply/<id>')
def complaint_reply(id):
    if session['lid'] != '':
        return render_template("admin/COMPLAINT  REPLY.html",id=id)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/complaint_reply_post',methods=['post'])
def complaint_reply_post():
    if session['lid'] != '':
        reply=request.form['textarea']
        id=request.form['complaint_id']
        db=Db()
        qry="UPDATE `complaint`SET `reply`='"+reply+"',`status`='replied' WHERE `complaint_id`='"+id+"'"
        res=db.update(qry)
        return '''<script>alert('sending');window.location='/complaints'</script>'''
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/complaints')
def complaints():
    if session['lid'] != '':
        db=Db()
        qry="SELECT * FROM `complaint`INNER JOIN `trader` ON `complaint`.`user_id`=`trader`.`l_id`"
        res=db.select(qry)
        return render_template("admin/COMPLAINTS.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/feedback')
def feedback():
    if session['lid'] != '':
        db=Db()
        qry="SELECT * FROM `feedback` INNER JOIN `trader`ON feedback.user_id=`trader`.`l_id` "
        res=db.select(qry)
        return render_template("admin/FEEDBACK.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/view_traders')
def view_traders():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM trader"
        res = db.select(qry)
        return render_template("admin/VIEW TRADER.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/view_complaints')
def view_complaints():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM `complaint` INNER JOIN `trader` ON `trader`.`user_id`=`complaint`.`user_id`  "
        res = db.select(qry)
        return render_template("admin/COMPLAINTS.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/view_complaints_post',methods=['post'])
def view_complaints_post():
    if session['lid'] != '':
        from_date=request.form['textfield']
        to=request.form['textfield2']
        db=Db()
        qry="SELECT * FROM `complaint` INNER JOIN `trader` ON `trader`.`user_id`=`complaint`.`user_id` WHERE `date` BETWEEN '"+from_date+"' AND '"+to+"'"
        res=db.select(qry)
        return render_template("admin/COMPLAINTS.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/a_home')
def a_home():
    if session['lid']!='':
        return render_template("admin/a_home.html")
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''



# ========================================== COMPANY=====================================================================#

@app.route('/signup_1')
def signup_1():
    return render_template("sindex.html")










@app.route('/signup_1_post',methods=['post'])
def signup_1_post():
    EMAIL= request.form['textfield']
    VERIFICATIONCODE = request.form['textfield2']
    CREATEPASSWORD = request.form['textfield4']
    VERIFYPASSWORD= request.form['textfield4']
    db=Db()
    return "ok"



@app.route('/registration_form')
def registration_form():
    return render_template("company/registration_form.html")

@app.route('/regstration_form_post',methods=['post'])
def registration_fotm_post():
    COMPANY_NAME = request.form['textfield']
    TAX_ID = request.form['textfield3']
    LEGAL_STATUS = request.form['textfield6']
    FIELD_OF_BUSINESS = request.form['textfield7']
    REGISTERED_OFFICE = request.form['textfield8']
    STATE = request.form['textfield4']
    REGION = request.form['textfield5']
    MUNCIPALITY = request.form['textfield9']
    POSTAL_CODE = request.form['textfield10']
    STREET = request.form['textfield11']
    NUMBER = request.form['textfield12']
    EMAIL = request.form['textfield13']
    TELEPHONE = request.form['textfield14']
    FAX = request.form['textfield15']
    POSTAL_ADDRESS = request.form['textfield16']
    LOGO = request.files['fileField']
    from  datetime import datetime
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    LOGO.save("C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\LOGO\\" + dt + ".jpg")
    path = "/static/company/LOGO/" + dt + ".jpg"
    CITY = request.form['textfield19']
    COUNTRY = request.form['textfield20']
    BANK = request.form['textfield21']
    ACCOUNT_NUMBER = request.form['textfield22']
    IFSC = request.form['textfield23']
    TITLE = request.form['textfield24']
    NAME = request.form['textfield26']
    SURNAME = request.form['textfield27']
    DOB = request.form['textfield25']

    PROOF_OF_FINANCIAL_ELIGIBILITY = request.files['fileField']
    from  datetime import datetime
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    PROOF_OF_FINANCIAL_ELIGIBILITY.save(
        "C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\PROOF\\" + dt + ".jpg")
    path1 = "/static/company/PROOF/" + dt + ".jpg"
    BANK_GUARANTEE = request.files['fileField2']
    from  datetime import datetime
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    BANK_GUARANTEE.save("C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\BANK_PROOF\\" + dt + ".jpg")
    path2 = "/static/company/BANK_PROOF/" + dt + ".jpg"
    checkbox = request.form['textfield4']
    db=Db()

    import random
    password=random.randint(1000000, 9999999)

    qry1="INSERT INTO `login` (`user_name`,`password`,`type`) VALUES('"+EMAIL+"','"+str(password)+"','company')"
    res=db.insert(qry1)

    qry="INSERT INTO `company` (`l_id`,`logo`,`c_name`,`tax_id`,`legal_status`,`field_of_business`,`registered_office`,`state`,`region`,`muncipality`,`postcode`,`street`,`phone_number`,`email`,`telephone`,`fax`,`postal_address`,`city`,`country`,`bank_name`,`bank_number`,`ifsc_code`,`director_name`,`director_title`,`director_surname`,`director_dob`,`bankguarantee`,`proof_of_financialeligibility`) VALUES ('"+str(res)+"','"+path+"','"+COMPANY_NAME+"','"+TAX_ID+"','"+LEGAL_STATUS+"','"+FIELD_OF_BUSINESS+"','"+REGISTERED_OFFICE+"','"+STATE+"','"+REGION+"','"+MUNCIPALITY+"','"+POSTAL_CODE+"','"+STREET+"','"+NUMBER+"','"+EMAIL+"','"+TELEPHONE+"','"+FAX+"','"+POSTAL_ADDRESS+"','"+CITY+"','"+COUNTRY+"','"+BANK+"','"+ACCOUNT_NUMBER+"','"+IFSC+"','"+NAME+"','"+TITLE+"','"+SURNAME+"','"+DOB+"','"+path1+"','"+path2+"')"
    res=db.insert(qry)

    import smtplib
    from email.message import EmailMessage

    # Create a new EmailMessage object
    msg = EmailMessage()

    # Set the sender, recipients, and subject of the email
    msg['From'] = 'tradechain4@gmail.com'
    msg['To'] = EMAIL
    msg['Subject'] = 'Tradechain Password'

    # Set the body of the email
    msg.set_content("This is your password:" + str(password))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        # Start the TLS encryption
        smtp.starttls()

        # Log in to your email account
        smtp.login('tradechain4@gmail.com', 'barulvmjpehkynls')

        # Send the email
        smtp.send_message(msg)


    return '''<script>alert('sucessfully registered');window.location='/'</script>'''



@app.route('/view_profile')
def view_profile():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM company WHERE `l_id`='"+str(session['lid'])+"'"
        res = db.selectOne(qry)
        return render_template("company/view_profile.html", data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/edit_profile')
def edit_profile():
    if session['lid'] != '':
        db=Db()
        qry="SELECT * FROM `company` WHERE `l_id`='"+str(session['lid'])+"'"
        res=db.selectOne(qry)
        return render_template("company/edit_Profile.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/edit_profile_post',methods=['post'])
def edit_profile_post():
    if session['lid'] != '':
        COMPANY_NAME = request.form['textfield']
        TAX_ID = request.form['textfield3']
        LEGAL_STATUS = request.form['textfield6']
        FIELD_OF_BUSINESS = request.form['textfield7']
        REGISTERED_OFFICE = request.form['textfield8']
        STATE = request.form['textfield4']
        REGION = request.form['textfield5']
        MUNCIPALITY = request.form['textfield9']
        POSTAL_CODE = request.form['textfield10']
        STREET = request.form['textfield11']
        NUMBER = request.form['textfield12']
        EMAIL = request.form['textfield13']
        TELEPHONE = request.form['textfield14']
        FAX = request.form['textfield15']
        POSTAL_ADDRESS = request.form['textfield16']
        LOGO = request.files['fileField']
        from  datetime import datetime
        dt=datetime.now().strftime("%Y%m%d-%H%M%S")
        LOGO.save("C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\LOGO\\"+ dt +".jpg")
        path="/static/company/LOGO/"+dt+".jpg"
        CITY = request.form['textfield19']
        COUNTRY = request.form['textfield20']
        BANK = request.form['textfield21']
        ACCOUNT_NUMBER = request.form['textfield22']
        IFSC = request.form['textfield23']
        TITLE = request.form['textfield24']
        NAME = request.form['textfield26']
        SURNAME = request.form['textfield27']
        DOB = request.form['textfield25']
        TITLE = request.form['textfield28']
        NAME = request.form['textfield29']
        SURNAME = request.form['textfield29']
        DOB = request.form['textfield29']
        TITLE = request.form['textfield29']
        NAME = request.form['textfield29']
        SURNAME = request.form['textfield29']
        DOB = request.form['textfield29']
        PROOF_OF_FINANCIAL_ELIGIBILITY = request.files['fileField']
        from  datetime import datetime
        dt = datetime.now().strftime("%Y%m%d-%H%M%S")
        PROOF_OF_FINANCIAL_ELIGIBILITY.save("C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\PROOF\\" + dt + ".jpg")
        path1 = "/static/company/PROOF/" + dt + ".jpg"
        BANK_GUARANTEE = request.files['fileField2']
        from  datetime import datetime
        dt = datetime.now().strftime("%Y%m%d-%H%M%S")
        BANK_GUARANTEE.save("C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\BANK_PROOF\\" + dt + ".jpg")
        path2 = "/static/company/BANK_PROOF/" + dt + ".jpg"
        checkbox = request.form['textfield4']
        db = Db()
        qry = "UPDATE `company` SET `logo`='"+path+"',`c_name`='"+COMPANY_NAME+"',`tax_id`='"+TAX_ID+"',`legal_status`='"+LEGAL_STATUS+"',`field_of_business`='"+FIELD_OF_BUSINESS+"',`registered_office`='"+REGISTERED_OFFICE+"',`state`='"+STATE+"',`region`='"+REGION+"',`muncipality`='"+MUNCIPALITY+"',`postcode`='"+POSTAL_CODE+"',`street`='"+STREET+"',`email`='"+EMAIL+"',`fax`='"+FAX+"',`postal_address`='"+POSTAL_ADDRESS+"',`city`='"+CITY+"',`country`='"+COUNTRY+"',`bank_name`='"+BANK+"',`bank_number`='"+ACCOUNT_NUMBER+"',`ifsc_code`='"+IFSC+"',`director_name`='"+NAME+"',`director_title`='"+TITLE+"',`director_surname`='"+SURNAME+"',`director_dob`='"+DOB+"',`bankguarantee`='"+path2+"',`proof_of_financialeligibility`='"+path1+"' WHERE `l_id`='"+str(session['lid'])+"' "
        res = db.update(qry)
        return '''<script>alert('Sucessfully changed');window.location='/'</script>'''
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/view_orders')
def view_orders():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM `orders` "
        res = db.select(qry)
        return render_template("company/view_orders.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/view_trader')
def view_trader():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM trader"
        res = db.select(qry)
        return render_template("company/view_trader.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/c_home')
def c_home():
    if session['lid'] != '':
        return render_template("company/c_home.html")
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''
# ========================================== TRADER=====================================================================#


@app.route('/and_login', methods=['POST'])
def and_login():
    db=Db()
    username=request.form['username']
    password=request.form['password']
    qry = "SELECT * FROM login WHERE `user_name`='" + username + "' AND `password`='" + password + "'"
    res = db.selectOne(qry)
    if res is not None:
        qry2="SELECT * FROM `trader` WHERE l_id='"+str(res['login_id'])+"'"
        res2=db.selectOne(qry2)
        return jsonify(status="ok",type=res['type'],lid=res['login_id'],name=res2['user_name'],email=res2['email'],photo=res2['photo'])
    else:
        return jsonify(status="not ok")



@app.route('/signup_t1',methods=['post'])
def signup_t1():
    EMAIL = request.form['EMAIL']
    db=Db()
    qry = "SELECT * FROM login WHERE `user_name`='" + EMAIL + "' "
    res = db.selectOne(qry)
    if res is None:



        import random
        v=random.randint(000000,999999)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("investunlisted000@gmail.com","wypygvjwttrtpiyv")

        subject = "verification mail"
        body = "your OTP/verification code is "+str(v)
        msg = "subject: "+subject+"\n\n"+body
        server.sendmail("investunlisted000@gmail.com",EMAIL,msg)
        server.quit()

        return jsonify(status="ok",otp=str(v))
    else:
        return jsonify(status="not ok")

@app.route('/signup_t1_post',methods=['post'])
def signup_t1_post():
    OTP=request.form['textfield2']
    db=Db()
    qry=""
    return "ok"


@app.route('/signup_t2_post',methods=['post'])
def signup_t2_post():
    DOB=request.form['textfield2']
    WHAT_IS_YOUR_GENDER=request.form['select2']
    MARITAL_STATUS=request.form['select2']
    WHAT_IS_YOUR_ANNUAL_INCOME=request.form['select2']
    WHAT_IS_YOUR_OCCUPATION=request.form['select']
    SELECT_YOUR_COUNTRY=request.form['select2']
    DECLARATION=request.form['checkbox']
    db=Db()
    qry="INSERT INTO `trader`(dob`,`gender`,`marital_status`,`annual_income`,`occuppation`,`country`) VALUES ('"+DOB+"','"+WHAT_IS_YOUR_GENDER+"','"+MARITAL_STATUS+"','"+WHAT_IS_YOUR_ANNUAL_INCOME+"','"+WHAT_IS_YOUR_OCCUPATION+"','"+SELECT_YOUR_COUNTRY+"')"
    res=db.insert(qry)
    return '''<script>alert('sucessfull');window.location='/signup_t3'</script>'''

@app.route('/signup_t3')
def signup_t3():
    return render_template("trader/Signup_t3.html")

@app.route('/signup_t3_post',methods=['post'])
def signup_t3_post():



    Account_Holder_Name=request.form['accountname']
    IFSC_CODE=request.form['ifsc']
    BANK_ACCOUNT_NUMBER=request.form['accountnumber']
    ACCOUNT_TYPE=request.form['accounttype']

    DOB = request.form['vdob']
    WHAT_IS_YOUR_GENDER = request.form['vgender']
    MARITAL_STATUS = request.form['vmaritalstatus']
    WHAT_IS_YOUR_ANNUAL_INCOME = request.form['vannualincome']
    WHAT_IS_YOUR_OCCUPATION = request.form['voccupation']
    SELECT_YOUR_COUNTRY = request.form['vcountry']

    EMAIL = request.form['vemail']
    password=request.form['vpassword']
    ivuploaddocs=request.form['ivuploaddocs']
    import base64
    from datetime import datetime
    ss=base64.b64decode(ivuploaddocs)
    xx=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    with open(r"C:\Users\sabar\PycharmProjects\Investment\static\trader\proof\\"+xx,'wb') as fs:
        fs.write(ss)
    path="/static/trader/proof/"+xx
    db = Db()

    qrylogin="INSERT INTO `login`(`user_name`,`password`,`type`) VALUES('"+EMAIL+"','"+password+"','trader')"
    res1=db.insert(qrylogin)

    qry = "INSERT INTO`trader`(`l_id`,`user_name`,`dob`,`email`,`gender`,`marital_status`,`annual_income`,`occuppation`,`country`,`accountholder_name`,`ifsc_code`,`account_number`,`account_type`,`photo`,`location`) VALUES ('"+str(res1)+"','"+Account_Holder_Name+"','"+DOB+"','"+EMAIL+"','"+WHAT_IS_YOUR_GENDER+"','"+MARITAL_STATUS+"','"+WHAT_IS_YOUR_ANNUAL_INCOME+"','"+WHAT_IS_YOUR_OCCUPATION+"','"+SELECT_YOUR_COUNTRY+"','"+Account_Holder_Name+"','"+IFSC_CODE+"','"+BANK_ACCOUNT_NUMBER+"','"+ACCOUNT_TYPE+"','"+path+"','"+SELECT_YOUR_COUNTRY+"')"
    res=db.insert(qry)
    return jsonify(status="ok")



@app.route('/changepassword_post',methods=['post'])
def changepassword_post():
    currentpassword=request.form['currentpassword']
    newpassword=request.form['newpassword']
    confirmpassword=request.form['confirmpassword']
    lid=request.form['lid']
    db=Db()
    db = Db()
    qry = "SELECT * FROM login WHERE `password`='" + currentpassword + "' AND `login_id`='" + lid + "'"
    res = db.selectOne(qry)
    if newpassword == confirmpassword:
        db = Db()
        qry = "UPDATE login SET `password`='" + confirmpassword + "' WHERE `login_id`='" + lid + "'"
        res = db.update(qry)
        return jsonify(status="ok")
    else:
        return jsonify(status="not ok")


@app.route('/and_viewprofile', methods=['POST'])
def and_viewprofile():
    db = Db()
    lid=request.form['lid']
    qry = "SELECT * FROM `trader`WHERE `l_id`='"+lid+"'"
    res = db.selectOne(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_sentcomplaint', methods=['POST'])
def and_sentcomplaint():
    sentcomplaint=request.form['complaint']
    lid = request.form['lid']
    db = Db()
    qry = "INSERT INTO`complaint`(`date`,`user_id`,`complaint`,`reply`,`status`) VALUES (CURDATE(),'"+lid+"','"+sentcomplaint+"','pending','pending')"
    res = db.insert(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_viewreply', methods=['POST'])
def and_viewreply():
    db = Db()
    lid=request.form['lid']
    qry = "SELECT * FROM`complaint`WHERE `user_id`='"+lid+"'"
    res = db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_newsfeed', methods=['POST'])
def and_newsfeed():
    db = Db()
    qry = "SELECT * FROM `newsfeed`"
    res = db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_portifolio', methods=['POST'])
def and_portifolio():
    db = Db()
    qry = "SELECT * FROM `portifolio`"
    res = db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/and_feedback', methods=['POST'])
def and_feedbacl():
    feedback=request.form['feedback']
    rating=request.form['rating']
    lid = request.form['lid']
    db = Db()
    qry = "INSERT INTO`feedback`(`user_id`,`date`,`feedback`,`rating`) VALUES ('"+lid+"',CURDATE(),'"+feedback+"','"+rating+"')"
    res = db.insert(qry)
    return jsonify(status="ok")




@app.route('/and_watchlist', methods=['POST'])
def and_watchlist():
    db = Db()
    lid=request.form['lid']
    qry = "SELECT * FROM`watchlist` INNER JOIN `company` ON `watchlist`.`c_id`=`company`.`l_id`"
    res = db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/and_delete_watchlist', methods=['POST'])
def and_delete_watchlist():
    db = Db()
    wid=request.form['wid']
    qry = "DELETE FROM `watchlist` WHERE `watch_id`='"+wid+"'"
    res = db.delete(qry)
    return jsonify(status="ok")




@app.route('/and_add_watchlist', methods=['POST'])
def and_add_watchlist():
    lid=request.form['lid']
    cid=request.form['cid']
    print(cid,"ooooooooooooooo")
    qry2="SELECT * FROM `watchlist` WHERE `c_id`='"+cid+"' AND `uid`='"+lid+"'"
    db=Db()
    res=db.selectOne(qry2)
    if res is None:
        qry="INSERT INTO `watchlist` (`c_id`,`uid`) VALUES('"+cid+"','"+lid+"')"
        db=Db()
        db.insert(qry)
        return jsonify(status="ok")
    else:
        return jsonify(status="no")









@app.route('/and_update_profile', methods=['POST'])
def and_update_profile():

    holdername=request.form['accountholdername']
    ifsc=request.form['ifsc']
    accnumber=request.form['accountnumber']
    dob = request.form['dob']
    phonenumber = request.form['phonenumber']
    m_status = request.form['m_status']
    annualincome = request.form['annualincome']
    occupation = request.form['occupation']
    country = request.form['country']
    gender = request.form['gender']
    lid=request.form['lid']
    qry="UPDATE `trader` SET `accountholder_name`='"+holdername+"',`ifsc_code`='"+ifsc+"',`account_number`='"+accnumber+"',`dob`='"+dob+"',`contact`='"+phonenumber+"',`marital_status`='"+m_status+"',`annual_income`='"+annualincome+"',`occuppation`='"+occupation+"',`country`='"+country+"',`gender`='"+gender+"' WHERE `l_id`='"+lid+"'"
    db = Db()
    res=db.update(qry)

    return jsonify(status="ok")





#================================Blockchain======================================================




def checkbalance(amount,accountnumber,privatekey,toaccount):
    from web3 import Web3, HTTPProvider
    blockchain_address = "http://127.0.0.1:7545"
    web3 = Web3(HTTPProvider(blockchain_address))
    if web3.isConnected():
        acc1 = accountnumber
        acc2 = toaccount

        prvkey = privatekey
        nonce = web3.eth.getTransactionCount(acc1)

        abcd = web3.eth.get_balance(acc1)
        abcd = web3.fromWei(abcd, 'ether')
        print(abcd)

        tx = {
            'nonce': nonce,
            'to': acc2,
            'value': web3.toWei(int(amount), 'ether'),
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei')
        }
        signedtx = web3.eth.account.sign_transaction(tx, prvkey)
        hashx = web3.eth.send_raw_transaction(signedtx.rawTransaction)
        print(web3.toHex(hashx))


@app.route('/addamountpost',methods=["post"])
def addamountpost():
    account = request.form['account']
    key = request.form['key']
    amounts = request.form['amounts']
    cid = request.form['cid']
    lid = request.form['lid']
    db = Db()
    qry = "SELECT * FROM `account_details` WHERE `acc_no`='" + account + "' AND `pvt_key`='" + key + "' and lid='"+lid+"'"
    res = db.selectOne(qry)
    if res is not None:
        qry1="SELECT * FROM `account_details` WHERE lid='"+str(cid)+"'"
        db=Db()
        ress=db.selectOne(qry1)
        if ress is not None:
            toaccount=ress['acc_no']
            checkbalance(amounts, account, key,toaccount)
            with open(compiled_contract_path) as file:
                contract_json = json.load(file)  # load contract info as JSON
                contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
                print(contract_abi)
            contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
            blocknumber = web3.eth.get_block_number()
            print(blocknumber)



            from datetime import datetime
            date = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
            # message2 = contract.functions.addTransaction(blocknumber + 1, policyid, userid, amount, date).transact()
            message2 = contract.functions.addTransaction(int(blocknumber + 1),int(cid), int(lid), int(amounts), date).transact()
            print(message2)
            return jsonify(status='ok')
        else:
            return jsonify(status='no')
    else:
        return jsonify(status='no')





@app.route("/mytrans",methods=['post'])
def mytrans():
    lid=request.form['lid']
    print(lid)
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)
    lq=[]
    for i in range(blocknumber,4, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        try:
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input)

            lq.append(decoded_input[1])
        except Exception as a:
            print(a)
            pass

    print(lq,"lq")
    tot=0
    ls=[]
    for i in lq:
        try:
            print(i["investmentida"])
            if int(i["userida"])==int(lid):
                # ls.append(i)
                print(i['userida'],"aaaaaaaaaaaaaaaaa")

                qry="SELECT * FROM `company` WHERE `l_id`='"+str(i['companyida'])+"'"
                db=Db()
                res=db.selectOne(qry)
                if res is not None:
                    a={'amounta':i['amounta'],'userida':i['userida'],'investmentida':i['investmentida'],'datea':i['datea'],'companyida':i['companyida'],'c_name':res['c_name']}
                    ls.append(a)
                tot+=i["amounta"]
        except Exception as e:
            pass
    return jsonify(status='ok',data=ls,total=tot)





@app.route("/alltrans")
def alltrans():
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)
    lq=[]
    for i in range(blocknumber,4, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        try:
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input)
            print("ku")
            print(decoded_input)
            lq.append(decoded_input[1])
        except Exception as a:
            pass

    print(lq)
    tot=0
    ls=[]
    for i in lq:
        print(i["policyida"])
        if i["userida"]==int(session['lid']):
            # ls.append(i)
            print(i['userida'],"aaaaaaaaaaaaaaaaa")

            qry="SELECT * FROM `crowdfunding_request` WHERE `ReqNo`='"+str(i['policyida'])+"'"
            db=Db()
            res=db.selectOne(qry)
            if res is not None:
                a={'amounta':i['amounta'],'userida':i['userida'],'policyida':i['policyida'],'amounta':i['amounta'],'datea':i['datea'],'Buisness Name':res['Buisness Name'],'Address':res['Address'],'City':res['City'],'Email':res['Email'],'Website':res['Website'],'Phone':res['Phone'],'Description':res['Description']}
                ls.append(a)
            tot+=i["amounta"]
    return jsonify(stayus='ok',data=ls,total=tot)









@app.route("/company_view_transaction")
def company_view_transaction():
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)
    lq=[]
    for i in range(blocknumber,4, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        try:
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input)
            print("ku")
            print(decoded_input)
            lq.append(decoded_input[1])
        except Exception as a:
            pass

    print(lq)
    tot=0
    ls=[]
    for i in lq:
        try:

            print(i["investmentida"])
            if i["companyida"]==int(session['lid']):
                # ls.append(i)
                print(i['userida'],"aaaaaaaaaaaaaaaaa")

                qry="SELECT * FROM `trader` WHERE l_id='"+str(i['userida'])+"'"
                db=Db()
                res=db.selectOne(qry)
                if res is not None:
                    a={'amounta':i['amounta'],'userida':i['userida'],'investmentida':i['investmentida'],'datea':i['datea'],'user_name':res['user_name'],'email':res['email']}
                    ls.append(a)
                tot+=i["amounta"]
        except Exception as e:
            pass
    print(ls)
    return render_template("company/view_orders.html",data=ls,tot=tot)






def netshares(cid):
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)
    lq=[]
    for i in range(blocknumber,4, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        try:
            decoded_input = contract.decode_function_input(a['input'])

            lq.append(decoded_input[1])
        except Exception as a:
            pass

    tot=0
    ls=[]
    for i in lq:
        try:
            if int(i["companyida"])==int(cid):
                tot+=i["amounta"]

        except Exception as e:
            pass
    return tot










@app.route('/and_view_availablecompanies', methods=['POST'])
def and_view_availablecompanies():
    db = Db()
    qry = "SELECT * FROM `company`"
    res = db.select(qry)
    l=[]
    for i in res:
        nets=netshares(i['l_id'])
        print(nets,"sharessss")
        l.append({'C_id':i['C_id'],'base_price':i['base_price'],'c_graph':i['c_graph'],'logo':i['logo'],'c_name':i['c_name'],'tax_id':i['tax_id'],'legal_status':i['legal_status'],'field_of_business':i['field_of_business'],'registered_office':i['registered_office'],'state':i['state'],'region':i['region'],'muncipality':i['muncipality'],'postcode':i['postcode'],'street':i['street'],'phone_number':i['phone_number'],'email':i['email'],'telephone':i['telephone'],'fax':i['fax'],'postal_address':i['postal_address'],'city':i['city'],'country':i['country'],'bank_name':i['bank_name'],'bank_number':i['bank_number'],'ifsc_code':i['ifsc_code'],'director_name':i['director_name'],'director_surname':i['director_surname'],'director_dob':i['director_dob'],'bankguarantee':i['bankguarantee'],'proof_of_financialeligibility':i['proof_of_financialeligibility'],'status':i['status'],'l_id':i['l_id'],'netshares':nets})
    return jsonify(status="ok",data=l)












@app.route("/history",methods=['post'])
def history():
    clid=request.form['clid']
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)
    lq=[]
    for i in range(blocknumber,4, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        try:
            decoded_input = contract.decode_function_input(a['input'])

            lq.append(decoded_input[1])
        except Exception as a:
            pass

    ls=[]
    for i in lq:
        try:

            if int(i["companyida"])==int(clid):
                a={'amt':i['amounta'],'date':i['datea']}
                ls.append(a)
        except Exception as e:
            pass
    print(ls)
    return jsonify(status="ok", data=ls)






@app.route('/and_forgot_password', methods=['POST'])
def and_forgot_password():

    email=request.form['email']

    qry="SELECT * FROM `login` WHERE `user_name`='"+email+"'"
    db=Db()
    res=db.selectOne(qry)

    import smtplib
    from email.message import EmailMessage

    # Create a new EmailMessage object
    msg = EmailMessage()

    # Set the sender, recipients, and subject of the email
    msg['From'] = 'tradechain4@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'Tradechain Password'

    # Set the body of the email
    msg.set_content("This is your password:"+str(res['password']))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        # Start the TLS encryption
        smtp.starttls()

        # Log in to your email account
        smtp.login('tradechain4@gmail.com', 'barulvmjpehkynls')

        # Send the email
        smtp.send_message(msg)

    return jsonify(status="ok")






@app.route('/forgotpassword')
def forgotpassword():
    return render_template("forgot_index.html")








@app.route('/forgot_password_post', methods=['POST'])
def forgot_password_post():

    email=request.form['textfield']

    qry="SELECT * FROM `login` WHERE `user_name`='"+email+"'"
    db=Db()
    res=db.selectOne(qry)

    import smtplib
    from email.message import EmailMessage

    # Create a new EmailMessage object
    msg = EmailMessage()

    # Set the sender, recipients, and subject of the email
    msg['From'] = 'tradechain4@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'Tradechain Password'

    # Set the body of the email
    msg.set_content("This is your password:"+str(res['password']))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        # Start the TLS encryption
        smtp.starttls()

        # Log in to your email account
        smtp.login('tradechain4@gmail.com', 'barulvmjpehkynls')

        # Send the email
        smtp.send_message(msg)

    return "<script>alert('password sent to your registered email address');window.location='/'</script>"












if __name__ == '__main__':
    app.run(debug=True,port=4000,host='0.0.0.0')
