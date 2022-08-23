import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "dir_path",
    help="shared directory path",
    type=str
)
args = parser.parse_args()

from flask import Flask, send_file
app = Flask(__name__)


@app.route('/')
def index():
    return "<html><h3>データ</h3><a href='/export/share_data'>ダウンロード</a></html>"


@app.route("/export/share_data")
def export_action_raspi():
    return send_file(
        args.dir_path,
        as_attachment=True
    )


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True,host='0.0.0.0', port=80)
