from django.template import Context,loader,RequestContext
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound

def doOperation(request):
	temp=0
	first=0
	a=0
	b=0
	sum=0
	res=0
	button_press=False	
	
	if request.POST:
		if 'num' in request.POST.keys():
			if 'capture' in request.POST and request.POST['capture'] =='true':
				b=''
			else:
				b = request.POST['valueof']
			a = request.POST['num']
			sum=b+a
			if 'val' in request.POST and request.POST['val'] != '':
				temp=request.POST['val'] + a
			else:
				temp=b+a
			return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":sum,"a":temp,}))
		elif '+' in request.POST.keys():
			if 'capture' in request.POST and request.POST['capture'] == 'true':
				b=''
			else:
				b = request.POST['valueof']
			
			first = request.POST['val']
			a=' + '
			res = first.split()
			k = len(res)
			if k == 1:
				return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":'',"a":first + a,'capture':"true"}))
			else:
				try:
					if res[1] == '+':
						b = str(int(res[0]) + int (res[2]))
						#a = ' + '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '-':
						b = str(int(res[0]) - int (res[2]))
						#a = ' + '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '*':
						b = str(int(res[0]) * int (res[2]))
						#a = ' + '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '/':
						b = str(int(res[0]) / int (res[2]))
						#a = ' + '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
				except ZeroDivisionError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"ZeroDivisionError (Add Func):"+str(detail)}))
				except OverflowError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"OverflowError (Add Func):"+str(detail)}))	
				except NameError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"NameError (Add Func):"+str(detail)}))	
				except Exception as detail:
					errors=["An Exception Occured (Add Func): No Integer Value Provided.","Do not enter values manually","Use numeric buttons only"]
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"errors":errors}))
					
						
		elif '-' in request.POST.keys():
			if 'capture' in request.POST and request.POST['capture'] == 'true':
				b=''
			else:
				b = request.POST['valueof']
				
			first = request.POST['val']
			a=' - '
			res = first.split()
			k = len(res)
			if k == 1:
				return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":'',"a":first + a,'capture':"true"}))
			else:
				try:
					if res[1] == '+':
						b = str(int(res[0]) + int (res[2]))
						#a = ' - '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '-':
						b =str(int(res[0]) - int (res[2]))
						#a = ' - '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '*':
						b = str(int(res[0]) * int (res[2]))
						#a = ' - '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '/':
						b = str(int(res[0]) / int (res[2]))
						#a = ' - '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
				except ZeroDivisionError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"ZeroDivisionError (Sub Func):"+str(detail)}))
				except OverflowError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"OverflowError (Sub Func):"+str(detail)}))	
				except NameError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"NameError (Sub Func):"+str(detail)}))	
				except Exception as detail:
					errors=["An Exception Occured (Add Func): No Integer Value Provided.","Do not enter values manually","Use numeric buttons only"]
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"errors":errors}))
			
		elif '*' in request.POST.keys():
			if 'capture' in request.POST and request.POST['capture'] == 'true':
				b=''
			else:
				b = request.POST['valueof']
				
			first = request.POST['val']
			a=' * '
			res = first.split()
			k = len(res)
			if k == 1:
				return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":'',"a":first + a,'capture':"true"}))
			else:
				try:
					if res[1] == '+':
						b = str(int(res[0]) + int (res[2]))
						#a = ' * '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '-':
						b = str(int(res[0]) - int (res[2]))
						#a = ' * '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '*':
						b = str(int(res[0]) * int (res[2]))
						#a = ' * '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '/':
						b = str(int(res[0]) / int (res[2]))
						#a = ' * '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
				except ZeroDivisionError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"ZeroDivisionError (Mul Func):"+str(detail)}))
				except OverflowError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"OverflowError (Mul Func):"+str(detail)}))	
				except NameError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"NameError (Mul Func):"+str(detail)}))	
				except Exception as detail:
					errors=["An Exception Occured (Add Func): No Integer Value Provided.","Do not enter values manually","Use numeric buttons only"]
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"errors":errors}))
			
		elif '/' in request.POST.keys():
			if 'capture' in request.POST and request.POST['capture'] == 'true':
				b=''
			else:
				b = request.POST['valueof']
				
			first = request.POST['val']
			a=' / '
			res = first.split()
			k = len(res)
			if k == 1:
				return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":'',"a":first + a,'capture':"true"}))
			else:
				try:
					if res[1] == '+':
						b = str(int(res[0]) + int (res[2]))
						#a = ' / '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '-':
						b = str(int(res[0]) - int (res[2]))
						#a = ' / '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '*':
						b = str(int(res[0]) * int (res[2]))
						#a = ' / '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
					elif res[1] == '/':
						b = str(int(res[0]) / int (res[2]))
						#a = ' / '
						return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":b + a,'capture':"true"}))
				except ZeroDivisionError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"ZeroDivisionError (Div Func):"+str(detail)}))
				except OverflowError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"OverflowError (Div Func):"+str(detail)}))	
				except NameError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"NameError (Div Func):"+str(detail)}))	
				except Exception as detail:
					errors=["An Exception Occured (Add Func): No Integer Value Provided.","Do not enter values manually","Use numeric buttons only"]
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"errors":errors}))
		
		elif 'clear' in request.POST.keys():
			return render(request,'./calculator/calculator.html',{})

		elif '=' in request.POST.keys():
			try:
				button_press=True
				b = request.POST['val']
				res = b.split()
				if res[1] == '+':
					b = str(int(res[0]) + int (res[2]))
					a = ''
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":a,"capture":"true"}))
				elif res[1] == '-':
					b = str(int(res[0]) - int (res[2]))
					a = ''
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":a,"capture":"true"}))
				elif res[1] == '*':
					b = str(int(res[0]) * int (res[2]))
					a = ''
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":a,"capture":"true"}))
				elif res[1] == '/':
					b = str(int(res[0]) / int (res[2]))
					a = ''
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":a,"capture":"true"}))
			except ZeroDivisionError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"Equal Function:"+str(detail)}))
			except OverflowError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"Equal Function:"+str(detail)}))	
			except NameError as detail:
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"error":"Equal Function:"+str(detail)}))	
			except Exception as detail:
					errors=["An Exception Occured (Add Func): No Integer Value Provided.","Do not enter values manually","Use numeric buttons only"]
					return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"errors":errors}))
	else:
		b = ''
		a = ''
		return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":a,}))

def pageNotFound(request):
	b = ''
	a = ''
	errors=["Invalid URL provided. Please use 127.0.0.1:8000 only."]
	return render(request,'./calculator/calculator.html',context_instance=RequestContext(request,{"b":b,"a":a,"errors":errors}))
