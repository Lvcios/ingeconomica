#_*_ coding:utf-8 _*_

from django.shortcuts import render_to_response
from django.core.context_processors import csrf
import datetime
from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField()
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

def contact(request):
	if request.method == 'POST': # If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']
			recipients = ['info@example.com']
			return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm() # An unbound form
	return render_to_response('form.html', {'form': form,})



def incio(request):
	tab = 'Incio'
	active_a = 'active'
	return render_to_response('index.html',locals())

def plan01(request,ingreso,isr,ibanco,inversion,financiamiento,vsalvamento,n):
	n = int(n) + 1
	ingreso = int(ingreso)
	cost = 0
	#dep = int(dep)
	cc = 0
	uai = 0
	isr = int(isr)/100.0
	udi = 0
	pp = 0
	fne = 0
	ibanco = int(ibanco)/100.0
	inversion = int(inversion)
	financiamiento = int(financiamiento)
	vsalvamento = int(vsalvamento)
	deuda = financiamiento
	pago_anual = 0
	costo_equipo = inversion + financiamiento
	pago_anual = financiamiento * round(((ibanco)*((1+ibanco)**(n-1))) / (((1+ibanco)**(n-1)) - 1),4) #calculo factor P(A/Pin)
	dep = ((costo_equipo -  vsalvamento)/(n-1))
	
	array_in = [ingreso]*n
	array_in[0] = 0
	array_de = [dep]*n
	array_de[0] = 0
	array_co = [0] * n
	array_cc = [0]*n #1
	array_pp = [0]*n #2
	array_uai = [0]*n #3
	array_isr = [0]*n #4
	array_udi = [0]*n #5
	array_fnc = [0]*n #6
	array_fnc[0] = inversion
	array_ani = [0]*n
	
	for i in range(1,n) :	
		array_cc[i] = round(deuda * ibanco,0)
		array_pp[i] = round(pago_anual - array_cc[i],0)
		deuda = round(deuda - array_pp[i],0)
		
	for i in range(1,n):
		array_uai[i] = ingreso - dep - array_cc[i]
	
	for i in range(1,n):
		array_isr[i] = array_uai[i]*isr
	
	for i in range(1,n):
		array_udi[i] = array_uai[i] - array_isr[i]

	for i in range(1,n):
		array_fnc[i] = array_udi[i] + dep - array_pp[i]  
	
	for i in range(n):
		array_ani[i] = i

	array_fnc[n - 1] = array_fnc[n - 1] + vsalvamento
	tab = 'PLAN 1'
	active_b = 'active'
	isr = int(isr*100)
	ibanco = int(ibanco*100)
	n = n -1
	return render_to_response('tabs.html',locals())

def plan02(request,ingreso,isr,ibanco,inversion,financiamiento,vsalvamento,n):
	n = int(n) +1 
	ingreso = int(ingreso)
	cost = 0
	#dep = int(dep)
	cc = 0
	uai = 0
	isr = int(isr)/100.0
	udi = 0
	pp = 0
	fne = 0
	ibanco = int(ibanco)/100.0
	inversion = int(inversion)
	financiamiento = int(financiamiento)
	vsalvamento = int(vsalvamento)
	deuda = financiamiento
	pago_anual = 0
	costo_equipo = inversion + financiamiento
	pago_anual = financiamiento / (n - 1)
	dep = ((costo_equipo -  vsalvamento)/(n-1))
	
	array_in = [ingreso]*n
	array_in[0] = 0
	array_de = [dep]*n
	array_de[0] = 0
	array_co = [0] * n
	array_cc = [0]*n #1
	array_pp = [0]*n #2
	array_uai = [0]*n #3
	array_isr = [0]*n #4
	array_udi = [0]*n #5
	array_fnc = [0]*n #6
	array_fnc[0] = inversion
	array_ani = [0]*n
	
	#Plan 02
	#Se conservan los ingresos, depreciación e interés
	#Mismo pago a principal durante los 5 años

	#Paso 1: Calcular el pago a principal
	for i in range(1,n) :	
		array_cc[i] = round(deuda * ibanco,0)
		array_pp[i] = pago_anual
		deuda = round(deuda - array_pp[i],0)
	
	for i in range(1,n):
		array_uai[i] = ingreso - dep - array_cc[i]
	
	for i in range(1,n):
		array_isr[i] = array_uai[i]*isr
	
	for i in range(1,n):
		array_udi[i] = array_uai[i] - array_isr[i]

	for i in range(1,n):
		array_fnc[i] = array_udi[i] + dep - array_pp[i]  
		
	for i in range(n):
		array_ani[i] = i	
	
	array_fnc[n - 1] = array_fnc[n - 1] + vsalvamento
	isr = int(isr*100)
	ibanco = int(ibanco*100)
	tab = 'PLAN 2'
	active_c = 'active'
	n = n -1	
	return render_to_response('tabs.html',locals())

