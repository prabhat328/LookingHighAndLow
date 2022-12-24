# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
import requests
import mysql.connector as sql

db = sql.connect(host='sql6.freesqldatabase.com', user='sql6585458',passwd="SPx7YNG9q3", database='sql6585458',port='3306')
cursor = db.cursor()

def start(request):
    if request.method=="POST":
        cc = request.POST['cc']
        loc_id = request.POST['loc_id']
        try:
            prev_loc = request.POST['prev_loc']
        except:
            prev_loc = 'none'
        alltno = ['cc1','cc2','cc3']; 
        for i in alltno:
            # verifying team/contingent no.
            if(i==cc): 
                # global t1
                qr_verf=f"select loc_c from otwtry2 where loc_c='{loc_id}'"
                cursor.execute(qr_verf)
                t1=tuple(cursor.fetchall())
                global qr_auth,hint
                # verifying QR scanned
                try:
                    qr_auth=t1[0][0]
                except:
                    # context={'qr_n_m':'Wrong QR scanned',}
                    # return render(request,'welcome.html',context)
                    return HttpResponse('''<script>alert("Wrong QR scanned")</script>''')
                else:
                    nxt_hnt=f"select {cc} from otwtry2 where loc_c='{loc_id}' and prev_{cc}='{prev_loc}'"
                    cursor.execute(nxt_hnt)
                    t2=tuple(cursor.fetchall())
                    try:
                        hint = t2[0][0]
                    except:
                        # context={'loc_n_m':'Last location does not match',}
                        # return render(request,'welcome.html',context)
                        return HttpResponse('''<script>alert("Last location does not match")</script>''')
                    else:
                        # context={'hint':hint,}
                        # return render(request,'welcome.html',context)
                        return redirect('/p1')
                
        else:
            # context={'tno_n_m':'Invalid team no.',}
            # return render(request,'welcome.html',context)
            return HttpResponse('''<script>alert("Invalid team no.")</script>''')
    return render(request, 'welcome.html')


def comp1(request):
    return HttpResponse(f"<h1>Next Hint: {hint}</h1>")

