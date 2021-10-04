import csv, json, math, os
import flask
import pandas as pd
import numpy as np
from flask import Blueprint, render_template, request, current_app

bluePrint = Blueprint("bluePrint", __name__)
file_name = ""
app = flask.Flask(__name__)

@bluePrint.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template("index.html")

@bluePrint.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    os.makedirs(os.path.join(current_app.instance_path, 'files'), exist_ok=True)
    f.save(os.path.join(current_app.instance_path, 'files', f.filename))
    global file_name
    file_name = f.filename
    f = open(os.path.join(current_app.instance_path, 'files', f.filename), "r")
    return render_template("index.html")


@bluePrint.route('/preview')
def preview_file():
    try:
        df = read_data(file_name)
    except Exception as e:
        return "Error reading data. Please check your file"
    return df.to_html(classes='table table-striped table-sm', max_rows=10, table_id="dataframe_table")

@app.errorhandler(400)
@bluePrint.route('/generate')
def generate_chart_data():
    target_field = request.args.get('target')
    try:
        touple_list = generate(os.path.join(current_app.instance_path, 'files', file_name), target_field)
        return json.dumps(touple_list)
    except Exception as e:
        return render_template("error400.html"), 400



@bluePrint.route('/header')
def get_header():
    df = read_data(file_name)
    json_file = json.dumps(df.columns.values.tolist())
    return  json_file


def read_data(file):
    df = pd.read_csv(os.path.join(current_app.instance_path, 'files', file_name), delimiter=get_delimiter())
    return df


def target_list(df, target_column):
    return df[target_column].tolist()


def generate_from_string(file, target_column):
    df = read_data(file_name)
    dataTypeObj = df.dtypes[target_column]
    if dataTypeObj != np.int64 or np.float64:
        return "Cannot use target column"
    column_list = target_list(df, target_column)
    number_of_rec = len(column_list)
    int_list = []
    bedford_list = []
    for i in range(len(column_list)):
        try:
            val = int(str(column_list[i])[0])
            int_list.append(val)
        except Exception as e:
            number_of_rec -= 1
    for c in range(10):
        percentage = (int_list.count(c) / number_of_rec) * 100
        bedford_list.append((c, percentage))
    return (bedford_list)

def generate(file, target_column):
    df = read_data(file_name)
    column_list = target_list(read_data(file_name), target_column)
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


def get_delimiter():
    f = open(os.path.join(current_app.instance_path, 'files', file_name), "r")
    dialect = csv.Sniffer().sniff(f.readline())
    f.seek(0)
    f.close()
    return dialect.delimiter
