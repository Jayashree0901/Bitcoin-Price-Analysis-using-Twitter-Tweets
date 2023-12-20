from flask import Blueprint, render_template,request,flash, redirect,url_for
import csv
import random
import math
import numpy as np
import pandas as pd




views = Blueprint('views',__name__)


@views.route('/real_dataset')
def tp():
    
    return render_template("index1.htm")


@views.route('/existing_dataset')
def tp1():

    return render_template("index.htm")





     

