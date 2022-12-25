from flask import Flask, render_template, redirect, url_for, request
import nltk

skills_app = Flask(__name__)

my_skills = [("Html", 80), ("CSS", 75), ("Python", 90), ("Eyad", 40)]
answerList=[]

@skills_app.route('/success')
def success():
    return render_template("skills.html", pagetitle="My Skills",
                                       page_head="Here is the Similarity",
                                       description="This is the similarity between each document in the database with your selected document",
                                       AnswerList=answerList,
                                       custom_css="skills")


@skills_app.route('/login', methods=['POST', 'GET'])
def login():
    global answerList
    if request.method == 'POST':
        user = request.form['nm1'].lower()

        mn = 1.0
        answer = "null"
        select = request.form['Palag']

        answerList.clear()
        for x in range(1000):
            st = str(x)
            if len(st) < 3:
                st = "0" + st
            if len(st) < 3:
                st = "0" + st
            fd = open("PineTools.com_files/shek.txt." + st, "r")
            user2 = fd.read().lower()
            file = "file" + str(x)

            if select == 'Jaccard':
                tokens1 = nltk.word_tokenize(user)
                tokens2 = nltk.word_tokenize(user2)
                ng1_chars = set(nltk.ngrams(tokens1, n=3))
                ng2_chars = set(nltk.ngrams(tokens2, n=3))
                jd_sent_1_2 = nltk.jaccard_distance(ng1_chars, ng2_chars)
                answerList.append(tuple(((1-jd_sent_1_2)*100,user2)))

                if jd_sent_1_2 < mn:
                    mn = jd_sent_1_2
                    answer = user2

            else:

                tokens1 = nltk.word_tokenize(user)
                tokens2 = nltk.word_tokenize(user2)
                ed_sent_1_2 = nltk.edit_distance(tokens1, tokens2)
                answerList.append(tuple(((100-ed_sent_1_2),user2)))
                if ed_sent_1_2 < mn:
                    mn = ed_sent_1_2
                    answer = user2


        answerList = sorted(answerList,key=lambda x:x[0],reverse=True)
        return redirect(url_for('success'))

    else:
        user = request.args.get('nm1')
        user2 = request.args.get('nm2')

        return redirect(url_for('success', name2=user + user2))

@skills_app.route("/")
def add():
    return render_template("add.html",
                            pagetitle= "Add",
                            custom_css="add")

@skills_app.route("/log")
def homepage():
    return render_template("login.html",
                           pagetitle="Homepage",
                           custom_css="home")

@skills_app.route("/explain")
def explain():
    return render_template("explain.html",
                           pagetitle="Explain",
                           custom_css="explain")


@skills_app.route("/about")
def about():
    return render_template("about.html",
                           pagetitle="About us",
                           custom_css="about")



# @skills_app.route("/skills")
# def skills():
#     return render_template("skills.html" , pagetitle= "My Skills",
#                             page_head="My Skills",
#                             description="This is my skills page",
#                             skills=my_skills,
#                             custom_css="skills")

if __name__ == "__main__":
    skills_app.run(debug=True)
