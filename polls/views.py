# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
import requests
import mysql.connector as sql
from datetime import datetime

db = sql.connect(host='sql6.freesqldatabase.com', user='sql6586638',passwd="R8SlQ9d8jn", database='sql6586638')
# db = sql.connect(host='localhost', user='root',passwd="151103", database='simplipay')
cursor = db.cursor()

def start(request):
    if request.method=="POST":
        cc = request.POST['cc']
        loc_c = request.POST['loc_id']
        try:
            prev_loc = request.POST['prev_loc']
        except:
            prev_loc = 'none'
        alltno = ['cc1','cc2','cc3']; 
        for i in alltno:
            # verifying team/contingent no.
            if(i==cc): 
                # global t1
                qr_verf=f"select loc_c from otwtry2 where loc_c='{loc_c}'"
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
                    nxt_hnt=f"select {cc},timestamp from otwtry2 where loc_c='{loc_c}' and prev_{cc}='{prev_loc}'"
                    cursor.execute(nxt_hnt)
                    global t2
                    t2=tuple(cursor.fetchall())
                    try:
                        hint = t2[0][0]
                    except:
                        # context={'loc_n_m':'Last location does not match',}
                        # return render(request,'welcome.html',context)
                        return HttpResponse('''<script>alert("Last location does not match")</script>''')
                    else:
                        global visit_status
                        global ts_chk
                        ts_chk=t2[0][1]
                        print(t2)
                        if(ts_chk==None):
                            ts = f'{datetime.now()}'
                            print(ts)
                            ts_query = f"UPDATE `otwtry2` SET `timestamp` = '{ts}' WHERE `loc_c` = '{loc_c}'"
                            cursor.execute(ts_query)
                            db.commit()
                            visit_status = "Visiting first time"
                        else:
                            visit_status = f"Reached at {ts_chk}"
                        # context={'hint':hint,}
                        # return render(request,'welcome.html',context)
                        return redirect('/p1')
                
        else:
            # context={'tno_n_m':'Invalid team no.',}
            # return render(request,'welcome.html',context)
            return HttpResponse('''<script>alert("Invalid team no.")</script>''')
    return render(request, 'welcome.html')


def comp1(request):
    try:
        return HttpResponse(f"<h1>{visit_status}\nNext Hint: {hint}</h1>")
    except:
        return HttpResponse(f"<h1>Next Hint: {hint}</h1>")
