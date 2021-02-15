from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import EditUserProfileForm
from .models import mark
from array import *
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout,models
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
dict={}
# Create your views here.
increment_ten_math=0
count_ten_math=0;
question_count_ten_math=0
d_ten_math=0
selected_answer_list_ten_math=[]

subject=""
increment_ten_english=0
count_ten_english=0;
question_count_ten_english=0
d_ten_english=0
selected_answer_list_ten_english=[]

increment_ten_physics=0
count_ten_physics=0;
question_count_ten_physics=0
d_ten_physics=0
selected_answer_list_ten_physics=[]

increment_ten_chemistry=0
count_ten_chemistry=0;
question_count_ten_chemistry=0
d_ten_chemistry=0
selected_answer_list_ten_chemistry=[]

increment_ten_biology=0
count_ten_biology=0;
question_count_ten_biology=0
d_ten_biology=0
selected_answer_list_ten_biology=[]

list1=[]
table_count_variable=0

increment_ten_social=0
count_ten_social=0;
question_count_ten_social=0
d_ten_social=0
selected_answer_list_ten_social=[]
answer_list_ten_math=['Denis-Ritchi','Sundar-pichai','Subhman-Gill','Ben-stokes','Nitish-Rana','India','Peris','Chaina','Warrior','Chaina','Russia']
answer_list_ten_english=['Actor','Sunil-Dutt','Ashraf','Singer','Sahrukh-Khan','Shasank-Redumption','Brad-Pit','Sachin-Tendulkar','England','Chaina','Aaron-Finch']
answer_list_ten_chemistry=['Ca(OH)2','Baking-Soda','Vinegar','Gylcerol','Simple-Esters','PbSO4','Combination','Iron','Cu-Sn','Iron','Colourless']
answer_list_ten_physics=['9.8m/s^2','E=mc^2','F=ma','3','Infinity','Virtual-and-Errect','-0.25m','Diopter','10cm','Diamond','Optically-denser']
answer_list_ten_biology=['Absorbing-Lights','Amino-Acid','Starch','Plasma','Gymnosperms','Nephrons','Transport-of-Water','Respiration','6.5m','Fallopian-Tubule','Proteins']
answer_list_ten_social=['Carbonary','1920','Kolkata','Bible','Mahatma-Gandhi','Middle-Class','Z-Gudy','Goa','RBI','All','All']
@login_required(login_url='/exam/login/')
def showTest(request):
    subject=request.GET['subject']
    request.session['sub']=subject
    if request.session['number']=="10" and subject=="math":
        question_list_ten_math=['Who developed c Language?','Who is father of java?','Who  am  I?','What is your name?','In which class do you read?','Where the Taj Mahal is Situated?',
        'Where is Eifel Tower?','Which country below has the Largest Wall?','Sikander is a?','Which country has largets population?','Which country has Largest Area?']
        option_list_ten_math=['Kane-Thompsan','Denis-Ritchi','Salman-Khan','Aamir-khan','Abraham-lincoln','Sunder-pichai','Sachin-Tendulkar','Mark-Zukerberg',
        'Virat-Kohli','Ms-Dhoni','Subhman-Gill','Ishan-Kishan','Andre-Russell','Rohit-Sharma','Ben-stokes','Jos-Buttler','Eion-Morgan',
        'Nitish-Rana','Jasprit-Bumrah','David-Warner','India','Pakistan','Dubai','Saudi','Newziland','Austrailia','Srilanka','Peris','Hongkong','North-Korea','Chaina','Japan','Cricketer','Receler','Warrior','Footboller','Chaina','India','Japan','Africa','Turkey','Russia','Instambol','Portugal']
        answer_list_ten_math=['Denis-Ritchi','Sundar-pichai','Subhman-Gill','Ben-stokes','Nitish-Rana','India','Peris','Chaina','Warrior','Chaina','Russia']
        global count_ten_math
        global d_ten_math
        global increment_ten_math
        global question_count_ten_math
        if question_count_ten_math==0:
           question_count_ten_math=question_count_ten_math+1
        if request.method=='POST':
            if 'answer' in request.POST:
                ans=request.POST["answer"]
                selected_answer_list_ten_math.append(ans)
                count_ten_math=count_ten_math+1
                increment_ten_math=increment_ten_math+3
                question_count_ten_math=question_count_ten_math+1
                if count_ten_math==len(question_list_ten_math):
                    count_ten_math=0;
                    increment_ten_math=0;
                    question_count_ten_math=0
                    d_ten_math=0
                    list1=[]
                    return HttpResponseRedirect('/exam/complete/')
                que=question_list_ten_math[count_ten_math]
                a=option_list_ten_math[count_ten_math+increment_ten_math+0]
                b=option_list_ten_math[count_ten_math+increment_ten_math+1]
                c=option_list_ten_math[count_ten_math+increment_ten_math+2]
                d=option_list_ten_math[count_ten_math+increment_ten_math+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'ans':ans,'count':question_count_ten_math,'Rem':len(question_list_ten_math)-count_ten_math-1}
                return render(request,'exam/test.html',data)
            else:
                que=question_list_ten_math[count_ten_math]
                a=option_list_ten_math[count_ten_math+increment_ten_math+0]
                b=option_list_ten_math[count_ten_math+increment_ten_math+1]
                c=option_list_ten_math[count_ten_math+increment_ten_math+2]
                d=option_list_ten_math[count_ten_math+increment_ten_math+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_math,'Rem':len(question_list_ten_math)-count_ten_math-1}
                res=render(request,'exam/test.html',data)
                return res

        else:
            que=question_list_ten_math[count_ten_math]
            a=option_list_ten_math[count_ten_math+increment_ten_math+0]
            b=option_list_ten_math[count_ten_math+increment_ten_math+1]
            c=option_list_ten_math[count_ten_math+increment_ten_math+2]
            d=option_list_ten_math[count_ten_math+increment_ten_math+3]
            level="Easy"
            data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_math,'Rem':len(question_list_ten_math)-count_ten_math-1}
            res=render(request,'exam/test.html',data)
            return res

    elif request.session['number']=="10" and subject=="english":
        question_list_ten_english=['Salman khan is a?','Who is father of Sanjay Dutt?','Who  am  I?','Who is Udit Narayan?','The Actor of Veer-zara?','Heighest IMDB rating movie of all time?',
        'The Actor of Inglorious Basterds?','Heighest century in ODIs by a player?','Heighest Individual score in ODI by a team?','Which country has largets population?','Heighest T20 Individual Score by a player?']
        option_list_ten_english=['Actor','Cricketer','Footballer','Swimer','Sunil-Dutt','Mukesh-Khanna','Amresh-Puri','Kishore-Kumar',
        'Ashraf','Alam','Sahil','Hero','Rapper','Singer','Dancer','Musician',
        'Sahrukh-Khan','Salman-Khan','Aamir-Khan','Sanjay-Dutt','Pulp-Fiction','Shasank-Redumption','Dangal','Pk','Brad-Pit','John-Cena','Rock','Under-Tacker','Virat-Kohli','Ricky-Ponting','Sachin-Tendulkar','Kumar-Sangakara','South-Africa','India','England','Austrailia','India','Chaina','Jermany','England','Aaron-Finch','Subhmann-Gill','B-Maccolam','Chris-Gayle']
        answer_list_ten_english=['Actor','Sunil-Dutt','Ashraf','Singer','Sahrukh-Khan','Shasank-Redumption','Brad-Pit','Sachin-Tendulkar','England','Chaina','Aaron-Finch']
        global count_ten_english
        global d_ten_english
        global increment_ten_english
        global question_count_ten_english
        if question_count_ten_english==0:
              question_count_ten_english=question_count_ten_english+1
        if request.method=='POST':
            if 'answer' in request.POST:
                ans=request.POST["answer"]
                selected_answer_list_ten_english.append(ans)
                count_ten_english=count_ten_english+1
                increment_ten_english=increment_ten_english+3
                question_count_ten_english=question_count_ten_english+1
                if count_ten_english==len(question_list_ten_english):
                    count_ten_english=0;
                    increment_ten_english=0;
                    question_count_ten_english=0
                    d_ten_english=0
                    list1=[]
                    return HttpResponseRedirect('/exam/complete/')
                que=question_list_ten_english[count_ten_english]
                a=option_list_ten_english[count_ten_english+increment_ten_english+0]
                b=option_list_ten_english[count_ten_english+increment_ten_english+1]
                c=option_list_ten_english[count_ten_english+increment_ten_english+2]
                d=option_list_ten_english[count_ten_english+increment_ten_english+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'ans':ans,'count':question_count_ten_english,'Rem':len(question_list_ten_english)-count_ten_english-1}
                return render(request,'exam/test.html',data)
            else:
                que=question_list_ten_english[count_ten_english]
                a=option_list_ten_english[count_ten_english+increment_ten_english+0]
                b=option_list_ten_english[count_ten_english+increment_ten_english+1]
                c=option_list_ten_english[count_ten_english+increment_ten_english+2]
                d=option_list_ten_english[count_ten_english+increment_ten_english+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_english,'Rem':len(question_list_ten_english)-count_ten_english-1}
                res=render(request,'exam/test.html',data)
                return res

        else:
            que=question_list_ten_english[count_ten_english]
            a=option_list_ten_english[count_ten_english+increment_ten_english+0]
            b=option_list_ten_english[count_ten_english+increment_ten_english+1]
            c=option_list_ten_english[count_ten_english+increment_ten_english+2]
            d=option_list_ten_english[count_ten_english+increment_ten_english+3]
            level="Easy"
            data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_english,'Rem':len(question_list_ten_english)-count_ten_english-1}
            res=render(request,'exam/test.html',data)
            return res

    elif request.session['number']=="10" and subject=="physics":
        question_list_ten_physics=['What is the value of g?','What is the theory of relativity?','Whta is the formula of Force?','How many Laws of Newtons?','Focal Length of plane mirror is?','Image Formed by plane mirror is?',
        'If Power of the Lens is -40,its focal length is?','The unit of power of lense is?','The Radius of curvature of a length is 20cm then its focal length is?','Which element has the maximum refrective index?','In optics an object which has heigher refrective index is called?']
        option_list_ten_physics=['10m/s^2','9.88m/s^2','9.8m/s^2','8m/s^2','E=mv^2','E=mc^2','E=mc','E=m^2c^2',
        'F=mv','F=mc','F=ma','F=mv^2','4','3','2','1',
        'Infinity','Zero','Negative','None','Real-and-Errect','Real-and-Inverted','Virtual-and-Errect','Virtual-and-Inverted','4m','-40m','-0.25m','-25m','Meter','Centimeter','Diopter','1/M','20cm','10cm','40cm','30cm','Ruby','Diamond','Glass','Water','Optically-rarer','Optically-denser','Optical-density','Refrective-Index']
        answer_list_ten_physics=['9.8m/s^2','E=mc^2','F=ma','3','Infinity','Virtual-and-Errect','-0.25m','Diopter','10cm','Diamond','Optically-denser']
        global count_ten_physics
        global d_ten_physics
        global increment_ten_physics
        global question_count_ten_physics
        if question_count_ten_physics==0:
              question_count_ten_physics=question_count_ten_physics+1
        if request.method=='POST':
            if 'answer' in request.POST:
                ans=request.POST["answer"]
                selected_answer_list_ten_physics.append(ans)
                count_ten_physics=count_ten_physics+1
                increment_ten_physics=increment_ten_physics+3
                question_count_ten_physics=question_count_ten_physics+1
                if count_ten_physics==len(question_list_ten_physics):
                    count_ten_physics=0;
                    increment_ten_physics=0;
                    question_count_ten_physics=0
                    d_ten_physics=0
                    list1=[]
                    return HttpResponseRedirect('/exam/complete/')
                que=question_list_ten_physics[count_ten_physics]
                a=option_list_ten_physics[count_ten_physics+increment_ten_physics+0]
                b=option_list_ten_physics[count_ten_physics+increment_ten_physics+1]
                c=option_list_ten_physics[count_ten_physics+increment_ten_physics+2]
                d=option_list_ten_physics[count_ten_physics+increment_ten_physics+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'ans':ans,'count':question_count_ten_physics,'Rem':len(question_list_ten_physics)-count_ten_physics-1}
                return render(request,'exam/test.html',data)
            else:
                que=question_list_ten_physics[count_ten_physics]
                a=option_list_ten_physics[count_ten_physics+increment_ten_physics+0]
                b=option_list_ten_physics[count_ten_physics+increment_ten_physics+1]
                c=option_list_ten_physics[count_ten_physics+increment_ten_physics+2]
                d=option_list_ten_physics[count_ten_physics+increment_ten_physics+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_physics,'Rem':len(question_list_ten_physics)-count_ten_physics-1}
                res=render(request,'exam/test.html',data)
                return res

        else:
            que=question_list_ten_physics[count_ten_physics]
            a=option_list_ten_physics[count_ten_physics+increment_ten_physics+0]
            b=option_list_ten_physics[count_ten_physics+increment_ten_physics+1]
            c=option_list_ten_physics[count_ten_physics+increment_ten_physics+2]
            d=option_list_ten_physics[count_ten_physics+increment_ten_physics+3]
            level="Easy"
            data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_physics,'Rem':len(question_list_ten_physics)-count_ten_physics-1}
            res=render(request,'exam/test.html',data)
            return res

    elif request.session['number']=="10" and subject=="chemistry":
        question_list_ten_chemistry=['Lime Water is?',' Which one of the following will turn red litmus blue?','Which one of the following will turn blue litmus red?','The by product of soap is?','Soaps are formed by saponification of?','The chemical formula of lead sulphate is?',
        'The reaction of H2 gas with oxygen gas to form water is an example of?','The second most abundant metal in the earth’s crust is?',' The bronze medals are made up of?','Which of the following metals is present in the anode mud during the electrolytic refining of copper?','Both CO2 and H2 gases are?']
        option_list_ten_chemistry=['CaO','Ca(OH)2','CaCO3','CaCl2','Vinegar','Baking-Soda','Lemon-Juice','Washing-Soda',
        'Vinegar','Lime-Water','Baking-Soda','Washing-Soda','Isoprene','Gylcerol','Butene','Propane',
        'Alcohals','Glycosides','Simple-Esters','Carboylic-Acid','Pb2SO4','Pb(SO4)2','PbSO4',' Pb2(SO4)3','Combination','Redox-reaction','Exothermic-reaction','None','Oxygen','Silicon','Aluminium','Iron','Cu-Zn','Zn-Ni','Cu-Sn','Cu-Zn-Tn','Sodium','Aluminium''Gold','Iron','Acidic-in-nature','Heavier-than-air','Colourless','Soluble-in-water']
        answer_list_ten_chemistry=['Ca(OH)2','Baking-Soda','Vinegar','Gylcerol','Simple-Esters','PbSO4','Combination','Iron','Cu-Sn','Iron','Colourless']
        global count_ten_chemistry
        global d_ten_chemistry
        global increment_ten_chemistry
        global question_count_ten_chemistry
        if question_count_ten_chemistry==0:
              question_count_ten_chemistry=question_count_ten_chemistry+1
        if request.method=='POST':
            if 'answer' in request.POST:
                ans=request.POST["answer"]
                selected_answer_list_ten_chemistry.append(ans)
                count_ten_chemistry=count_ten_chemistry+1
                increment_ten_chemistry=increment_ten_chemistry+3
                question_count_ten_chemistry=question_count_ten_chemistry+1
                if count_ten_chemistry==len(question_list_ten_chemistry):
                    count_ten_chemistry=0;
                    increment_ten_chemistry=0;
                    question_count_ten_chemistry=0
                    d_ten_chemistry=0
                    list1=[]
                    return HttpResponseRedirect('/exam/complete/')
                que=question_list_ten_chemistry[count_ten_chemistry]
                a=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+0]
                b=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+1]
                c=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+2]
                d=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'ans':ans,'count':question_count_ten_chemistry,'Rem':len(question_list_ten_chemistry)-count_ten_chemistry-1}
                return render(request,'exam/test.html',data)
            else:
                que=question_list_ten_chemistry[count_ten_chemistry]
                a=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+0]
                b=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+1]
                c=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+2]
                d=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_chemistry,'Rem':len(question_list_ten_chemistry)-count_ten_chemistry-1}
                res=render(request,'exam/test.html',data)
                return res

        else:
            que=question_list_ten_chemistry[count_ten_chemistry]
            a=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+0]
            b=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+1]
            c=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+2]
            d=option_list_ten_chemistry[count_ten_chemistry+increment_ten_chemistry+3]
            level="Easy"
            data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_chemistry,'Rem':len(question_list_ten_chemistry)-count_ten_chemistry-1}
            res=render(request,'exam/test.html',data)
            return res

    elif request.session['number']=="10" and subject=="biology":
        question_list_ten_biology=['The chlorophyll in photosynthesis is used for?','Proteins after digestion are converted into?','Carbohydrates in the plants are stored in the form of?','Blood consist of what fluid medium??',' A plant that has seeds but no flowers and fruits?','The filtration units of kidney?',
        'The Xylem in plants are responsible for?','Which life process converts chemical energy into heat energy?','The Length of small intenstine in human adult?','The place of fertilization in humans is?','Chromosoms are the combination of DNA with?']
        option_list_ten_biology=['Absorbing-Lights','Reduction-of-CO2','Breaking-down-water-molecules','None','Carbohydrates','Small-Globals','Amino-Acid','Starch',
        'Glycogen','Starch','Glucose','Maltose','Lymph','Platelets','Plasma','All',
        'Bryophytes','Gymnosperms','Mosses','Pteridophytes','Ureter','Urethra','Nephrons','Neurons','Transport-of-Water','Transport-of-food','Transport-of-AminoAcid','Transport-of-oxygen','Nutrition','Respiration','Excertion','Transpiration','4.5m','3.5m','1.5m','6.5m','Fallopian-Tubule','Uterus','Vagina','Scrotum','RNA','Proteins','Fats','Fibers']
        answer_list_ten_biology=['Absorbing-Lights','Amino-Acid','Starch','Plasma','Gymnosperms','Nephrons','Transport-of-Water','Respiration','6.5m','Fallopian-Tubule','Proteins']
        global count_ten_biology
        global d_ten_biology
        global increment_ten_biology
        global question_count_ten_biology
        if question_count_ten_biology==0:
              question_count_ten_biology=question_count_ten_biology+1
        if request.method=='POST':
            if 'answer' in request.POST:
                ans=request.POST["answer"]
                selected_answer_list_ten_biology.append(ans)
                count_ten_biology=count_ten_biology+1
                increment_ten_biology=increment_ten_biology+3
                question_count_ten_biology=question_count_ten_biology+1
                if count_ten_biology==len(question_list_ten_biology):
                    count_ten_biology=0;
                    increment_ten_biology=0;
                    question_count_ten_biology=0
                    d_ten_biology=0
                    list1=[]
                    return HttpResponseRedirect('/exam/complete/')
                que=question_list_ten_biology[count_ten_biology]
                a=option_list_ten_biology[count_ten_biology+increment_ten_biology+0]
                b=option_list_ten_biology[count_ten_biology+increment_ten_biology+1]
                c=option_list_ten_biology[count_ten_biology+increment_ten_biology+2]
                d=option_list_ten_biology[count_ten_biology+increment_ten_biology+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'ans':ans,'count':question_count_ten_biology,'Rem':len(question_list_ten_biology)-count_ten_biology-1}
                return render(request,'exam/test.html',data)
            else:
                que=question_list_ten_biology[count_ten_biology]
                a=option_list_ten_biology[count_ten_biology+increment_ten_biology+0]
                b=option_list_ten_biology[count_ten_biology+increment_ten_biology+1]
                c=option_list_ten_biology[count_ten_biology+increment_ten_biology+2]
                d=option_list_ten_biology[count_ten_biology+increment_ten_biology+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_biology,'Rem':len(question_list_ten_biology)-count_ten_biology-1}
                res=render(request,'exam/test.html',data)
                return res

        else:
            que=question_list_ten_biology[count_ten_biology]
            a=option_list_ten_biology[count_ten_biology+increment_ten_biology+0]
            b=option_list_ten_biology[count_ten_biology+increment_ten_biology+1]
            c=option_list_ten_biology[count_ten_biology+increment_ten_biology+2]
            d=option_list_ten_biology[count_ten_biology+increment_ten_biology+3]
            level="Easy"
            data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_biology,'Rem':len(question_list_ten_biology)-count_ten_biology-1}
            res=render(request,'exam/test.html',data)
            return res
    elif request.session['number']=="10" and subject=="social":
        question_list_ten_social=['Mezni was associated with which organisation?','When did the Khilafat Movement Start in India?','In which of the these cities in india first juit mill established?','Whic was the first book published by GutenBurg?','Who is Known as the "Father Of The Nation"?','Which social Class Emerged as the Intellactual Class?',
        'Which among the following are not against color Descrimination?','Which state of India has Heighest per capita Income?','Which is the Central Bank of India?','What is the Main source of Energy?','Which of the following is Man-Made disaster?']
        option_list_ten_social=['Red-Army','Carbonary','Diet','Hetariya','1920','1935','1918','1925',
        'Kolkata','Mumbai','Delhi','Patna','Geeta','Bible','The Hitler','Movement-in-Russia',
        'Chacah-Nehru','Rajendra-Prasad','Mahatma-Gandhi','Raza-Ram-Mohan-Roy','Entrepreneur-Class','Middle-Class','Capitalist-Class','Labour-Class','Mahatma-Gandhi','Martin-Luthar','Z-Gudy','Hitler','Kerla','Punjab','Haryana','Goa','RBI','PNB','SBI','DBS','Coal','Petrolium','Electricity','All','Terrorism','Communal-Riot','Epidemic','All']
        answer_list_ten_social=['Carbonary','1920','Kolkata','Bible','Mahatma-Gandhi','Middle-Class','Z-Gudy','Goa','RBI','All','All']
        global count_ten_social
        global d_ten_social
        global increment_ten_social
        global question_count_ten_social
        if question_count_ten_social==0:
              question_count_ten_social=question_count_ten_social+1
        if request.method=='POST':
            if 'answer' in request.POST:
                ans=request.POST["answer"]
                selected_answer_list_ten_social.append(ans)
                count_ten_social=count_ten_social+1
                increment_ten_social=increment_ten_social+3
                question_count_ten_social=question_count_ten_social+1
                if count_ten_social==len(question_list_ten_social):
                    count_ten_social=0;
                    increment_ten_social=0;
                    question_count_ten_social=0
                    d_ten_social=0
                    list1=[]
                    return HttpResponseRedirect('/exam/complete/')
                que=question_list_ten_social[count_ten_social]
                a=option_list_ten_social[count_ten_social+increment_ten_social+0]
                b=option_list_ten_social[count_ten_social+increment_ten_social+1]
                c=option_list_ten_social[count_ten_social+increment_ten_social+2]
                d=option_list_ten_social[count_ten_social+increment_ten_social+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'ans':ans,'count':question_count_ten_social,'Rem':len(question_list_ten_social)-count_ten_social-1}
                return render(request,'exam/test.html',data)
            else:
                que=question_list_ten_social[count_ten_social]
                a=option_list_ten_social[count_ten_social+increment_ten_social+0]
                b=option_list_ten_social[count_ten_social+increment_ten_social+1]
                c=option_list_ten_social[count_ten_social+increment_ten_social+2]
                d=option_list_ten_social[count_ten_social+increment_ten_social+3]
                level="Easy"
                data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_social,'Rem':len(question_list_ten_social)-count_ten_social-1}
                res=render(request,'exam/test.html',data)
                return res

        else:
            que=question_list_ten_social[count_ten_social]
            a=option_list_ten_social[count_ten_social+increment_ten_social+0]
            b=option_list_ten_social[count_ten_social+increment_ten_social+1]
            c=option_list_ten_social[count_ten_social+increment_ten_social+2]
            d=option_list_ten_social[count_ten_social+increment_ten_social+3]
            level="Easy"
            data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level,'count':question_count_ten_social,'Rem':len(question_list_ten_social)-count_ten_social-1}
            res=render(request,'exam/test.html',data)
            return res
