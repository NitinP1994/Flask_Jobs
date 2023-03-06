'''
    1) creating a minimal app with flask and using debug mode and also use host which is 
      optional also we can change port by default port is set to 5000

'''

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hello, World !!!"

# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True)


###########################################################################################

''' 2) now we are introducing html and css files in our projects 
        1) we create templates folder which contain all html files
        2) we create and write a small html file name is home.html
        3) now er hsve to render this file in our actual web so we use render_template function

'''

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     # return "Hello, World !!!"
#     return render_template('home.html')

# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True)


#########################################################################################

''' 3)  now we are creating pages and detail project form below make some changes in our 
        html file please check and try to make wire frame we need design and rough wire frame
        on blank page etc.
        1) we add heading as Jovian Carriers using <h1><h1> tags.
        2) now with that heading we have to add image  <img src="copy url here it gives image/or set image through static folder get access">
            1) if url not able to show image the we have to upload image loacally in static folder
            2) if any folder under the static folder will be directly shared by flask externally.
            3) our banner.jpeg file under static folder we copy url as path and copy this path
                into home01.html file's image section for get accession that image from static folder
            4) as we see on web image size is too large so we have to specify width and height
             
            5) image downloaded from unsplash.com and rename that image
'''  

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     # return "Hello, World !!!"
#     return render_template('home01.html')

# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True)


#############################################################################################

'''
    4) above we set jovian carriers heading size and set image now we fill some info about
        jovian 
        1) after we set about jovian heading then now we no need to type lot of text so we 
        need text generator eg. to search lorem ipsum text generator on google.
        2) then we have generate some text in paragraph so we have choose how much para you 
          want just select and generate then copy that para and copy that para in home02.html
          file.
        
        3) on the same page below about jovian next task is job openings 
        4) adding button for contact us
        

'''

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     # return "Hello, World !!!"
#     return render_template('home02.html')

# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True)


#########################################################################################

'''
    5) now we are providing some styles to our pages.
        1) we create <style></style> tage in our html head tag and in this style tag we need to 
        tell the browserhow to apply a certain colour or certain layout to a specific portion
        of html page. see the html page
        2) in this style tag type tag h1 and use {...some info...refer..html03 file} and now we 
          are able apply some styles.
           every style you applies has 2 parts.
           1) what property you want to change eg. font-size:40px; font-family : Robot; etc.
           2) for image we set id="banner" which is in body part of html and using # singn in
              in head part of html and create #banner {} and in bracess set image height, width
           3) now About Jovian set as like first we set for text it is in first step. using h2{}
           4) now for paragraph in head part's stype tag below h2{} we type p{} and set style
                for para in braces.
           5)  now we put all things in <div> tag in body of html page so it allign properly and
             not acquire whole space. which ends after contact us button
           6) then in that div we take id="container". and this useful styling purpose use in
               head tag in style tag use #container{} and in bracess we set style.
               1) margin : 0 auto; is best opion used most of the time
           7) adjust the contact us button at the center using style but in different way check
                html03 file  
           8)  below contact us button we use paragraph <p>copyright 2023, Jovian</p>  in this 
                we use p for styling so that style applied same on this para also but if we
                doesnt want to make changes like other para then see html03 file
'''

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     # return "Hello, World !!!"
#     return render_template('home03.html')

# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True)


###########################################################################################

'''
6) above we see we are mannually made the changes but we have alredy avaliable codes that can
   styling or designig our pages through css for eg. using getsbootstrap.com
    we have first remove all styles from top to bottom from our html04 file
      
       yet we are not using bootstrap code we just copy
    1) from web first we just copy some tags
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1"> and paste into
        html04 file below jovian carrier title.
    2) second step we copy link 
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        and paste that link into the head tag below the meta tag
        this link tag is the way to add link some other resources on internet inside our html
        page
    
    3) after making some chages like making <div class="container"> for text in body and for
       image <div class="img-fluid"> then we need some styling we below link tag in head adding
       style tag.

    4) now we are aligning text at center for all header <h1 class="text-center"> in body
    5) how to increase font size of para of abou jovian <p class="lead">
    6) if we need some margine then we use my , mx, mt, mb see home04 file for heading
    7) fix button <button class="btn btn-primary btn-lg" and align button at the center.
    8) add some spacing between copyright and button <p class="mt-4">

'''


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     # return "Hello, World !!!"
#     return render_template('home04.html')

# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True)


#########################################################################################

'''
7) How to show dynamic data on a webpage
    it is not good idea to just list all the jobs and directly write into the html file
    because everytime we have goto the html file and add new job and remove the job or made 
    some changes and making some changes directly in the html file can be tricky so according
    to this we have to stored data in somewhere else in the database where administrator can 
    directly create jobs or made some changes with that database and then this info get fetch
    from a database and entered into html file and displayed on the screen and send to the 
    browser.

    1) we are not going to connect database yet but we are going to simmulate something simmilar
       creating a pyton list job which can store the info about job to keep track of
    
    2) we are seperating job item from html file and making jobitem.html file and paste those 
      all data which is related to the job and then using just {% include 'jobitem.html' %}

    3) now adding apply button to the right side and underline each job position.
       1) for border at the bottom our code in jobitems.html page so we can made change check
          file. if we want some space inside bottom we use padding else we use margin for the
          outside
        
       2) we create apply butten using primary button code from bootstrap and paste into
          the jobitems.html page.

       3)  column wrapping for making table like copy code from bootstrap 
      

'''
# from flask import Flask, render_template

# app = Flask(__name__)


# JOBS = [ 
#     {
#       'id': 1,
#       'title': 'Data Analyst',
#       'location': 'Benguluru, India',
#       'salary': '10,00,000 P/A'

#     },
#     {
#       'id': 2,
#       'title': 'Data Scientist',
#       'location': 'Delhi, India',
#       'salary': '15,00,000 P/A'

#     },
#     {
#       'id': 3,
#       'title': 'Frontend Engineer',
#       'location': 'Remote',
      

#     },
#     {
#       'id': 4,
#       'title': 'Backend Engineer',
#       'location': 'Pune, India',
#       'salary': '13,00,000 P/A'

#     },
# ]

# ''' here this jobs list provide in render template after that we goto the home05 file in jobs
#     part and <p> {{jobs}} </p>
# '''

# @app.route('/')
# def hello_world():
#     # return "Hello, World !!!"
#     return render_template('home05.html', 
#                            jobs=JOBS,
#                            company_name = "Jovian") #we made changes in title check file

# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True)

''' this one way to create dyanmaic data base web'''

########################################################################################

'''
8) now lets check another way to create dynamic data base websites with the help of some websites
  that allows us to access some dynamic data using in our api instead of returning hmtl we can 
  return some json. json is simply java script objects

    1) we need to jsonify our jobs this function avaliable with our flask lib we use jsonify
       infront of render_template

'''

from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [ 
    {
      'id': 1,
      'title': 'Data Analyst',
      'location': 'Benguluru, India',
      'salary': '10,00,000 P/A'

    },
    {
      'id': 2,
      'title': 'Data Scientist',
      'location': 'Delhi, India',
      'salary': '15,00,000 P/A'

    },
    {
      'id': 3,
      'title': 'Frontend Engineer',
      'location': 'Remote',
      

    },
    {
      'id': 4,
      'title': 'Backend Engineer',
      'location': 'Pune, India',
      'salary': '13,00,000 P/A'

    },
]


@app.route('/')
def hello_world():
    # return "Hello, World !!!"
    return render_template('home06.html', 
                           jobs=JOBS,
                           company_name = "Jovian")   # this html version of data

@app.route('/api/jobs') 
def list_jobs():
    return jsonify(JOBS)  #we create json object This is json version of data

''' instead of rendering a template through html we can simply jsonify the the data
     API : application programming interface and it is just url which does not return html to
     be shown on the browser but it return some structured data in the form of json which is 
     programatically analyse so we create job endpoint and check that end point and then we 
     can create/replace that end point '/jobs' with '/api/jobs'.
''' 

 
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)


#############################################################################################

'''
now we have to deploy this website on cloud. in some sense this website already deployed on 
replet but is better suited foe development purpose, reple can shutdown any down any time
beacuse it is free resources and it is unable to handle large workload all these reasons
  1) now we are put it this into productions we need some cloud platform where we are going to
    do this.  eg. AWS, render.com, google cloud, azure etc.

  2) we are deploying on render.com cloud so goto this website we have to create account

'''