from ..model.user import User, UserInf
from ..model.Recipe import Recipe,Ingredient
from flask import make_response, jsonify
from .. import *
from sqlalchemy import and_, or_


# post just for managerment!!!!
def process_upload_igd(igd_info):
    response_data = {"igd_name": igd_info['igd_name'], "message": "fail to upload！"}
    status_code = 200
    print(igd_info)
    igd_dic = {"igd_name":None,
               "igd_category":None,
               "igd_opponent":None,
               "igb_description":None,
                "igd_calorie":0,
                "igd_img_url":None}

    igd = Ingredient.query.filter(Ingredient.igd_name == igd_info['igd_name']).first()
    if not igd:
        for key in igd_info.keys():
            if key in igd_dic.keys():
                igd_dic[key] = igd_info[key]

        igd= Ingredient(igd_name=igd_dic['igd_name'] ,
                        igd_category=igd_dic["igd_category"],
                        igd_opponent=igd_dic['igd_opponent'],
                        igb_description=igd_dic['igb_description'],
                        igd_calorie=igd_dic['igd_calorie'],
                        igd_img_url=igd_dic['igd_img_url'])
        db.session.add(igd)
        db.session.commit()
        response_data['message'] = f"{igd_info['igd_name']} upload successfully!!"
    else:
        response_data['message'] = f"{igd_info['igd_name']} already exist!!"
        status_code = 400

    resp = make_response(jsonify(response_data))
    resp.status_code = status_code

    return resp
# get
def process_select_igd_v1(igd_info):
    response_data = {"igd_name": igd_info['igd_name'], "message": "success"}
    status_code = 200

    igd = Ingredient.query.filter_by(username=igd_info["igd_name"]).first()
    if igd is None:
        response_data['message'] = 'failed,Ingredient is not exist'
        status_code = 400
    else:
        response_data['message'] = 'failed,Ingredient is not exist'

    resp = make_response(jsonify(response_data))
    resp.status_code = status_code
    return resp