def plan03(request,ingreso,isr,ibanco,inversion,financiamiento,vsalvamento,n):
	n = int(n) + 1
	ingreso = int(ingreso)
	cost = 0
	#dep = int(dep)
	cc = 0
	uai = 0
	isr = int(isr)/100.0
	udi = 0
	pp = 0
	fne = 0
	ibanco = int(ibanco)/100.0
	inversion = int(inversion)
	financiamiento = int(financiamiento)
	vsalvamento = int(vsalvamento)
	deuda = financiamiento
	pago_anual = 0
	costo_equipo = inversion + financiamiento
	pago_anual = financiamiento
	dep = ((costo_equipo -  vsalvamento)/(n-1))
	
	array_in = [ingreso]*n
	array_in[0] = 0
	array_de = [dep]*n
	array_de[0] = 0
	array_co = [0] * n
	array_cc = [0]*n #1
	array_pp = [0]*n #2
	array_pp[n - 1] = pago_anual
	array_uai = [0]*n #3
	array_isr = [0]*n #4
	array_udi = [0]*n #5
	array_fnc = [0]*n #6
	array_fnc[0] = inversion
	array_ani = [0]*n
	
	
	for i in range(1,n) :	
		array_cc[i] = round(deuda * ibanco,0)

	for i in range(1,n):
		array_uai[i] = ingreso - dep - array_cc[i]
	
	for i in range(1,n):
		array_isr[i] = array_uai[i]*isr
	
	for i in range(1,n):
		array_udi[i] = array_uai[i] - array_isr[i]

	for i in range(1,n):
		array_fnc[i] = array_udi[i] + dep - array_pp[i]  
		
	for i in range(n):
		array_ani[i] = i
	
	array_fnc[n-1] = array_fnc[n-1] + vsalvamento
	
	isr = int(isr*100)
	ibanco = int(ibanco*100)
	tab = 'PLAN 3'
	active_d = 'active'
	n = n -1
	return render_to_response('tabs.html',locals())
	
def plan04(request,ingreso,isr,ibanco,inversion,financiamiento,vsalvamento,n):
	n = int(n) +1 
	ingreso = int(ingreso)
	cost = 0
	#dep = int(dep)
	cc = 0
	uai = 0
	isr = int(isr)/100.0
	udi = 0
	pp = 0
	fne = 0
	ibanco = int(ibanco)/100.0
	inversion = int(inversion)
	financiamiento = int(financiamiento)
	vsalvamento = int(vsalvamento)
	deuda = financiamiento
	pago_anual = 0
	costo_equipo = inversion + financiamiento
	pago_anual = financiamiento
	dep = ((costo_equipo -  vsalvamento)/(n-1))
	array_in = [ingreso]*n
	array_in[0] = 0
	array_de = [dep]*n
	array_de[0] = 0
	array_co = [0] * n
	array_cc = [0]*n #1
	array_pp = [0]*n #2
	array_pp[n-1] = pago_anual
	array_uai = [0]*n #3
	array_isr = [0]*n #4
	array_udi = [0]*n #5
	array_fnc = [0]*n #6
	array_fnc[0] = inversion
	array_ani = [0]*n
	
	#paso 1 obtener el cc completo al final del ultimo año
	array_cc[n-1] = round(financiamiento * ((1 + ibanco)**(n-1)),0)
	array_cc[n-1] = array_cc[n-1] - pago_anual
	
	for i in range(1,n):
		array_uai[i] = ingreso - dep - array_cc[i]
	
	for i in range(1,n):
		array_isr[i] = array_uai[i]*isr
	
	for i in range(1,n):
		array_udi[i] = array_uai[i] - array_isr[i]

	for i in range(1,n):
		array_fnc[i] = array_udi[i] + dep - array_pp[i]  
		
	for i in range(n):
		array_ani[i] = i
	
	array_fnc[n-1] = array_fnc[n-1] + vsalvamento
	isr = int(isr*100)
	ibanco = int(ibanco*100)
	tab = 'PLAN 4'
	active_e = 'active'
	n = n -1
	return render_to_response('tabs.html',locals())


def simple(request):
	import random
	import django
	import datetime
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter	
	fig = Figure()
	ax = fig.add_subplot(111)
	x = []
	y = []
	now=datetime.datetime.now()
	delta=datetime.timedelta(days=1)
	for i in range(10):
		x.append(now)
		now+=delta
		y.append(random.randint(0, 1000))
	ax.plot_date(x, y, '-')
	ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
	fig.autofmt_xdate()
	canvas=FigureCanvas(fig)
	response=django.http.HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response
