Folder structure
----------------

1) Find the calculator.html file in the path: calculator/templates/calculator/calculator.html

2) Find the css file for the html in the path: calculator/static/calculator/css/calculator.css


Program Execution
-----------------

- Just run the python server and type the ip 127.0.0.1:8000, you will see the html page.

- If the url specified is something like this http://127.0.0.1:8000/sf/sfs/sf or 
   127.0.0.1:8000/sf/sfs/sf then the request will be redirected to the same page
   with an error being displayed below the calculator.
   
- Do not provide url with more than 3 '/' such as 127.0.0.1:8000/sf/sfs/sf/viv, because 
   the path provided in the pageNotFound of view.py file is not getting CSS displayed 
   properly.  Do not understand why?
   
- If you type in the address bar like 127.0.0.1:8000/calculator, you will not be 
  redirected to any page but stay in the same page itself because regular expression 
  in the root urls file doesn't recognize it.

-If you enter manually some string or integers, and try to perform any operation an 
 error will be thrown on the same screen indicated below the calculator.