def sign_up(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully')
            fm.save()
            fm.username=" "
            fm.first_name=" "
            dict.clear()
    else:
        fm=SignUpForm()
    return render(request,'exam/sign_up.html',{'fm':fm})

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        number=request.POST['number']
        request.session['number']=number
        request.session['name']=username
        user=authenticate(username=username,password=password)
        data1="Standerd Must be Equal to 10"
        if user is not None:
            if int(number)<=10:
                login(request,user)
                user_score=mark.objects.get(name=username)
                dict['math']=user_score.math
                dict['english']=user_score.english
                dict['physics']=user_score.physics
                dict['chemistry']=user_score.chemistry
                dict['biology']=user_score.biology
                dict['social']=user_score.social
                return HttpResponseRedirect('/exam/feedback/')
            else:
                return render(request,'exam/user_login.html',{'data1':data1})
        else:
            data="Username or Password is incorrect"
            res=render(request,'exam/user_login.html',{'data':data})
            return res
    else:
        return render(request,'exam/user_login.html')


@login_required(login_url="/exam/login/")
def exam_complete(request):
    list1.clear()
    number_result=0
    request.session['num_english']=0
    request.session['num_physics']=0

    if request.session['number']=="10" and request.session['sub']=="math":
        for lst in range(len(answer_list_ten_math)):
            if selected_answer_list_ten_math[lst]==answer_list_ten_math[lst]:
                list1.append("true")
                number_result=number_result+1
                request.session['num_math']=number_result
                dict['math']=number_result

            else:
                list1.append("false")
        return render(request,'exam/user_profile.html',{'name':request.user,'number':number_result,'list':selected_answer_list_ten_math,'answerlist':answer_list_ten_math,'list1':list1,'dict':dict})

    elif request.session['number']=="10" and request.session['sub']=="english":
        for lst in range(len(answer_list_ten_english)):
            if selected_answer_list_ten_english[lst]==answer_list_ten_english[lst]:
                list1.append("true")
                number_result=number_result+1
                request.session['num_english']=number_result
                dict['english']=number_result

            else:
                list1.append("false")
        return render(request,'exam/user_profile.html',{'name':request.user,'number':request.session['num_english'],'list':selected_answer_list_ten_english,'answerlist':answer_list_ten_english,'list1':list1,'dict':dict})

    elif request.session['number']=="10" and request.session['sub']=="physics":
        for lst in range(len(answer_list_ten_physics)):
            if selected_answer_list_ten_physics[lst]==answer_list_ten_physics[lst]:
                list1.append("true")
                number_result=number_result+1
                request.session['num_physics']=number_result
                dict['physics']=number_result
            else:
                list1.append("false")
        return render(request,'exam/user_profile.html',{'name':request.user,'number':request.session['num_physics'],'list':selected_answer_list_ten_physics,'answerlist':answer_list_ten_physics,'list1':list1,'dict':dict})

    elif request.session['number']=="10" and request.session['sub']=="chemistry":
        for lst in range(len(answer_list_ten_chemistry)):
            if selected_answer_list_ten_chemistry[lst]==answer_list_ten_chemistry[lst]:
                list1.append("true")
                number_result=number_result+1
                request.session['num_chemistry']=number_result
                dict['chemistry']=number_result
            else:
                list1.append("false")
        return render(request,'exam/user_profile.html',{'name':request.user,'number':number_result,'list':selected_answer_list_ten_chemistry,'answerlist':answer_list_ten_chemistry,'list1':list1,'dict':dict})
    elif request.session['number']=="10" and request.session['sub']=="biology":
        for lst in range(len(answer_list_ten_biology)):
            if selected_answer_list_ten_biology[lst]==answer_list_ten_biology[lst]:
                list1.append("true")
                number_result=number_result+1
                request.session['num_biology']=number_result
                dict['biology']=number_result
            else:
                list1.append("false")
        return render(request,'exam/user_profile.html',{'name':request.user,'number':number_result,'list':selected_answer_list_ten_biology,'answerlist':answer_list_ten_biology,'list1':list1,'dict':dict})
    elif request.session['number']=="10" and request.session['sub']=="social":
        for lst in range(len(answer_list_ten_social)):
            if selected_answer_list_ten_social[lst]==answer_list_ten_social[lst]:
                list1.append("true")
                number_result=number_result+1
                request.session['num_social']=number_result
                dict['social']=number_result
            else:
                list1.append("false")
        return render(request,'exam/user_profile.html',{'name':request.user,'number':number_result,'list':selected_answer_list_ten_social,'answerlist':answer_list_ten_social,'list1':list1,'dict':dict})
def userLogout(request):
    selected_answer_list_ten_math.clear()
    selected_answer_list_ten_english.clear()
    selected_answer_list_ten_physics.clear()
    selected_answer_list_ten_chemistry.clear()
    selected_answer_list_ten_biology.clear()
    selected_answer_list_ten_social.clear()
    logout(request)
    return HttpResponseRedirect('/exam/login/')

@login_required(login_url="/exam/login/")
def userFeedback(request):
    return render(request,'exam/user_feedback.html',{'name':request.user})
l=[]
@login_required(login_url='/exam/login/')
def user_profile(request):
        marks=mark()
        total=0
        name1=request.session['name']
        marks.name=name1
        if 'math' in dict:
            marks.math=dict['math']
            total=total+dict['math']
        if 'english' in dict:
            marks.english=dict['english']
            total=total+dict['english']
        if 'physics' in dict:
            marks.physics=dict['physics']
            total=total+dict['physics']
        if 'chemistry' in dict:
            marks.chemistry=dict['chemistry']
            total=total+dict['chemistry']
        if 'biology' in dict:
            marks.biology=dict['biology']
            total=total+dict['biology']
        if 'social' in dict:
            marks.social=dict['social']
            total=total+dict['social']
        marks.total=total
        marks.save()
        get=mark.objects.get(name=name1)
        if request.method=="POST":
            fm=EditUserProfileForm(request.POST,instance=request.user)
            if fm:
                fm.save()
                return render(request,'exam/personal_page.html',{'fm':fm,'msg':"YOUR PROFILE HAS BEEN UPDATED SUCCESSFULLY ",'get':get})
        elif 'number' in request.session:

            if 'num_math' in request.session:
                math_number=request.session['num_math']
                fm=EditUserProfileForm(instance=request.user)

                return render(request,'exam/personal_page.html',{'fm':fm,'get':get})
            if 'num_english' in request.session:
                english_number=request.session['num_english']
                fm=EditUserProfileForm(instance=request.user)

                return render(request,'exam/personal_page.html',{'fm':fm,'get':get})
            if 'num_physics' in request.session:
                physics_number=request.session['num_physics']
                fm=EditUserProfileForm(instance=request.user)

                return render(request,'exam/personal_page.html',{'fm':fm,'get':get})
            if 'num_chemistry' in request.session:
                chemistry_number=request.session['num_chemistry']
                fm=EditUserProfileForm(instance=request.user)
                return render(request,'exam/personal_page.html',{'fm':fm,'get':get})
            if 'num_biology' in request.session:
                biology_number=request.session['num_biology']
                fm=EditUserProfileForm(instance=request.user)
                return render(request,'exam/personal_page.html',{'fm':fm,'get':get})
            if 'num_social' in request.session:
                social_number=request.session['num_socail']
                fm=EditUserProfileForm(instance=request.user)
                return render(request,'exam/personal_page.html',{'fm':fm,'get':get})



        else:
            return HttpResponseRedirect("/exam/login/")

def userLeaderBoard(request):
    list2=[]
    list3=[]
    list4=[]
    leader=mark.objects.all()
    for lead in leader:
        list2.append(lead.total)
    list2.sort()
    list2.reverse()
    length=len(leader)
    list=[]
    list_total=[]
    g=0
    for i in range(length):
        list.append(i+1)
    for m in list2:
        record=mark.objects.get(total=m)
        list3.append(record)

    if request.method=="POST":
        name=request.POST['top']
        msg=name
        for l2 in leader:
            list4.append(l2.name)
            list_total.append(l2.total)

        for lst in list4:
            if lst==name:
                g=g+1
        if g==1:
            rec=mark.objects.get(name=name)
            tot=list_total.index(rec.total)
            tot=tot+1
            return render(request,'exam/leader_board.html',{'leader':list3,'size':list,'record':rec,'rank':tot})
        else:
            return render(request,'exam/leader_board.html',{'leader':list3,'size':list,'msg':msg})
    else:
        return render(request,'exam/leader_board.html',{'leader':list3,'size':list})

def userChangePassword(request):
    msg="Confirm Password Doesnot Match"
    mr="Your Password Updated SUCCESSFULLY"
    if request.method=="POST":
        uname=request.POST['change']
        password1=request.POST['change1']
        password2=request.POST['change2']
        if password1==password2:
            obj=User.objects.get(username=uname)
            obj.set_password(password1)
            obj.save()
            return render(request,'exam/changepass.html',{'msg':mr})
        else:
            return render(request,'exam/changepass.html',{'msg':msg})
    return render(request,'exam/changepass.html')
