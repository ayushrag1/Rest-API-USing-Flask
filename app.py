from flask import Flask, request, jsonify
import requests
from datetime import datetime
app = Flask(__name__)

# Base URL of the existing API
base_api_url = "https://app.ylytic.com/ylytic/test"
try:
    response = requests.get(base_api_url)
    response_data =response.json()
except Exception as e:
    print(f"connection error {e}")
    response_data={}

def validate(query_params, json_object):
    date_to_check, author, like, reply, text=list(json_object.values())
    date_to_check = datetime.strptime(date_to_check, '%a, %d %b %Y %H:%M:%S GMT')
        
    if 'search_author' in query_params and query_params['search_author'] not in author:
        return False

    elif 'at_from' in query_params and 'at_to' in query_params and (date_to_check< query_params['at_from'] or date_to_check > query_params['at_to']):
        print('date')
        return False
    
    elif 'like_from' in query_params and 'like_to' in query_params and (like< query_params['like_from'] or like > query_params['like_to']):
        print('like')
        return False
    
    elif 'reply_from' in query_params and 'reply_to' in query_params and (reply< query_params['reply_from'] or reply > query_params['reply_to']):
        print('reply')
        return False
    
    elif 'search_text' in query_params and query_params['search_text'] not in text:
        return False

    return True

@app.route("/search", methods=["GET"])
def search_comments():
    # Define the default query parameters
    try:
        if len(response_data)==0:
            raise Exception(f"Can't get any data from base_api_url {base_api_url}")
        query_params = {
            "search_author": request.args.get("search_author", None),
            "at_from": request.args.get("at_from", None),
            "at_to": request.args.get("at_to", None),
            "like_from": request.args.get("like_from", None),
            "like_to": request.args.get("like_to", None),
            "reply_from": request.args.get("reply_from", None),
            "reply_to": request.args.get("reply_to", None),
            "search_text": request.args.get("search_text", None),
        }
        

        # Remove None values from the query_params
        query_params = {k: v for k, v in query_params.items() if v is not None}
        if len(query_params)==0:
            raise Exception("please enter valid paramters")
        for key,value in query_params.items():
            if key=='at_from':
                query_params[key]=datetime.strptime(value, '%d-%m-%Y')
            elif key=='at_to':
                query_params[key]=datetime.strptime(value, '%d-%m-%Y')
            elif key=='like_from':
                query_params[key]=int(value)
            elif key=='like_to':
                query_params[key]=int(value)
            elif key=='reply_from':
                query_params[key]=int(value)
            elif key=='reply_to':
                query_params[key]=int(value)
        
        
        # Make a request to the existing API with the filtered query parameters
        result = [i for i in response_data['comments']if validate(query_params=query_params,json_object=i)]

        # Return the JSON response from the existing API
        return jsonify({'success':True, 'result':result}),200
    except Exception as e:
        # Handle the case where the existing API returns an error
        return jsonify({'success':False,"message": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True)

