__author__ = 'lukehsu'
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import forms
from pymongo import Connection
import datetime
import time
class UserForm(forms.Form):

    headImg = forms.FileField(label="pic")
    content = forms.CharField(widget=forms.Textarea())
    price = forms.CharField()
def regist(req):

    if req.method == 'POST':
        uf = UserForm(req.POST, req.FILES)
        if uf.is_valid():
            f = open('./mysite/static/pic/%s' % uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            f.write(s)
            f.close()
            conn = Connection('localhost', 27017)
            db = conn.test
            db.authenticate("test", "test")
            dbt = db.test
            pic = uf.cleaned_data['headImg'].name
            content = uf.cleaned_data['content']
            price = uf.cleaned_data['price']
            t = time.time()
            s = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
            intime = str(s)
            post = {"pic": pic, "content": content, "price": price,"time": intime}
            dbt.insert(post)
            return render_to_response('re.html')
    else:
        uf = UserForm()
    return render_to_response('back.html', {'uf': uf})