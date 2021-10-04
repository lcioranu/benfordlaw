import csv, json, math, os


import pandas as pd
from flask import Blueprint, render_template, request, current_app

bluePrint = Blueprint("bluePrint", __name__)
fileName = ""
target = '7_2009'


@bluePrint.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template("index.html")


@bluePrint.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    os.makedirs(os.path.join(current_app.instance_path, 'files'), exist_ok=True)
    f.save(os.path.join(current_app.instance_path, 'files', f.filename))
    global fileName
    fileName = f.filename
    f = open(os.path.join(current_app.instance_path, 'files', f.filename), "r")
    return render_template("index.html")


@bluePrint.route('/preview')
def previewfile():
    try:
        df = readData(fileName)
    except Exception as e:
        return "Error reading data. Please check your file"
    return df.to_html(classes='table table-striped table-sm', max_rows=10, table_id="dataframe_table")


@bluePrint.route('/generate')
def generateChartData():
    targetField = request.args.get('target')
    touplelist = generate(os.path.join(current_app.instance_path, 'files', fileName), targetField)
    return json.dumps(touplelist)


@bluePrint.route('/header')
def getHeader():
    df = readData(fileName)
    json_file = json.dumps(df.columns.values.tolist())
    return  json_file


def readData(file):
    df = pd.read_csv(os.path.join(current_app.instance_path, 'files', fileName), delimiter=getDelimiter())
    return df


def targetList(df, target_column):
    return df[target_column].tolist()


def generate(file, target_column):
    column_list = targetList(readData(fileName), target_column)
    numberOfRec = len(column_list)
    int_list = []
    bedford_list = []
    for i in range(len(column_list)):
        if not math.isnan(column_list[i]):
            value = math.trunc(column_list[i])
            int_list.append(value // 10 ** (len(str(value)) - 1))
        else:
            numberOfRec -= 1
    for c in range(10):
        percentage = (int_list.count(c) / numberOfRec) * 100
        bedford_list.append((c, percentage))
    return (bedford_list)


def getDelimiter():
    f = open(os.path.join(current_app.instance_path, 'files', fileName), "r")
    dialect = csv.Sniffer().sniff(f.readline())
    f.seek(0)
    f.close()
    return dialect.delimiter
