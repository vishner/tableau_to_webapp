from flask import Flask, abort, render_template, redirect, url_for, request, make_response
from urllib.parse import urlparse, urljoin
import requests, tableauserverclient as TSC
from flask_talisman import Talisman
from secret import SECRET_KEY, TABLEAU_AUTH, USERS_LIST, PASSWORD_LOGIN
import base64
import datetime




app = Flask(__name__)
app.secret_key = SECRET_KEY

from PIL import Image

global_token = ""
server = TSC.Server('https://tabsmxnprod/')
server.add_http_options({'verify': False})
server.use_server_version()
folder_path = "static/images"

import io 
from flask import Response

@app.route('/tableau_view') 
def tableau_view(): 
# Step 1: Create a server instance 
    server.auth.sign_in(TABLEAU_AUTH)
    view_item = server.views.get_by_id('bc6579db-bb60-4836-a70f-a528b048741e') # Step 4: Render the view as an image 
    server.views.populate_image(view_item)
    
    image_bytes = view_item.image
    
    
    image_buffer = io.BytesIO(image_bytes)
    headers = {'Content-Type': 'image/png'}
    
    return Response(image_buffer, headers=headers)

@app.route('/report1') 
def report1(): 
# Step 1: Create a server instance 
    server.auth.sign_in(TABLEAU_AUTH)
    view_item = server.views.get_by_id('bc6579db-bb60-4836-a70f-a528b048741e') # Step 4: Render the view as an image
    server.views.populate_image(view_item,)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #test on image of current time to show that image really refreshes
    # image = _generate_sample_img(timestamp)

    #-----
    image_bytes = view_item.image
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((1920, 900))
    # ---
    image_buffer = io.BytesIO()
    image.save(image_buffer, format='PNG')
    encoded_image = base64.b64encode(image_buffer.getvalue()).decode('utf-8')
    return render_template('image.html', encoded_image=encoded_image)

@app.route('/report_full') 
def report_full():
    server.auth.sign_in(TABLEAU_AUTH)
    view_item = server.views.get_by_id('bc6579db-bb60-4836-a70f-a528b048741e') # Step 4: Render the view as an image
    server.views.populate_image(view_item,)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #test on image of current time to show that image really refreshes
    # image = _generate_sample_img(timestamp)

    #-----
    image_bytes = view_item.image
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((1920, 900))
    # ---
    image_buffer = io.BytesIO()
    image.save(image_buffer, format='PNG')
    encoded_image = base64.b64encode(image_buffer.getvalue()).decode('utf-8')
    return render_template('image.html', encoded_image=encoded_image)

@app.errorhandler(404)
def page_not_found(e):
# Step 1: Create a server instance
    server.auth.sign_in(TABLEAU_AUTH)
    view_item = server.views.get_by_id('bc6579db-bb60-4836-a70f-a528b048741e') # Step 4: Render the view as an image
    image_req_opt = TSC.ImageRequestOptions(maxage=1)
    server.views.populate_image(view_item,image_req_opt)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #test on image of current time to show that image really refreshes
    # image = _generate_sample_img(timestamp)

    #-----
    image_bytes = view_item.image
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((1920, 900))
    # ---
    image_buffer = io.BytesIO()
    image.save(image_buffer, format='PNG')
    encoded_image = base64.b64encode(image_buffer.getvalue()).decode('utf-8')
    return render_template('image.html', encoded_image=encoded_image)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8000)
    
