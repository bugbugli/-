
from app.home import blueprint
from flask import render_template, redirect, url_for,request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound

from app.home.models import goods,CommissionReturn,order,DealReturn,picture,TWII,transform_date

TWII = TWII()#提早到這裡呼叫TWII(),避免每個頁面重新呼叫
@blueprint.route('/index')
@login_required
def index():

    return render_template('index.html',TWII = TWII)

@blueprint.route('/<template>',methods=['POST','GET'])
def route_template(template):
    try:
        #print(template)
        if not template.endswith( '.html' ):
            template += '.html'
        if request.method == "POST":
            CompCode = request.form["id"]
            buysell = request.form["buy/sell"]
            if buysell == "buy":
                return render_template(template, tt=order(CompCode,"B"),content=goods(),TWII=TWII)
            else:
                return render_template(template, tt=order(CompCode,"S"),content=goods(),TWII=TWII)
        if template == 'asset.html':
            return render_template(template, content=goods(),TWII=TWII)
        elif template =='order.html':
            #print(picture())
            return render_template(template, content=CommissionReturn(),deal=DealReturn(),tt=picture(),TWII=TWII)
        elif template =='homepage.html':
            return render_template(template,TWII=TWII)
        else:
            return render_template(template,TWII=TWII)

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500
